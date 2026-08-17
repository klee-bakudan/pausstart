label act_3:
    scene act3
    pause 0.5

    scene jamur asap with Fade(0.8, 0.2, 0.8)

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.4 alpha 0.5
    with dissolve

    transform popup:
        xalign 0.2
        yanchor 0.82
        ypos 910
        block:
            linear .05 yoffset 10
            linear .05 yoffset -5
            linear .05 yoffset 3
            linear .05 yoffset 0
            repeat False
    show a_datar at popup zorder 2

    pause 0.5

    hide a_datar
    
    transform popup_left:
        xalign 0.99
        block:
            linear .05 yoffset 10
            linear .05 yoffset -5
            linear .05 yoffset 3
            linear .05 yoffset 0
            repeat False

    show mc_hah at popup_left zorder 2
    pause 0.5

    transform popup_right:
        xalign 0.01
        yanchor 0.82
        ypos 910
        block:
            linear .05 yoffset 10
            linear .05 yoffset -5
            linear .05 yoffset 3
            linear .05 yoffset 0
            repeat False
    show l_takut at popup_right zorder 2
    pause 0.5

    hide l_takut
    hide mc_hah

    show a_datar zorder 2:
        xalign 0.2
    a "Sepertinya mereka sudah mulai bergerak.."

    show a_datar zorder 2:
        xanchor 0.0
        xalign 0.02
        xoffset -500
    with ease

    show l_takut zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920
    l "eee b-bagaimana ini minna-san!? Kita sudah ketahuan oleh antek-antek Ratu Merah"
    
    hide a_datar with dissolve

    show l_takut zorder 2:
        xalign 0.09
        xanchor 0.0
        xoffset -150
    with ease

    show mc_hah zorder 2:
        xalign 0.99
    mc "Sekarang banget nih...trus kita harus gimana??"
    hide mc_hah
    hide l_takut

    show a_datar zorder 2 with dissolve:
        xalign 0.2
    a "Pergilah ke area hutan yang terbakar."
    a "Sang Perajin Gaun seharusnya berada di sana untuk membantumu."
    hide a_datar with dissolve

    show l_takut zorder 2 with dissolve
    l "A-aku akan coba bantu kamu ke sana, Ayo!"
    hide l_takut
    pause 0.5

    transform fadeout:
        linear 0.3 alpha 0.0
    hide a_datar at fadeout

    scene jamur3
    with dissolve

    scene jamurkb
    pause 0.5

    show j_bayang 
    pause 0.5
    hide j_bayang

    show j_datar at vpunch zorder 2:
        xalign 0.5

    j "mc jangan sembunyi~~~"
    # font
    j "CARI SAMPAI KETEMU" with vpunch
    hide j_datar
    show pasukan
    j "HIDUP ATAU MATI HARUS KITA BAWAKAN KE BAGINDA RAJA" with vpunch
    pause 0.5

    hide pasukan

    # minigame lari

    scene jamur_tengah

    show mc_takut zorder 2:
        xanchor 0.85
        xpos 0.99
        yalign 0.25
    $ renpy.pause(0.2, hard=True)

    mc "hufft hufft… Lucien kemana dah... Cepet amat larinya"
    mc "gimanasih katanya bakal bantu heungg.."
    hide mc_takut
    show maung at vpunch zorder 2
    "GRAAAAAA" 
    "(menyakar mc)" with vpunch
    hide maung
    show maung_2 zorder 2:
        xanchor 0.02
    show mc_terluka zorder 2:
        xanchor 0.89
        xpos 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "Ha!?? SIAL GUE HARUS KABUR" with vpunch

    call play_jalan_puzzle("act_4")
    jump act_4



