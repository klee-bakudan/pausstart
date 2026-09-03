## =========================================================
## battle.rpy  (fix: hapus auto-reset guard yang bikin loop,
##              kasih id ke timer dialog musuh, delay musuh
##              dibedain normal vs heavy sesuai mekanik HTML)
## =========================================================

define border_dark   = "#2a1f14"
define panel_bg      = "#efe6d0"
define panel_border  = 3

transform telegraph_in:
    zoom 2.4 rotate -6 alpha 0.0
    ease 0.35 zoom 1.0 rotate 0 alpha 1.0
    block:
        ease 0.25 zoom 1.08
        ease 0.25 zoom 1.0
        repeat

transform flash_fx:
    alpha 0.8
    ease 0.35 alpha 0.0

transform shake_fx:
    xoffset 0
    linear 0.04 xoffset -8
    linear 0.04 xoffset 8
    linear 0.04 xoffset -6
    linear 0.04 xoffset 6
    linear 0.04 xoffset 0

transform charging_fx:
    zoom 1.0
    block:
        ease 0.3 zoom 1.06
        ease 0.3 zoom 1.0
        repeat

transform damage_pop_fx:
    alpha 1.0
    yoffset 0
    parallel:
        easein 0.9 yoffset -55
    parallel:
        pause 0.55
        easein 0.35 alpha 0.0

transform hit_flash_fx:
    alpha 0.0
    linear 0.05 alpha 0.55
    linear 0.2 alpha 0.0
    pause 0.15
    linear 0.05 alpha 0.55
    linear 0.2 alpha 0.0

