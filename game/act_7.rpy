define debat_kastil = [("apa maksudnya?", None),
("Heri jadi gila gegara rumah dan keluarganya terbakar", None), ("nyawa udah ga ada harganya", None),
("darah? muda?", "jadi ini tumbal darah biar muda"),
("Banyak kebakaran dan kerusakan", "itu disengaja"),
("monster itu ratu", "ratu meminum darah")]

label act_7:
    play sound "audio/transition-act.mp3"
    pause 1.0

    scene act7
    with dissolve
    
    pause 6.0
    stop sound


    scene taman_kastil-merah
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show mc_baju_datar zorder 2:
        xalign 0.9
        yalign 0.2
    # anu ini ganti aset mc baju datar
    # anu kasih warna text dalam hati yang text dia pake ()
    mc "{color=#7e6d2f}(wah kastinya ngastil banget){/color}"
    mc "{color=#7e6d2f}(tapi..kenapa firasatku gak enak ya){/color}"
    hide mc_baju_datar

    show pelayan at expression_pop zorder 2:
        xalign 1.0
        yalign 0.25
    pl "anda ini siapa?"
    hide pelayan
    show pelayan:
        xalign 0.08
        yalign 0.25
    with ease

    show mc_baju_kaget zorder 2:
        xalign 0.9
        yalign 0.2
    mc "eum a- ano-"
    hide mc_baju_kaget
    hide pelayan
    show mc_baju_datar:
        xalign 0.2
        yalign 0.2
    with ease

    show c_mangap at expression_pop zorder 2:
        xalign 0.92
        yalign 0.25
    c "tch dasar gak sopan"
    hide c_mangap

    show c_mingkem:
        xalign 0.92
        yalign 0.25
    with ease

    show mc_baju_huft zorder 2:
        xalign 0.2
        yalign 0.2
    mc "(huft dat so kripi)"
    hide mc_baju_huft 

    show mc_baju_datar:
        xalign 0.2
        yalign 0.2
    with ease

    hide c_mingkem
    show c_mangap zorder 2:
        xalign 0.92
        yalign 0.25
    c "dia ini bangsawan"
    hide c_mangap
    show c_mingkem:
        xalign 0.92
        yalign 0.25
    with ease
    
    hide mc_baju_datar
    show pelayan zorder 2:
        xalign 0.1
        yalign 0.25
    pl "o-oh maaf yang mulia hamba sudah lancang.."

    show c_mangap zorder 2:
        xalign 0.92
        yalign 0.25
    c "ya, sana minggir"
    hide pelayan 
    hide c_mangap

    show c_mingkem:
        xalign 0.92
        yalign 0.25
    with ease
    show mc_baju_senang zorder 2:
        xalign 0.2
        yalign 0.2
    mc "eh kucing? makasi ya"
    hide mc_baju_senang

    show mc_baju_datar:
        xalign 0.2
        yalign 0.2
    with ease

    show c_mangap zorder 2:
        xalign 0.92
        yalign 0.25
    c "chiro"
    hide c_mangap

    show c_mingkem:
        xalign 0.92
        yalign 0.25
    with ease
    show mc_baju_kaget at expression_pop zorder 2:
        xalign 0.2
        yalign 0.2
    mc "ah"
    hide mc_baju_kaget

    show mc_baju_senang zorder 2:
        xalign 0.2
        yalign 0.2
    mc "makasi ya chiro"
    hide c_mingkem

    hide mc_baju_senang

    show mc_baju_datar:
        xalign 0.2
        yalign 0.2
    with ease
    show c_mangap zorder 2:
        xalign 0.92
        yalign 0.25
    c "yh"
    hide c_mangap
    hide mc_baju_datar

    #bg taman kastil merah 
    
    "/bisik"

    show l_datar zorder 2:
        xalign 0.99
        yanchor 0.9
        ypos 800
    l "hey [mcname]"
    hide l_datar

    show l_datar:
        xalign 0.02
        yanchor 1.0
        ypos 920
    with ease

    show mc_baju_kaget at expression_pop zorder 2:
        xalign 0.9
        yalign 0.2
    mc "EH LUR-"
    hide mc_baju_kaget
    show mc_baju_datar:
        xalign 0.9
        yalign 0.2
    with ease

    hide l_datar 

    show l_takut at expression_pop zorder 2:
        xalign 0.1
        yanchor 0.87
        ypos 920
    l "ssstt"
    hide l_takut

    show l_datar:
        xalign 0.02
        yanchor 1.0
        ypos 920
    with ease

    show mc_baju_bingung zorder 2:
        xalign 0.9
        yalign 0.2
    mc "uh.. jadi ini tempatnya?"
    hide mc_baju_bingung

    show mc_baju_datar:
        xalign 0.9
        yalign 0.2
    with ease
    hide l_datar

    show l_datar zorder 2:
        xalign 0.02
        yanchor 1.0
        ypos 920
    l "iya, btw kamu nanti pura-pura ga kenal aku ya"

    show l_datar at expression_pop zorder 2:
        xalign 0.02
        yanchor 1.0
        ypos 920
    l "takut ketauan ih"
    hide l_datar
    hide mc_baju_datar

    show k_terang zorder 2:
        xalign 0.9
    
    k "baby you look so soo magnificent"
    hide k_terang

    show k_gelap:
        xalign 0.2
    with ease 

    show q_terang at expression_pop zorder 2:
        xalign 0.9
    q "apasih sayang ih"
    hide q_terang
    hide k_gelap

    show mc_baju_datar zorder 2:
        xalign 0.5
        yalign 0.5
    # ganti mc datar
    pause 5.0
    hide mc_baju_datar

    show q_gelap zorder 2:
        xalign 0.9
    q "honey can i get that"
    hide q_gelap
    show q_gelap at expression_pop zorder 2:
        xalign 0.9
    q "dia terlihat sangat muda dan manis, pasti darahnya juga manis"
    hide q_gelap

    show q_gelap:
        xalign 0.2
    with ease

    show k_gelap zorder 2:
        xalign 0.9
    k "tentu saja istriku, akan aku sajikan dia sebagai dessert mu malam ini"
    hide k_gelap
    show k_gelap at expression_pop zorder 2:
        xalign 0.9
    k "so you can stay magnificent forever and ever baby"
    hide q_gelap
    hide k_gelap
    
    show mc_baju_takut zorder 2:
        xalign 0.9
        yalign 0.2
    # ganti mc baju takut
    mc "{color=#7e6d2f}(what the hell is going on){/color}"
    mc "{color=#7e6d2f}(ini maksudnya aku kah){/color}"
    mc "{color=#7e6d2f}(who are they talking about?){/color}"
    hide mc_baju_takut

    show mc_baju_berpikir
    label minigame_kastil:
        $choice_positions = [
            (50, 100),  
            (700, 50), 
            (1350, 100), 
            (50, 450), 
            (700, 450), 
            (1350, 450)]
        
        $ renpy.music.set_volume(1.0, channel="music")
        $ renpy.music.play("audio/debat-bg.mp3", channel="music", loop=True)

        call screen bubble_choicef(debat_kastil)
        $ hasil = _return
        
        $ renpy.music.stop(channel="music", fadeout=1.0)

    hide mc_baju_berpikir

    show k_gelap zorder 2:
        xalign 0.9
    k "bawakan aku anak itu"
    hide k_gelap
    show k_gelap:
        xalign 0.1
    with ease
    show j_siap at expression_pop zorder 2:
        xalign 0.9
    j "SIAP LAKSANAKAN!"
    hide j_siap
    hide k_gelap

    # show mc_baju_berpikir zorder 2
    # pause 0.3
    # show j_bayang zorder 2
    # hide j_bayang
    # hide mc_baju_berpikir

    scene hitam
    show d_kesel-fix zorder 2:
        xalign 0.2
        yalign 0.9
    d "huhft untung aja aku ga telat"
    hide d_kesel-fix

    show mc_baju_takut at expression_pop zorder 2:
        xalign 0.9
        yalign 0.2
    mc "D-D-dit!"
    hide mc_baju_takut

    scene kastil_merah 
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show mc_baju_takut zorder 2:
        xalign 0.9
        yalign 0.2
    # ganti takut
    mc "aku mendengarnya"
    hide mc_baju_takut
    show mc_baju_kaget at expression_pop zorder 2:
        xalign 0.9
        yalign 0.2
    mc "mereka minum darah!"
    hide mc_baju_kaget
    show d_datar-fix zorder 2:
        xalign 0.2
        yalign 0.9
    d "mereka sudah menargetkanmu"
    hide d_datar-fix
    show d_kesel-fix at expression_pop zorder 2:
        xalign 0.2
        yalign 0.9
    d "kita udah ga bisa tinggal diam"
    hide d_kesel-fix
    show mc_baju_kaget at expression_pop zorder 2:
        xalign 0.9
        yalign 0.2
    mc "apa maksudmu?"
    hide mc_baju_kaget
    show d_datar-fix zorder 2:
        xalign 0.2
        yalign 0.9
    d "sekarang"
    hide d_datar-fix
    show d_kesel-fix at expression_pop zorder 2:
        xalign 0.2
        yalign 0.9
    d "KITA AKAN LAWAN"
    hide d_kesel-fix
    hide mc_baju_takut
    hide d_kesel

    
    show d_datar-fix zorder 2:
        xalign 1.0
        yalign 0.25
    pause 0.5
    hide d_datar-fix

    show j_siap zorder 2:
        xalign 1.0
        yalign 0.25
    j "LOH LOH DIDIT!!"
    hide j_siap
    window hide 

    show k_terang zorder 2:
        xalign 0.008
        yalign 0.5
    show q_terang zorder 2:
        xalign 1.0
        yalign 0.5

    pause 0.5

    hide k_terang
    hide q_terang

    show k_gelap zorder 2:
        xalign 1.0
        yalign 0.5
    k "PRAJURIT GA BECUS!"
    hide k_gelap

    show q_gelap zorder 2:
        xalign 1.0
        yalign 0.5

    q "do you need my help baby~"
    hide q_gelap

    show k_gelap zorder 2:
        xalign 1.0
        yalign 0.5
    k "OFF WITH THEIR HEAD"
    play sound "audio/monster-cry.mp3"
    hide k_gelap
    
    "/semua orang membeku"
    pause 5.0

    show k_gelap zorder 2:
        xalign 1.0
        yalign 0.5
    k "didit… didit… kali ini kau ga akan bisa lepas"
    k "DAN KAU DAN KAU DAN KALIAN SEMUA MUSNAH HUAHAHAHA"
    k "dan istriku akan jelita selamanya"
    hide k_gelap
    show mc_baju_takut at expression_pop zorder 2:
        xalign 0.9
        yalign 0.2
    hide mc_baju_takut
    show mc_baju_datar:
        xalign 0.9
        yalign 0.2
    with ease
    show d_senyum-fix zorder 2:
        xalign 0.1
        yalign 0.9
        xanchor 500
    d "ampyunn dech masih aja sok sok an"
    hide d_senyum-fix

    show d_senyum-fix at expression_pop zorder 2:
        xalign 0.1
        yalign 0.9
        xanchor 500
    d "hey [mcname] sudah saatnya kita musnahkan raja bodoh dan ratu jelek itu"
    hide d_senyum-fix
    show d_datar-fix:
        xalign 0.1
        yalign 0.9
        xanchor 500
    with ease
    hide mc_baju_datar 
    show mc_baju_huft at expression_pop zorder 2:
        xalign 0.9
        yalign 0.2
    mc "..."
    hide d_senyum-fix
    hide mc_baju_huft

    call battle from _call_battle
    
label ending_a:

    play music "audio/bad-ending.mp3"

    scene hitam
    pause 0.5

    scene tea_party

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5

    show a_datar zorder 2

    d "akhirnya kamu bangun setelah 4 bulan tidur"

    hide a_datar

    mc "hah...aku kalah..?"

    scene hutan_bakar
    pause 0.5

    scene jamur asap
    pause 0.5

    scene hitam
    pause 0.3

    call screen credits_screen

    $ mc_hp = 0
    $ renpy.full_restart()

label ending_b:

    play music "audio/good-ending.mp3"

    scene putih
    pause 0.5

    scene ruangs
    pause 0.5

    show l_bling

    l "terima kasih penyelamat.."

    hide l_bling

    mc "selamat tinggal....."

    "(sedih)"

    scene putih
    "(mc kembali ke dunia nyata)"

    scene gorong
    pause 0.3

    call screen credits_screen

    $ renpy.full_restart()