label act_4:
    scene act4
    pause 0.5

    scene hutan_bakar
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show mc_terluka zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "baru day 1 nyawa otw melayang"

    show c_mingkem zorder 2:
        xalign 0.02
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    c "tch mendokuse nih perban sendiri"

    hide mc_terluka
    hide c_mingkem

    call play_reassemble_puzzle ("Pieces/puzzle1")

    show plester at item_popup zorder 2
    pause 0.3
    hide plester

    show mc_perban_bagging zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "tolong plis ak dikejar pasukan kerajaan merah"

    show c_mingkem zorder 2:
        xalign 0.02
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    c "..."

    hide c_mingkem

    show c_mangap zorder 2:
        xalign 0.02
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "gwh g pduli"

    hide mc_perban_bagging

    show mc_perban_datar zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "Tapi dia kan pemimpinmu"

    hide mc_perban_datar

    show mc_perban_bingung zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "kamu harus ikut menuntut keadilan dong?!"

    hide c_mangap

    show c_mingkem zorder 2:
        xalign 0.02
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    c "peduli apa gw"

    c "gw masih bisa nyantai kok"

    hide mc_perban_bingung
    hide c_mingkem

    show mc_perban_kesel at vpunch zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "paling ga suka modelan rakyat kek km yang gak mikirin orang lain"

    show c_mangap at vpunch zorder 2:
        xalign 0.02
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    c "(kesel)"

    c "bodo amat emang gw pikirin"

    c "udahlah gw mau ke kerajaan merah dulu bay"

    hide c_mangap
    hide darkoverlay

    pause 0.3

    call play_jalan_puzzle("act_5")
    jump act_5
