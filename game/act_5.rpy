init python:
    renpy.music.register_channel("walking", "sfx", loop=False)

transform expression_pop:
    yoffset 0

    easeout 0.15 yoffset -35
    easein 0.12 yoffset 0
    easeout 0.10 yoffset -15
    easein 0.10 yoffset 0

label act_5:
    play sound "audio/transition-act.mp3"
    pause 1.0

    scene act5
    with dissolve
    
    pause 6.0
    stop sound

    scene butut
    with dissolve
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show mc_hah zorder 2:
        xalign 0.99
        yalign 0.25

    mc "hah...sudah berapa lama rumah ini ditelantarkan"

    hide mc_hah
    hide darkoverlay
    window hide

    scene butut2
    with dissolve
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show mc_tch zorder 2:
        xalign 0.99
        yalign 0.25

    mc "kerajaan ga becus, udah kacau gini aja masih tutup mata"

    hide mc_tch
    hide darkoverlay
    window hide 

    scene tea_party
    with dissolve
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show d_datar-fix zorder 2:
        xalign 1.1
        yalign 0.25

    d "Uweaaa, lihat siapa yang dibawa kelinci imut kali ini~"
    hide d_datar-fix

    show d_senyum-fix at expression_pop zorder 2:
        xalign 1.1
        yalign 0.25

    d "Kelinci nackal~ kalau lagi kencan ga perlu pamer sana sini juga kali~"
    hide d_senyum-fix

    show d_datar-fix:
        xalign -0.05
        yalign 0.25
    with ease

    show l_datar zorder 2:
        xalign 0.99
        yanchor 1.0
        ypos 920

    l "I-imut? Apasih!! Ini si [mcname] loh yang ada di gulungan takdir itu"

    hide d_datar-fix
    

    show d_senyum-fix at expression_pop zorder 2:
        xalign -0.05
        yalign 0.25

    d "owhhhh ternyata kamyu~"
    d "selamat datang [mcname] di wonderland~ maaf ya kalo berdebu"
    d "habis bakar-bakar kecil soalnya HAHAHAHA~"
    
    hide l_datar

    show h_senyum-fix at expression_pop zorder 2:
        xalign 1.0
        yalign 0.25

    h "BAWAHAHAHA bakar-bakar kecil katanya!"
   
    hide d_senyum-fix
    hide h_senyum-fix

    show h_mingkem-fix:
        xalign -0.05
        yalign 0.25
    with ease

    show ar_jengkel at expression_pop zorder 2:
        xalign 1.0
        yalign 0.25

    ar "Aduhh keluar lagi dah tuh jokes garing"
    hide h_mingkem-fix
    hide ar_jengkel

    show ar_normal:
        xalign -1
        yalign 0.25
    with ease

    hide h_senyum-fix
    show d_senyum-fix at expression_pop zorder 2:
        xalign 1.1
        yalign 0.25

    d "HAHA~ pasti capek kan dijalan, ayok sini kita minum teh dulu sudah waktunya minum teh~"
    hide d_senyum-fix
    hide ar_normal

    show h_mingkem-fix at expression_pop zorder 2:
        xalign 1.0
        yalign 0.25
    h "IH DORMMOUSE JANGAN AMBIL PISANG GORENG AKU"
    hide h_mingkem-fix
    show h_mingkem-fix:
        xalign -0.05
        yalign 0.25
    with ease

    show ar_jengkel at expression_pop zorder 2:
        xalign 0.99
        yalign 0.25
    ar "DIH! siapa juga yang mau ngambil"
    hide ar_jengkel
    hide h_mingkem-fix

    show mc_datar zorder 2:
        xalign 0.99
        yalign 0.25
    mc "Jadi.. aku mau bertanya tentang-"
    hide mc_datar

    play sound "audio/broken-glass.mp3"
    pause 3.0

    show d_kesel-fix at expression_pop zorder 2:
        xalign 0.99
        yalign 0.25
    d "WOI PEGANG PIRING YANG BENER!"
    hide d_kesel-fix

    show mc_tch zorder 2:
        xalign 0.99
        yalign 0.1

    mc "Aneh banget... Ini beneran orang yang bakal bantu aku..?"
    hide mc_tch

    show mc_beg zorder 2:
        xalign 0.99
        yalign 0.1
    mc "Lurcien bantu aku dong..."
    hide mc_beg

    show mc_kaget at expression_pop zorder 2:
        xalign 0.99
        yalign 0.1
    mc "lah LU NAPA SEMBUNYI KE BAWAH!?"
    hide mc_kaget

    show l_takut zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920
    l "E-eh maaf soalnya aku takut sama tikus itu.."
    hide l_takut

    show l_takut:
        xalign 0.1
        yanchor 0.87
        ypos 920
    with ease

    show mc_kaget at expression_pop zorder 2:
        xalign 0.99
        yalign 0.25
    mc "LAH ITU TIKUS?! Kok gede?"
    hide mc_kaget
    
    show mc_datar:
        xalign 0.99
        yalign 0.25
    with ease

    hide l_takut
    
    show l_takut zorder 2:
        xalign 0.1
        yanchor 0.87
        ypos 920
    l "Co-coba kamu pisahin mereka…"
    l "sekalian jauhin dari aku peliss"
    hide l_takut

    
    window hide

    jump act5_minigame5

