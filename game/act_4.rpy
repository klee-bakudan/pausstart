label act_4:
    scene act4 
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

    # minigame

    show mc_perban_bagging zorder 2
    mc "tolong plis ak dikejar pasukan kerajaan merah"
    show c_mingkem zorder 2
    c "..."
    hide c_mingkem
    show c_mangap zorder 2
    mc "gwh g pduli"
    hide mc_perban_bagging
    show mc_perban_datar zorder 2 
    mc "Tapi dia kan pemimpinmu"
    hide mc_perban_datar
    show mc_perban_bingung zorder 2
    mc "kamu harus ikut menuntut keadilan dong?!"
    hide c_mangap
    show c_mingkem zorder 2
    c "peduli apa gw"
    c "gw masih bisa nyantai kok"
    hide mc_perban_bingung
    hide c_mingkem
    show mc_perban_kesel zorder 2
    mc "paling ga suka modelan rakyat kek km yang gak mikirin orang lain"
    show c_mangap zorder 2
    c "(kesel)"
    c "bodo amat emang gw pikirin"
    c "udahlah gw mau ke kerajaan merah dulu bay"
    hide c_mangap
    pause 0.3

    jump act_5



