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

    mc "dasar pemerintah, kekacauan begini aja masih tutup mata"

    hide mc_tch
    hide darkoverlay
    window hide 

    scene tea_party
    with dissolve
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show d_datar zorder 2:
        xalign 1.1
        yalign 0.25

    d "Uweaaa, lihat siapa yang dibawa kelinci imut kali ini~"
    hide d_datar

    show d_senyum zorder 2:
        xalign 1.1
        yalign 0.25

    d "Kelinci nackal~, kalau lagi kencan ga perlu pamer sana sini juga kali~"

    hide d_senyum

    show l_datar zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920

    l "I-imut? Apasih!! Ini si MC loh yang ada di gulungan takdir itu"

    hide l_datar

    show d_senyum zorder 2:
        xalign 1.1
        yalign 0.25

    d "owhhhh ternyata kamyu~"
    d "selamat datang di wonderland~ maaf ya kalo berdebu"
    d "habis bakar-bakar kecil soalnya HAHAHAHA~"

    hide d_senyum

    show h_senyum zorder 2:
        xalign 1.0
        yalign 0.25

    h "BAWAHAHAHA bakar-bakar kecil katanya!"
    hide h_senyum

    show mc_bingung zorder 2:
        xalign 0.99
        yalign 0.25

    mc "Aneh banget... Ini beneran orang yang bakal bantu aku..?"
    hide mc_bingung

    show d_senyum zorder 2:
        xalign 1.1
        yalign 0.25

    d "HAHA~ pasti capek kan dijalan, ayok sini kita minum teh dulu sudah waktunya minum teh~"
    hide d_senyum

    show h_senyum zorder 2:
        xalign 1.0
        yalign 0.25
    h "IH DORMMOUSE JANGAN AMBIL PISANG GORENG AKU"
    hide h_senyum

    show mc_datar zorder 2:
        xalign 0.99
        yalign 0.25
    mc "Jadi.. aku mau bertanya tentang-"
    hide mc_datar

    show d_kesel zorder 2:
        xalign 1.1
        yalign 0.25
    d "dih sok ngeklaim lu"
    hide d_kesel

    show mc_datar zorder 2:
        xalign 0.99
        yalign 0.25
    mc "Lurcien bantu aku dong..."
    hide mc_datar

    show mc_kaget zorder 2:
        xalign 0.99
        yalign 0.25
    mc "lah LU NAPA SEMBUNYI KE BAWAH!?"
    hide mc_kaget

    show l_takut zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920
    l "E-eh maaf soalnya aku takut sama tikus itu.."
    hide l_takut

    show mc_kaget zorder 2:
        xalign 0.99
        yalign 0.25
    mc "LAH ITU TIKUS?! Kok gede?"
    hide mc_kaget

    show l_takut zorder 2:
        xalign 0.99
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
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "Eh… keknya jangan makan dulu deh"

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

    show h_mingkem zorder 2:
        xalign 1.0
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    h "Bye-bye~"

    hide h_mingkem

    show mc_kaget at vpunch zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "(eh.. Bener juga sih kalau aku pergi tanpa tujuan nanti ketangkep)"

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

    jump act5_lanjut


label act5_lanjut:
    scene tea_party
    pause 0.3
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show d_datar zorder 2:
        xalign 1.1
        yalign 0.25
    d "Okayy sepertinya pahlawan tidak memiliki jadwal untuk minum teh.."
    d "Ya..seperti yang terlihat wilayah ini udah kebakar habis.."
    hide d_datar

    show d_senyum zorder 2:
        xalign 1.1
        yalign 0.25

    d "cuman sisa meja ini doang sih dan rumah si arden yang sekarang ada di tanah tuh~"

    hide d_senyum

    show h_senyum zorder 2:
        xalign 1.0
        yalign 0.25

    h "hehe rumah aku kebakar sih"
    h "(tertawa)"
    h "Semuanya! semua-muanyaaa terbakar… TERBAKARR"
    hide h_senyum

    show ar_jengkel zorder 2:
        xalign 1.0
        yalign 0.25

    ar "Aduhh keluar lagi tuh joks garing"

    hide ar_jengkel

    show mc_bingung zorder 2:
        xalign 0.99
        yalign 0.25

    mc "Aneh banget... Ini beneran orang yang bakal bantu aku..?"
    
    hide mc_bingung
    show d_senyum zorder 2:
        xalign 1.1
        yalign 1.5

    d "HAHA~ pasti capek kan dijalan, ayok sini kita minum teh dulu sudah waktunya minum teh~"

    hide d_senyum

    show h_senyum zorder 2:
        xalign 1.0
        yalign 0.25

    h "IH DORMMOUSE JANGAN AMBIL PISANG GORENG AKU"
    hide h_senyum

    show mc_datar zorder 2:
        xalign 0.99
        yalign 0.25

    mc "Jadi.. aku mau bertanya tentang-"

    hide mc_datar

    show ar_jengkel zorder 2:
        xalign 1.0
        yalign 0.25

    ar "Oi lu ngapain sih kang topi kagak jelas main bantal kursi. ITU PUNYA GW!"

    hide ar_jengkel

    show d_kesel zorder 2:
        xalign 1.0
        yalign 0.25

    d "dih sok ngeklaim lu"

    hide d_kesel

    show mc_datar zorder 2:
        xalign 0.99

    mc "Lurcien bantu aku dong..."

    hide mc_datar

    show mc_kaget at vpunch zorder 2:
        xalign 0.99

    mc "lah LU NAPA SEMBUNYI KE BAWAH!?"
    
    hide mc_kaget
    
    show l_takut zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920

    l "E-eh maaf soalnya aku takut sama tikus itu.."
    
    hide l_takut

    show mc_kaget zorder 2:
        xalign 0.99

    mc "LAH ITU TIKUS?! Kok gede?"

    hide mc_kaget

    show l_takut zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920

    l "Co-coba kamu pisahin mereka…"
    l "sekalian jauhin dari aku peliss"

    hide l_takut
    hide darkoverlay

    show d_senyum zorder 2:
        xalign 1.1
        yalign 0.25

    d "decision~ desicion~"

    hide d_senyum

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
        (15, 100),
        (900, 120),
        (500, 580)
    ]

    $ choice_texts = [
        "aku harus nyelesaiin apa yang udah ditakdirkan biar bisa cepet pulang",
        "ini udah diluar batasku sepertinya aku ga bisa ngerubah apa-apa",
        "ini semua ga bisa dibiarin gitu aja, aku harus memperjuangkan keadilan!"
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

    jump act_6