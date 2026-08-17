label act_6:
<<<<<<< HEAD
    play sound "audio/transition-act.mp3"
    pause 1.0

    scene act6
    with dissolve
=======
    scene act6
    pause 0.5

    scene kastil_putih
    pause 0.5
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show d_senyum zorder 2
    d "Aku telah membawa penyelamat kita~ Ratu Putih."
    hide d_senyum

    show s_datar zorder 2
    s " Dia..."
    s "dia yang akan menyelamatkan dunia ini dari malapetaka?"
    hide s_datar
    show s_mangap zorder 2
    s "Tolong.."
    s "Tolonglah selamatkan kami wahai penyelamat"
    hide s_mangap

    show pedang zorder 2
    pause 0.5
    hide pedang
>>>>>>> a05a961d6961a4f940f3c4c34efb966269094c9f
    
    pause 6.0
    stop sound

<<<<<<< HEAD
    scene kastil_putih
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5

    show d_senyum zorder 2:
        xalign 1.0
        yalign 0.25
    d "Aku telah membawa penyelamat kita~ Ratu Putih."
    hide d_senyum

    show s_datar zorder 2:
        xalign 1.0
    s " Dia..."
    s "dia yang akan menyelamatkan dunia ini dari malapetaka?"
    hide s_datar
    show s_mangap zorder 2
    s "Tolong.."
    s "Tolonglah selamatkan kami wahai penyelamat"
    hide s_mangap

    show pedang at item_popup zorder 2

    pause 2.0


    hide pedang
    hide darkoverlay
    
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5

    show mc_baju_bingung zorder 2
    mc "Pedang ini..Apakah ini bisa mengalahkan malapetaka itu?"
    
    show s_mangap zorder 2
    s " Iya… ini adalah pedang kuno yang telah disucikan oleh air suci"
    s "jika kamu butuh sesuatu silakan gunakan air ini sebelum melawan malapetaka di kastil merah"
    hide s_mangap

    hide mc_baju_bingung
    show mc_baju_senang zorder 2
    mc "Terima kasih, Yang Mulia"
    hide mc_baju_senang

    show mc_berpikir zorder 2
    mc "(heumm keknya aku bisa buat sesuatu pakai air suci ini)"
    hide mc_berpikir

    call molotov_scene

    show molotov zorder 2
    pause 0.5

    show d_senyum zorder 2
    d "Sudah waktunya kita berangkat~ si kucing sudah membobol keamanan kastil merah"
    
=======
    show mc_baju_bingung zorder 2
    mc "Pedang ini..Apakah ini bisa mengalahkan malapetaka itu?"
    
    show s_mangap zorder 2
    s " Iya… ini adalah pedang kuno yang telah disucikan oleh air suci"
    s "jika kamu butuh sesuatu silakan gunakan air ini sebelum melawan malapetaka di kastil merah"
    hide s_mangap

    hide mc_baju_bingung
    show mc_baju_senang zorder 2
    mc "Terima kasih, Yang Mulia"
    hide mc_baju_senang

    show mc_berpikir zorder 2
    mc "(heumm keknya aku bisa buat sesuatu pakai air suci ini)"
    hide mc_berpikir

    call molotov_scene
    $add_mc_hp(7)

    show molotov zorder 2
    pause 0.5

    show d_senyum zorder 2
    d "Sudah waktunya kita berangkat~ si kucing sudah membobol keamanan kastil merah"
    
>>>>>>> a05a961d6961a4f940f3c4c34efb966269094c9f
    show mc_baju_kaget zorder 2
    mc "Ehh kucing..? heum oke deh"
    d "btw nanti disana kamu sendiri ya~ aku kan buronan raja"
    d "(tertawa)"
<<<<<<< HEAD

=======
    call play_jalan_puzzle("act_7")
    $add_mc_hp(7)
>>>>>>> a05a961d6961a4f940f3c4c34efb966269094c9f
    jump act_7


    return