default choice_positions = []

# MINIGAME - TEA PARTY
label act5_minigame5:

    scene tea_party
    with dissolve

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show mc_berpikir at vpunch zorder 2:
        xalign 0.5
        yalign 0.19

    $ renpy.pause(0.2, hard=True)

    $ renpy.music.set_volume(1.0, channel="music")
    $ renpy.music.play("audio/debat-bg.mp3", channel="music", loop=True)

    $ choice_positions = [(50, 150), (1000, 100), (500, 650)]

    $ choice_texts = [
        "lumayan nih, pisgor enak nih sama teh",
        "pergi aja kali ya..?",
        "haduh bisa serius ga sih!"
    ]

    call screen bubble_choice(choice_texts)
    $ hasil = _return

    window show

    hide mc_berpikir
    hide darkoverlay

    if hasil == 0:
        $ add_mc_hp(3)
        jump act5_pilihan1
    elif hasil == 1:
        $ add_mc_hp(3)
        jump act5_pilihan2
    elif hasil == 2:
        $ add_mc_hp(6)
        jump act5_pilihan3

label act5_pilihan1:

    scene meja_tea
    with dissolve

    pause 0.1

    show mc_ngiler zorder 2:
        xalign 0.99
        yalign 0.1

    $ renpy.pause(0.2, hard=True)

    mc "{color=#7e6d2f}(Eh… keknya jangan makan dulu deh){/color}"

    hide mc_ngiler
    window hide

    jump act5_lanjut


label act5_pilihan2:

    scene meja_tea
    with dissolve

    show mc_tch zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "Ini beneran kita minum teh padahal diluar lagi kacau balau??"
    mc "Kalau ga mau diskusi, aku pergi aja"

    hide mc_tch

    show h_senyum-fix at expression_pop zorder 2:
        xalign 1.0
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    h "Bye-bye~"

    hide h_senyum-fix

    show mc_kaget at vpunch zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "{color=#7e6d2f}(eh.. Bener juga sih kalau aku pergi tanpa tujuan nanti ketangkep){/color}"


    hide mc_kaget
    window hide

    jump act5_lanjut


label act5_pilihan3:

    scene meja_tea
    with dissolve

    show mc_tch at vpunch zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "WOI! INI KALIAN BENARAN MAU MENGHADAPI MALA PETAKA!?"
    mc "Aku datang ke dunia ini BUKAN buat minum teh!"
    mc "tapi menghadapi mala petaka sialan yang harus aku selesaikan DEMI KALIAN"

    hide mc_tch
    window hide

    jump act5_minigame6


