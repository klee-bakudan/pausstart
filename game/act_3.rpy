label act_3:
    # scene act3
    # pause 0.5

    # scene jamurbesar
    # pause 1.0 
    # with dissolve
    # scene jamur3
    # show a_datar
    # pause 0.5
    # hide a_datar
    # show l_takut at slightleft
    # pause 0.5
    # show mc_hah at slightright
    # pause 0.5

    # hide l_takut
    # hide mc_hah

    # show a_datar
    # a "Sepertinya mereka sudah mulai bergerak.."
    # show l_takut
    # l "eee b-bagaimana ini minna-san!? Kita sudah ketahuan oleh antek-antek Ratu Merah"
    # hide l_takut
    # show l_takut at slightleft
    # hide a_datar
    # show mc_hah
    # mc "Sekarang banget nih...trus kita harus gimana??"
    # hide mc_hah
    # hide l_takut

    # show a_datar
    # a "Pergilah ke area hutan yang terbakar."
    # a "Sang Perajin Gaun seharusnya berada di sana untuk membantumu."
    # show l_takut
    # l "A-aku akan coba bantu kamu ke sana, Ayo!"
    # hide l_takut
    # pause 0.5
    # hide a_datar at fadeout

    # scene jamur3
    # with dissolve
    # scene jamurkb
    # pause 0.5
    # show j_bayang
    # pause 0.5
    # hide j_bayang
    # show j_datar
    # j "mc jangan sembunyi~~~"
    # # font
    # j "CARI SAMPAI KETEMU"
    # hide j_datar
    # show pasukan
    # j "HIDUP ATAU MATI HARUS KITA BAWAKAN KE BAGINDA RAJA"
    # hide pasukan

    # call escape_scene

#label act3_lanjut
    # scene jamur_tengah
    # show mc_takut
    # mc "hufft hufft… Lurcien kemana dah... Cepet amat larinya"
    # mc "gimanasih katanya bakal bantu heungg"
    # hide mc_takut
    # show maung
    # "GRAAAAAA"
    # "(menyakar mc)"
    # hide maung
    # show maung_2
    # show mc_terluka
    # mc "Ha!?? SIAL"

    # call play_jalan_puzzle("act_4")
    jump act_4



