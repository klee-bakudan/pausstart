label act_4:
    scene act4 
    pause 0.5

    scene hutan_bakar
    pause 0.5
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show mc_terluka zorder 2
    pause 0.3
    mc "baru day 1 nyawa otw melayang"
    show c_mingkem zorder 2
    c "tch mendokuse nih perban sendiri"
    hide mc_terluka
    hide c_mingkem

    call play_reassemble_puzzle ("Pieces/puzzle1")

    show plester zorder 2
    pause 0.3
    hide plester

    show mc_perban_bagging zorder 2:
        xalign 0.98
        yalign 0.25

    mc "tolong plis ak dikejar pasukan kerajaan merah"
    show c_mingkem zorder 2:
        xalign 0.02
        yalign 0.25

    c "..."
    hide c_mingkem
    show c_mangap at popup_left zorder 2:
        xalign 0.02
        yalign 0.25
    mc "tch.. gue ga peduli"
    hide mc_perban_bagging
    show mc_perban_datar zorder 2:
        xalign 0.98
        yalign 0.25
    mc "Lah.. Tapi dia kan pemimpinmu, gimanasih??"
    hide mc_perban_datar
    show mc_perban_bingung at popup_right zorder 2:
        xalign 0.98
        yalign 0.25
    mc "kamu harus ikut menuntut keadilan dong?!"
    hide c_mangap
    show c_mingkem zorder 2:
        xalign 0.02
        yalign 0.25
    c "peduli apa gue"
    c "gue masih bisa nyantai kok"
    hide mc_perban_bingung
    hide c_mingkem
    show mc_perban_kesel at popup_right zorder 2:
        xalign 0.98
        yalign 0.25
    mc "paling ga suka modelan rakyat kek kamu yang gak mikirin orang lain"
    show c_mangap zorder 2:
        xalign 0.02
        yalign 0.25
    c "(kesel)"
    c "bodo amat emang gue pikirin"
    c "udahlah gue mau ke kerajaan merah dulu bay"
    hide c_mangap with dissolve
    pause 0.3
    
    show mc_perban_kesel at popup_right zorder 2:
        xalign 0.98
        yalign 0.25

    mc "Yaelah lanjut ke tea party aja deh"
    hide mc_perban_kesel with dissolve

    call play_jalan_puzzle("act_5")
    $add_mc_hp(7)
    jump act_5



