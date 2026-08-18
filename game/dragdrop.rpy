init python:
    kain_used = 0
    permata_used = 0
    air_used = 0

    def itemDropped(drags, drop):
        global kain_used, permata_used, air_used

        if drop is None:
            return

        for d in drags:
            if d.drag_name == "kain" and kain_used == 0:
                kain_used = 1
                d.draggable = False
            elif d.drag_name == "permata" and permata_used == 0:
                permata_used = 1
                d.draggable = False
            elif d.drag_name == "air" and air_used == 0:
                air_used = 1
                d.draggable = False
                
        renpy.restart_interaction()

        if kain_used == 1 and permata_used == 1 and air_used == 1:
            return True

screen molotov_minigame:
    add "images/bgd.png"

    text "buat molotov menggunakan air suci" xpos 70 ypos 40 bold True color "#FFFFFF" size 36
    # anu nis font

    frame:
        xpos 70 ypos 160
        background "#000000AA" 
        padding (20, 14)
        vbox:
            spacing 8
            text "progres: " color "#F2ECE0" size 24
            fixed:
                xsize 300
                ysize 20
                add Solid("#3A3550") xsize 300 ysize 20
                add Solid("#7ec98f") xsize int(300 * (kain_used + permata_used + air_used) / 3)ysize 20

    add "images/border.png" xpos 810 ypos 80

    draggroup:
        drag:
            drag_name "botol_target"
            xpos 36 ypos 121
            child "images/botol.png"
            draggable False
            droppable True

        if air_used == 0:
            drag:
                drag_name "air"
                xpos 960 ypos 284
                child "images/air.png"
                draggable True
                droppable False 
                dragged itemDropped
        if permata_used == 0:
            drag:
                drag_name "permata"
                xpos 1366 ypos 158
                child "images/permata.png"
                draggable True
                droppable False 
                dragged itemDropped
        if kain_used == 0:
            drag:
                drag_name "kain"
                xpos 1171 ypos 566
                child "images/kain.png"
                draggable True
                droppable False 
                dragged itemDropped

label molotov_scene:
    $kain_used = 0
    $permata_used = 0
    $air_used = 0
    call screen molotov_minigame
    return