label act5_lanjut:
    scene tea_party
    pause 0.3
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show d_datar-fix zorder 2:
        xalign 1.1
        yalign 0.25
    d "Okayy sepertinya pahlawan tidak memiliki jadwal untuk minum teh.."
    d "Ya..seperti yang terlihat wilayah ini udah kebakar habis.."
    hide d_datar-fix

    show d_senyum-fix at expression_pop zorder 2:
        xalign 1.1
        yalign 0.25

    d "cuman sisa meja ini doang sih dan rumah si arden yang sekarang ada di tanah tuh~"

    hide d_senyum-fix

    show d_datar-fix:
        xalign -0.05
        yalign 0.25
    with ease

    show ar_jengkel zorder 2:
        xalign 1.0
        yalign 0.25
    ar "NAMANYA JUGA BUNKER"
    hide d_datar-fix
    hide ar_jengkel
    show ar_normal:
        xalign -1
        yalign 0.25
    with ease

    show h_senyum-fix zorder 2:
        xalign 1.0
        yalign 0.25

    h "hehe rumah aku kebakar sih"
    h "(tertawa)"
    h "Semuanya! semua-muanyaaa terbakar… TERBAKARR"
    
    hide h_senyum-fix

    show h_mingkem-fix:
        xalign 1.0
        yalign 0.25
    with ease

    hide ar_normal

    show ar_jengkel zorder 2:
        xanchor 0.35
        xpos 150
        yalign 0.25

    ar "Aduhh kumat lagi tuh gilanya"
    
    hide ar_jengkel
    hide h_mingkem-fix

    show ar_normal-fix zorder 2:
        xanchor 0.35
        xpos 150
        yalign 0.25
    ar "mangkanya"
    hide ar_normal-fix 

    show ar_normal-fix:
        xanchor 0.35
        xpos 150
        yalign 0.25
    with ease

    show mc_bingung at expression_pop zorder 2:
        xalign 0.99
        yalign 0.1
    mc "mangkanya apa?"
    hide mc_bingung    

    show mc_datar:
        xalign 0.99
        yalign 0.1
    with ease

    hide ar_normal-fix
    show ar_senyum zorder 2:
        xanchor 0.35
        xpos 150
        yalign 0.25

    ar "There is no place for us here, [mcname]"
    hide mc_datar
    hide ar_senyum


    show d_datar-fix zorder 2:
        xalign 1.1
        yalign 0.25
    d "jadi gimana nih~ sang penyelamat"
    hide d_datar-fix 

    show d_senyum-fix at expression_pop zorder 2:
        xalign 1.1
        yalign 0.25
    d "decision~ desicion~"

    hide d_senyum-fix

    window hide

    jump act5_minigame6

# MINIGAME - KEPUTUSAN AKHIR
label act5_minigame6:

    scene tea_party
    with dissolve

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show mc_berpikir at vpunch zorder 2:
        xalign 0.5
        yalign 0.19

    $ renpy.pause(0.2, hard=True)

    window hide

    $ choice_positions = [
        (20, 100),
        (900, 120),
        (500, 580)
    ]

    $ choice_texts = [
        "aku harus menyelesaikan takdir ini dan pulang",
        "ini di luar batasku. Aku nggak bisa mengubahnya",
        "ini nggak bisa dibiarkan. Aku harus melawan!"
    ]

    call screen bubble_choice(choice_texts)

    $ hasil = _return
    window hide
    hide mc_berpikir
    hide darkoverlay
    
    $ renpy.music.stop(channel="music", fadeout=1.0)

    if hasil == 0:
        $ add_mc_hp(1)
    elif hasil == 1:
        $ add_mc_hp(2)
    elif hasil == 2:
        $ add_mc_hp(5)

    jump act5_teko