init python:

    import random
    import time

    in_battle = False

    gauge_max = 5
    heavy_every = 3
    heavy_react_seconds = 2.5
    monster_dialogue_delay_normal = 1.2
    monster_dialogue_delay_heavy = 1.7

    monster_dialogue_lines = [
        "kau kira kebakaran itu kebetulan aja?",
        "DASAR BODOH!",
        "Akulah yang mengendalikan semuanya",
        "SEMUANYA",
        "ratusan ribuan bahkan jutaan",
        "MASIH KURANG",
        "AKAN KU KURAS HABIS DARAH DARI YANG JELITA",
        "lezat, nikmat, mantap",
        "apalagi kalau masih segar",
        "mengalir dari nadi",
        "HUAHAHAHAHA",
        "tidak sabar ku persembahkan",
        "darah paling nikmat dari pemberontak yang jelita",
        "kepada kekasihku yang aku cinta",
        "GRAHHHH",
    ]

    # Pengaman: kalau mc_hp/mc_hp_max belum ke-set di script.rpy, kasih default
    # supaya screen hp_indicator nggak silent-fail.
    if not hasattr(store, "mc_hp_max"):
        mc_hp_max = 1000
    if not hasattr(store, "mc_hp"):
        mc_hp = mc_hp_max

    def add_mc_hp(amount):
        store.mc_hp += amount
        if store.mc_hp > store.mc_hp_max:
            store.mc_hp = store.mc_hp_max
        elif store.mc_hp < 0:
            store.mc_hp = 0
        renpy.notify("HP %+d" % amount)

    config.overlay_screens.append("hp_indicator")

    attack_dmg = 6
    skill_dmg = 12
    monster_atk_dmg = 8
    monster_heavy_dmg = 16
    monster_max_hp = 100

    class Fighter(object):
        def __init__(self, key, name, max_hp):
            self.key = key
            self.name = name
            self.max_hp = max_hp
            self.hp = store.mc_hp if key == "mc" else max_hp
            self.mood = "neutral"
            self.defending = False

        def portrait(self, show_guard=False):
            if not self.is_alive():
                mood = "sad"
            elif self.defending and show_guard:
                mood = "shield"
            else:
                mood = self.mood
            return "images/battle/%s_%s.png" % (mood, self.key)

        def is_alive(self):
            return self.hp > 0

        def take_damage(self, amount):
            self.hp = max(0, self.hp - amount)
            if self.key == "mc":
                store.mc_hp = self.hp
            if self.is_alive():
                self.mood = "angry"
            else:
                self.mood = "sad"
                self.defending = False

        def reset_mood(self):
            if not self.is_alive():
                self.mood = "sad"
                return
            if self.defending:
                return
            self.mood = "sad" if self.hp <= self.max_hp * 0.5 else "neutral"

    class Monster(object):
        def __init__(self, key, name, max_hp):
            self.key = key
            self.name = name
            self.hp = max_hp
            self.max_hp = max_hp
            self.staggered = False

        def portrait(self):
            return "images/battle/monster.png"

        def is_alive(self):
            return self.hp > 0

        def take_damage(self, amount):
            self.hp = max(0, self.hp - amount)

    def make_party():
        try:
            player_display_name = mcname
        except NameError:
            player_display_name = "MC"
        return [
            Fighter("mc", player_display_name, mc_hp_max),
            Fighter("d", "D'dit", 25),
        ]

    party = []
    monster = None

    gauge = 0
    monster_turn_count = 0
    battle_log = "MUSNAHLAH KALIAN"
    chosen_actions = []
    current_actor_index = 0
    battle_over = False
    battle_won = False
    heavy_deadline = None
    last_hit_target = None
    last_hit_is_monster = False
    last_hit_heavy = False
    last_hit_amount = 0
    last_hit_id = 0
    screen_shake_flag = False
    screen_flash_flag = None
    monster_dialogue_active = False
    resolving = False
    resolving_is_skill = False

    def is_next_monster_heavy():
        return (monster_turn_count % heavy_every) == (heavy_every - 1)

    def alive_party():
        return [p for p in party if p.is_alive()]

    def next_actor():
        global current_actor_index
        while current_actor_index < len(party) and not party[current_actor_index].is_alive():
            current_actor_index += 1
        return current_actor_index

    def enter_actor_turn():
        global heavy_deadline, screen_shake_flag, resolving
        # reset shake flag di sini secara langsung, BUKAN lewat timer async,
        # supaya nggak ada proses yang nyelonong di tengah klik tombol
        screen_shake_flag = False
        resolving = False
        idx = next_actor()
        if idx < len(party):
            party[idx].reset_mood()
        if not battle_over and is_next_monster_heavy():
            heavy_deadline = time.time() + heavy_react_seconds
        else:
            heavy_deadline = None

    def heavy_time_left():
        if heavy_deadline is None:
            return None
        remain = heavy_deadline - time.time()
        return max(0.0, min(1.0, remain / heavy_react_seconds))

    def check_heavy_timeout():
        if heavy_deadline is not None and not battle_over:
            if time.time() >= heavy_deadline:
                do_action("timeout")

    def do_action(action_type):
        global current_actor_index, gauge, battle_log, battle_over, battle_won
        global heavy_deadline, screen_shake_flag, screen_flash_flag
        global last_hit_target, last_hit_is_monster, last_hit_amount, last_hit_id
        global resolving, resolving_is_skill

        # Kunci: kalau lagi resolving (masih nunggu delay giliran sebelumnya),
        # klik ga akan diproses. Ini yang mencegah klik numpuk "ketelan" ke
        # giliran berikutnya (persis kayak flag `resolving` di demo HTML).
        if resolving or battle_over or monster_dialogue_active:
            return

        resolving = True
        resolving_is_skill = (action_type == "skill")

        heavy_deadline = None
        last_hit_target = None
        last_hit_is_monster = False
        actor = party[current_actor_index]

        if action_type == "attack":
            dmg = attack_dmg
            monster.take_damage(dmg)
            gauge = min(gauge_max, gauge + 1)
            battle_log = "%s menyerang %s! -%d HP." % (actor.name, monster.name, dmg)
            screen_shake_flag = True
            last_hit_is_monster = True
            last_hit_amount = dmg
            last_hit_id += 1

        elif action_type == "defend":
            actor.defending = True
            battle_log = "%s bersiap bertahan." % actor.name

        elif action_type == "skill":
            dmg = skill_dmg
            monster.take_damage(dmg)
            monster.staggered = True
            actor.mood = "happy"
            gauge = 0
            battle_log = "%s pakai SKILL! %s -%d HP & kena Stagger." % (actor.name, monster.name, dmg)
            screen_shake_flag = True
            screen_flash_flag = "white"
            last_hit_is_monster = True
            last_hit_amount = dmg
            last_hit_id += 1

        elif action_type == "timeout":
            battle_log = "%s telat bereaksi! Gagal bertahan tepat waktu..." % actor.name

        if not monster.is_alive():
            battle_over = True
            battle_won = True
            battle_log += "\n\n%s dikalahkan!" % monster.name
            return
        # resolving TETAP True di sini, sengaja — supaya tombol nggak lagi
        # bisa diklik pas battle_over. Screen battle_over yang akan ambil alih.

    def finish_player_action():
        # Dipanggil lewat timer di screen, ~0.9-1.1 detik SETELAH do_action,
        # persis kayak setTimeout di commitAction() pada demo HTML.
        # Di sinilah giliran baru benar-benar pindah & tombol baru muncul.
        global current_actor_index, resolving
        resolving = False
        current_actor_index += 1
        while current_actor_index < len(party) and not party[current_actor_index].is_alive():
            current_actor_index += 1

        if current_actor_index >= len(party):
            monster_turn()
        else:
            enter_actor_turn()

    def monster_turn():
        global battle_log, battle_over, battle_won, monster_turn_count
        global last_hit_target, last_hit_is_monster, last_hit_heavy, screen_shake_flag, screen_flash_flag
        global last_hit_amount, last_hit_id, monster_dialogue_active

        targets = alive_party()
        if not targets:
            battle_over = True
            battle_won = False
            return

        target = random.choice(targets)
        heavy = is_next_monster_heavy()
        dmg = monster_heavy_dmg if heavy else monster_atk_dmg

        if monster.staggered:
            dmg = dmg // 2
            monster.staggered = False

        if target.defending:
            dmg = int(dmg * (0.4 if heavy else 0.5))

        target.take_damage(dmg)
        last_hit_target = party.index(target)
        last_hit_is_monster = False
        last_hit_heavy = heavy
        last_hit_amount = dmg
        last_hit_id += 1
        screen_shake_flag = True
        if heavy:
            screen_flash_flag = "red"

        if monster_turn_count < len(monster_dialogue_lines):
            speech = monster_dialogue_lines[monster_turn_count]
        else:
            speech = monster_dialogue_lines[monster_turn_count % len(monster_dialogue_lines)]

        battle_log = speech
        monster_turn_count += 1

        if not alive_party():
            battle_over = True
            battle_won = False
            return

        monster_dialogue_active = True

    def finish_monster_turn():
        global monster_dialogue_active, current_actor_index
        monster_dialogue_active = False
        for p in party:
            p.defending = False
            p.reset_mood()
        if battle_over or not alive_party():
            return
        current_actor_index = 0
        next_actor()
        enter_actor_turn()

    def reset_battle():
        global party, monster, battle_log, chosen_actions, current_actor_index
        global battle_over, battle_won, gauge, monster_turn_count, heavy_deadline
        global last_hit_target, last_hit_is_monster, last_hit_heavy, screen_shake_flag, screen_flash_flag
        global last_hit_amount, last_hit_id, monster_dialogue_active, resolving
        party = make_party()
        monster = Monster("monster", "SKRIMER", monster_max_hp)
        gauge = 0
        monster_turn_count = 0
        battle_log = "MUSNAHLAH KALIAN"
        chosen_actions = []
        current_actor_index = 0
        battle_over = False
        battle_won = False
        heavy_deadline = None
        last_hit_target = None
        last_hit_is_monster = False
        last_hit_heavy = False
        last_hit_amount = 0
        last_hit_id = 0
        screen_shake_flag = False
        screen_flash_flag = None
        monster_dialogue_active = False
        resolving = False
        enter_actor_turn()

