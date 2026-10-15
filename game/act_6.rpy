label act_6:
    scene act6
    pause 0.5

    scene kastil_putih
    pause 0.5
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show d_senyum-fix zorder 2:
        xalign 1.0
        yalign 0.25
    d "Aku telah membawa penyelamat kita~ Ratu Putih."
    hide d_senyum-fix 

    show s_datar zorder 2:
        xalign 1.0
        yalign 0.25
    s " Dia...[mcname]?"
    s "Pahlawan yang akan menyelamatkan dunia ini dari malapetaka?"
    hide s_datar
    show s_mangap zorder 2:
        xalign 1.0
        yalign 0.25
    s "Tolong.."
    s "Tolonglah selamatkan kami wahai penyelamat"
    hide s_mangap
    
    show pedang at item_popup zorder 2

    pause 1

    hide pedang
    
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show mc_baju_bingung zorder 2:
        xalign 0.99
        yalign 0.25
    mc "Pedang ini..Apakah ini bisa mengalahkan malapetaka itu?"
    hide mc_baju_bingung
    
    show s_mangap zorder 2:
        xalign 1.0
        yalign 0.25
    s " Iya… ini adalah pedang kuno yang telah disucikan oleh air suci"
    s "jika kamu butuh sesuatu silakan gunakan air ini sebelum melawan malapetaka di kastil merah"
    hide s_mangap

    hide mc_baju_bingung
    show mc_baju_senang zorder 2:
        xalign 0.99
        yalign 0.25
    mc "Terima kasih, Yang Mulia"
    hide mc_baju_senang

    show mc_baju_berpikir zorder 2:
        xalign 0.99
        yalign 0.25
    mc "{color=#7e6d2f}(heumm keknya aku bisa buat sesuatu pakai air suci ini){/color}"
    hide mc_baju_berpikir

    call molotov_scene from _call_molotov_scene
    $add_mc_hp(7)

    show molotov at item_popup zorder 2

    pause 2.0

    hide molotov
    hide darkoverlay

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5

    show d_senyum-fix at expression_pop zorder 2:
        xalign 1.0
        yalign 0.25

    d "Sudah waktunya kita berangkat~ si kucing sudah membobol keamanan kastil merah"
    hide d_senyum-fix

    show d_datar-fix:
        xalign -0.05
        yalign 0.25
    with ease


    show mc_baju_kaget zorder 2:
        xalign 0.99
        yalign 0.25
    mc "Ehh kucing..? eum oke deh"
    hide mc_baju_kaget
    
    show mc_baju_datar:
        xalign 0.99
        yalign 0.25
    with ease
    
    show d_senyum-fix zorder 2:
        xalign -0.05
        yalign 0.25
    d "btw nanti disana kamu sendiri ya~ aku kan buronan raja"
    d "(tertawa)"
    hide d_senyum-fix

    scene jamurkb
    pause 0.3
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show j_bayang zorder 2
    j "hayooo didit mau kemana hayoo"
    hide j_bayang

    show d_kesel-fix at expression_pop zorder 2:
        xalign 0.5
        yalign 0.5
    d "####"
    d "in three, two, one~"
    hide d_kesel-fix

    call dor from _call_dor 

    
label act_6lanjut:
    scene jamurkb
    pause 0.3
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show d_kesel-fix at expression_pop zorder 2:
        xalign 0.5
        yalign 0.5
    d "tch"
    d "hampir aja masuk backroom"
    hide d_kesel-fix

    show j_mangap at expression_pop zorder 2:
        xalign 0.5
        yalign 0.5

    j "SIALANN"
    call play_jalan_puzzle("act_7") from _call_play_jalan_puzzle_4
    $add_mc_hp(7)
    jump act_7


    return