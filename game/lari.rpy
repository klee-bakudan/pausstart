init python:
    shake_active = False
    click_count = 0

    def handleEscapeTap():
        global escape_progress, shake_active, click_count
        click_count += 1
        escape_progress = min(escape_progress + 8, 100)
        shake_active = True
        renpy.restart_interaction()

        if escape_progress >= 100:
            return True
    
    def decayEscapeProgress(st):
        global escape_progress
        if escape_progress > 0 and escape_progress < 100:
            escape_progress = max(escape_progress - 0.6, 0)
    
    def shakeUpdate(t, st, at):
        if st < 0.06:
            t.xoffset = renpy.random.randint(-6, 6)
            t.yoffset = renpy.random.randint(-6, 6)
            return 0.02
        else:
            t.xoffset = 0
            t.yoffset = 0
            return None

image escape_run = Animation("images/lari1.png", 0.15, "images/lari2.png", 0.15, repeat = True)

transform shake_transform:
    function shakeUpdate

screen escape_qte:
    modal True
    timer 0.015 action Function(decayEscapeProgress, 0) repeat True

    image "images/bgl.png" at shake_transform
    add "escape_run" xalign 0.5 yalign 0.5

    frame:
        xalign 0.5 yalign 0.92
        background "#000000AA"
        padding (32,20)
        vbox:
            spacing 12
            text "click (mouse kiri) untuk lariiii" color "#F2ECE0" size 36 xalign 0.5 
            # ini nis font minigame lari

            fixed:
                xsize 700
                ysize 24
                add Solid("#3A3550") xsize 700 ysize 24
                add Solid("#D4547A") xsize int(700 * (escape_progress / 100)) ysize 24

        
    button:
        xfill True
        yfill True
        action Function(handleEscapeTap)
        background None

label escape_scene:
    $escape_progress = 0
    call screen escape_qte
    $add_mc_hp(7)
    pause 0.5
    jump act3_lanjut