label act5_teko:
    # sfx kuda 
    scene teaparty_asap 
    pause 1
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    play walking "audio/walking-sounds.mp3"
    play sound "audio/horse-neigh.mp3"
    
    show d_kesel-fix zorder 2:
        xalign 0.99
        yalign 0.25
    d "OH HELL NAWHHHHH THATS THE PRAJURIT"
    hide d_kesel-fix

    show d_senyum-fix zorder 2:
        xalign 0.85
        yalign 0.25
    d "kamu cepet makan ini truz langsung masuk ke teko yah"
    hide d_senyum-fix
    
    stop walking fadeout 3.0
    
    window hide

    show klepon at item_popup zorder 2
    pause 5
    hide klepon

    show mc_huft zorder 2:
        xalign 0.99
        yalign 0.1
    mc "apa lagi ini..pliss.."
    play sound "audio/menyusut.mp3"
    hide mc_huft

    show mc_datar at glitch_flicker zorder 2:
        xalign 0.99
        yalign 0.1
    "/mengecil"
    hide mc_datar

    show d_senyum-fix at expression_pop zorder 2:
        xalign 0.85
        yalign 0.25
    d "hoho~ mungilnya, cepat sembunyi kedalam teko ini"
    hide d_senyum-fix

    show teko at item_popup zorder 2
    pause 5
    hide teko

    scene dalam_teko
    pause 0.3
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show mc_melirik zorder 2 
    pause 0.5
    hide mc_melirik

    j "iyuh ketemu gelandangan ini lagi"
    "/menggema"
    scene teaparty_asap 
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show d_senyum-fix zorder 2:
        xalign 0.85
        yalign 0.25
    d "kamyu kok gitu sich~"
    d "ini namanya ngalcer~ katro ih"
    hide d_senyum-fix

    show d_datar-fix:
        xalign -0.05
        yalign 0.25
    with ease

    show j_mangap at expression_pop zorder 2:
        xalign 0.99
    j "WOI CEPET SERAHIN [mcname]"
    j "kamu tidak mau bernasib sama seperti ayam potong kan!"
    hide j_mangap
    hide d_datar-fix
    show j_siap at expression_pop zorder 2:
        xalign 0.99
    p "[mcname] sudah tidak ada di sini jendral"
    hide j_siap

    show d_kesel-fix zorder 2:
        xalign 0.85
        yalign 0.25
    d "ku bilang juga apa kau tidak percaya"
    hide d_kesel-fix
    show d_datar-fix:
        xalign -0.05
        yalign 0.25
    with ease
    
    show j_mangap at expression_pop zorder 2:
        xalign 0.99
    j "PRAJURIT GA GUNA!"
    j "BUANG-BUANG WAKTU AJA"
    j "AYO CEPAT PERGI!"
    hide j_mangap
    hide d_datar-fix

    pause 0.3
    scene dalam_teko
    pause 0.3
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    h "Hey, prajuritnya sudah pergi"
    h "keluar abistu makanlah ini"
    scene tea_party
    show klepon at item_popup zorder 2
    pause 2
    hide klepon

    play sound "audio/menyusut.mp3"

    pause 3.0

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show h_senyum-fix zorder 2:
        xalign 1.0
        yalign 0.25
    h "nih dari didit"
    hide h_senyum-fix
    call play_reassemble_puzzle ("Pieces/puzzle2") from _call_play_reassemble_puzzle_1

    show baju at item_popup zorder 2
    pause 1.5
    hide baju

    show d_datar-fix zorder 2:
        xalign 0.85
        yalign 0.25
    d "YA AMPUN AKU TIDAK LIHAT APA-APA SUERRR"
    d "e-eh udah kan ya"
    hide d_datar-fix

    show d_datar-fix:
        xalign -0.05
        yalign 0.25
    with ease

    show mc_baju_senang zorder 2:
        xalign 0.99
        yalign 0.1
    mc "aman bang"
    hide d_datar-fix

    show d_senyum-fix at expression_pop zorder 2:
        xalign -0.05
        yalign 0.25
    d "yaurrrr letsgo ke ratu putih~"
    hide d_senyum-fix
    hide mc_baju_senang

    show h_senyum-fix zorder 2:
        xalign 1.0
        yalign 0.25
    show ar_senyum zorder 2:
        xanchor 0.35
        xpos 150
        yalign 0.25
    "ati ati yee"
    hide h_senyum-fix
    hide ar_senyum

    show l_bling zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920
    l " s-semoga perjalanan kalian lancar"
    hide l_bling

    call play_jalan_puzzle("act_6") from _call_play_jalan_puzzle_3
    $add_mc_hp(7)
    jump act_6