# screen battle
screen hp_indicator():
    zorder 100
    if not in_battle:
        frame:
            xpos 0
            xanchor 0.0
            xoffset 10
            ypos 5
            background Solid(border_dark)
            padding (2, 2)
            frame:
                background Solid(panel_bg)
                padding (8, 4)
                hbox:
                    spacing 6
                    text "MC HP" size 13 color "#181428" bold True
                    bar value mc_hp range mc_hp_max xsize 100 ysize 12 left_bar Solid("#c0392b") right_bar Solid("#3a2a1a")
                    text "[mc_hp]/[mc_hp_max]" size 12 color "#181428"

screen battle_screen():

    tag menu
    zorder 0

    # >>> FIX: guard "if monster is None or not party: $ reset_battle()"
    # yang ada di versi sebelumnya DIHAPUS. Guard itu jalan tiap screen
    # di-render ulang dan jadi penyebab loop full-HP-reset. reset_battle()
    # sekarang cuma dipanggil sekali dari `label battle`, persis kayak di
    # screens_battle.rpy v10 yang sudah terbukti jalan normal.

    add "images/battle/bg.png"

    # ---------- Panel party: posisi absolut persis ----------
    for i, fighter in enumerate(party):
        $ fighter_at = shake_fx if (screen_shake_flag and not last_hit_is_monster and last_hit_target == i) else Transform()
        $ is_current_turn = (i == current_actor_index and not battle_over and not monster_dialogue_active)
        $ mood_shown = ("DEAD" if not fighter.is_alive() else ("GUARD" if (fighter.defending and is_current_turn) else fighter.mood.upper()))

        $ fx, fy = (77, 108) if i == 0 else (1285, 108)
        $ ax, ay = (103, 132) if i == 0 else (1311, 132)
        $ bx, by = (103, 244) if i == 0 else (1311, 244)
        $ px, py = (139, 254) if i == 0 else (1361, 254)

        $ atas_rel = (ax - fx, ay - fy)
        $ bawah_rel = (bx - fx, by - fy)
        $ portrait_rel = (px - bx, py - by)

        $ frame_w, frame_h = renpy.image_size("images/battle/frame.png")
        $ border_thick = 8
        $ border_gap = 6

        fixed:
            xpos fx
            ypos fy
            at fighter_at

            if is_current_turn:
                add Solid("#ffd54f") xpos -border_gap ypos -border_gap xsize (frame_w + border_gap*2) ysize border_thick
                add Solid("#ffd54f") xpos -border_gap ypos (frame_h + border_gap - border_thick) xsize (frame_w + border_gap*2) ysize border_thick
                add Solid("#ffd54f") xpos -border_gap ypos -border_gap xsize border_thick ysize (frame_h + border_gap*2)
                add Solid("#ffd54f") xpos (frame_w + border_gap - border_thick) ypos -border_gap xsize border_thick ysize (frame_h + border_gap*2)

            add "images/battle/frame.png"

            frame:
                xpos atas_rel[0]
                ypos atas_rel[1]
                background Image("images/battle/kotak_atas.png")
                text "[mood_shown]" size 14 color ("#ff4444" if not fighter.is_alive() else "#181428") xalign 0.5 bold True

            frame:
                xpos bawah_rel[0]
                ypos bawah_rel[1]
                background Image("images/battle/kotak_bawah.png")
                fixed:
                    xpos portrait_rel[0]
                    ypos portrait_rel[1]
                    add fighter.portrait(show_guard=is_current_turn)
                    if last_hit_id > 0 and (not last_hit_is_monster) and last_hit_target == i:
                        add AlphaMask(Solid("#3a6fd8"), fighter.portrait(show_guard=is_current_turn)):
                            id "partyhitflash_%d_%d" % (last_hit_id, i)
                            at hit_flash_fx
                    if not fighter.is_alive():
                        add AlphaMask(Solid("#888888cc"), fighter.portrait(show_guard=is_current_turn))

            hbox:
                xpos bawah_rel[0]
                ypos (bawah_rel[1] + 210)
                spacing 4
                text "♥" color "#c0392b" size 18
                bar value fighter.hp range fighter.max_hp xsize 130 ysize 14 left_bar Solid("#c0392b") right_bar Solid("#3a2a1a")
                text "[fighter.hp]/[fighter.max_hp]" size 13 color "#181428"

    # ---------- Monster ----------
    $ monster_charging_at = charging_fx if (not battle_over and is_next_monster_heavy()) else Transform()
    $ monster_hit_at = shake_fx if (screen_shake_flag and last_hit_is_monster) else Transform()

    text "[monster.name] — [monster.hp]/[monster.max_hp]" size 18 color "#efe6d0" xpos 642 ypos 130
    bar value monster.hp range monster.max_hp xsize 260 ysize 16 xpos 642 ypos 160 left_bar Solid("#c0392b") right_bar Solid("#3a2a1a")

    fixed:
        xpos 642
        ypos 237
        at monster_hit_at, monster_charging_at
        add monster.portrait()
        if last_hit_id > 0 and last_hit_is_monster:
            add AlphaMask(Solid("#3a6fd8"), monster.portrait()):
                id "monsterhitflash_%d" % last_hit_id
                at hit_flash_fx

    # Log & skill gauge
    frame:
        xsize 620
        xalign 0.5
        ypos 480
        background Solid(border_dark)
        padding (panel_border, panel_border)
        frame:
            background Solid(panel_bg)
            padding (16, 10)
            xfill True
            text battle_log size 16 color "#181428"

    frame:
        xalign 0.5
        ypos 560
        background Solid(border_dark)
        padding (panel_border, panel_border)
        frame:
            background Solid(panel_bg)
            padding (10, 8)
            has vbox
            xalign 0.5
            spacing 2
            text "SKILL BAR" size 12 color "#8a5a1c" xalign 0.5 bold True
            hbox:
                xalign 0.5
                spacing 5
                for i in range(gauge_max):
                    frame:
                        xsize 30
                        ysize 16
                        background (Solid("#e8b23c") if i < gauge else Solid("#3a3560"))
            if gauge >= gauge_max:
                text "SKILL SIAP DIPAKAI!" size 13 color "#8a5a1c" xalign 0.5

    # ---------- Telegraph heavy attack ----------
    if not battle_over and is_next_monster_heavy():
        frame:
            xalign 0.5
            ypos 10
            background "#d94b2b"
            padding (16, 8)
            at telegraph_in
            has vbox
            xalign 0.5
            text "⚠ HEAVY ATTACK ⚠  MUSUH BERSIAP — DEFEND!" size 16 color "#ffffff" bold True xalign 0.5

        $ time_left = heavy_time_left()
        if time_left is not None:
            $ heavy_bar_color = Solid("#d94b2b") if time_left < 0.34 else Solid("#2fa6a0")
            frame:
                xalign 0.5
                ypos 46
                xsize 260
                background None
                bar value int(time_left*100) range 100 xsize 260 ysize 10 left_bar heavy_bar_color right_bar Solid("#3a2a1a")
            timer 0.05 repeat True action Function(check_heavy_timeout)

    # ---------- Angka damage pop-up ----------
    if last_hit_id > 0:
        if last_hit_is_monster:
            frame:
                xpos 642
                ypos 210
                background None
                text ("-%d" % last_hit_amount):
                    id "dmgpop_%d" % last_hit_id
                    size 34
                    bold True
                    color "#ffffff"
                    outlines [(absolute(2), "#000000", absolute(0), absolute(0))]
                    at damage_pop_fx
        else:
            $ pop_x = 139 if last_hit_target == 0 else 1361
            frame:
                xpos pop_x
                ypos 220
                background None
                text ("-%d" % last_hit_amount):
                    id "dmgpop_%d" % last_hit_id
                    size 34
                    bold True
                    color "#ffffff"
                    outlines [(absolute(2), "#000000", absolute(0), absolute(0))]
                    at damage_pop_fx

    # ---------- Battle over: cek HP langsung, tanpa UI apapun ----------
    if battle_over:
        $ mc_alive_now = party[0].is_alive()
        $ ddit_alive_now = party[1].is_alive()
        $ party_wiped = (not mc_alive_now) and (not ddit_alive_now)
        timer 0.05 action Return(not party_wiped)

    elif monster_dialogue_active:
        # >>> FIX: dikasih id supaya timer ini nggak restart tiap re-render,
        # dan delay-nya dibedain normal vs heavy (1.2s / 1.7s), sesuai
        # mekanik enemyTurn() di demo HTML (1200ms / 1700ms).
        $ dialogue_delay = monster_dialogue_delay_heavy if last_hit_heavy else monster_dialogue_delay_normal
        timer dialogue_delay action Function(finish_monster_turn) id "monster_dialogue_timer"

    elif resolving:
        # Jeda sebelum giliran berikutnya muncul (900ms biasa, 1100ms skill),
        # persis kayak setTimeout di demo HTML. Tombol nggak dirender sama
        # sekali di sini, jadi ga ada yang bisa "ketelan" diklik.
        # id dikasih supaya timer ini ga restart tiap screen re-render.
        timer (1.1 if resolving_is_skill else 0.9) action Function(finish_player_action) id "resolve_timer"

    elif current_actor_index < len(party):
        $ actor = party[current_actor_index]
        $ skill_ready = gauge >= gauge_max
        $ defend_bg = Solid("#bfe8df") if is_next_monster_heavy() else None
        $ skill_label = u"SKILL ⚡" if skill_ready else "SKILL"
        $ skill_bg = Solid("#e8b23c") if skill_ready else None

        text "What should [actor.name] do?" size 16 color "#efe6d0" bold True xalign 0.5 ypos 875

        textbutton "ATTACK":
            id "btn_attack"
            xpos 602
            ypos 929
            text_size 16
            action Function(do_action, "attack")

        textbutton "DEFEND":
            id "btn_defend"
            xpos 848
            ypos 929
            text_size 16
            background defend_bg
            action Function(do_action, "defend")

        textbutton skill_label:
            id "btn_skill"
            xpos 1095
            ypos 929
            text_size 16
            sensitive skill_ready
            background skill_bg
            action Function(do_action, "skill")

    # ---------- Kilatan layar (paling akhir = paling atas) ----------
    if screen_flash_flag == "white":
        frame:
            background Solid("#FFFFFF")
            xfill True
            yfill True
            at flash_fx
        timer 0.4 action SetVariable("screen_flash_flag", None)
    elif screen_flash_flag == "red":
        frame:
            background Solid("#D94B2B")
            xfill True
            yfill True
            at flash_fx
        timer 0.5 action SetVariable("screen_flash_flag", None)


label battle:
    $ in_battle = True
    $ renpy.block_rollback()
    $ reset_battle()
    call screen battle_screen
    $ battle_result = _return
    $ in_battle = False
    $ renpy.block_rollback()

    if battle_result:
        jump ending_b
    else:
        jump ending_a