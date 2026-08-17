default choice_positions = [(50, 150), (1150, 50), (850, 400)]
# ini def letak awan

label act_2:
    scene hitam


    play sound "audio/transition-act.mp3"
    pause 1.0

    scene act2 
    with dissolve

    pause 3.0
    stop sound

    scene ruangs
    with Fade(0.8, 0.2, 0.8)

    pause 1.0

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4
    
    show mc_garuk zorder 2:
        xanchor 0.89
        xpos 0.94
        yalign 0.25

    mc "awh kepalaku"

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4

    hide mc_garuk
    # transisi yeah 

    show mc_bingung zorder 2:
        xalign 0.99

    mc "ini...tempat apa...kok kecil banget"

    hide mc_bingung

    show mc_kaget zorder 2:
        xalign 0.99


    "/menyenggol meja" with vpunch
    #sfx plis
    hide mc_bingung
    hide mc_kaget
    hide darkoverlay


    window hide

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4

    show klepon at item_popup zorder 2

    pause 2.0


    hide klepon
    hide darkoverlay

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4

    show mc_ngiler zorder 2:
        xalign 0.99

    mc "Ih klepon. Belom lima menit nih"
    hide mc_ngiler

    show mc_makan zorder 2:
        xalign 0.99

    mc "nyom nyommm"
    mc "Kok ada rasa kek- ya.. Adalah pokoknya"

    hide mc_makan

    show mc_kaget at glitch_flicker zorder 2:
        xalign 0.99

    mc "EEEEHHH"

    window hide
    hide mc_kaget

    scene putih
    with Dissolve(0.25)

    scene ruangb
    with Dissolve(0.5)

    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show mc_bingung zorder 2:
        xalign 0.99

    $ renpy.pause(0.2, hard=True)

    mc "alamak kok jadi kecil gini.."

    hide darkoverlay
    with dissolve

    scene ruangb_buka
    pause 1.0

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5

    show l_datar zorder 2:
        xalign 0.99
        yanchor 1.0
        ypos 920

    l "Sini-sini ikut aku"

    pause 0.5

    show mc_kaget zorder 2:
        xalign 0.99

    show l_datar:
        xalign 0.02
        yanchor 1.0
        ypos 920
    with ease
    #transisi bos

    mc "Hah…… Kok ada manusia hewan??"
    

    hide l_datar 
    hide mc_kaget
    with dissolve

    scene terowongan
    pause 1.0

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5

    show l_datar zorder 2:
        xalign 0.99
        yanchor 1.0
        ypos 920

    l "pelan-pelan aja nanti kepentok"
    pause 0.5

    show mc_garuk zorder 2:
        xanchor 0.89
        xpos 0.94
        yalign 0.25

    show l_datar:
        xalign 0.02
        yanchor 1.0
        ypos 920
    with ease


    mc "mm- okey.."

    hide l_datar 
    hide mc_kaget
    with dissolve

    scene jamur with fade
    pause 1.0
    
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show l_datar zorder 2:
        xalign 0.99
        yanchor 1.0
        ypos 920

    l "kamu mc kan?"

    hide l_datar

    show mc_kaget zorder 2:
        xalign 0.99

    show l_datar zorder 2:
        xalign 0.02
        yanchor 1.0
        ypos 920
    with ease

    mc "kok….tau namaku? ANTEK ANTEK ASING YA??"

    hide l_datar
    hide mc_kaget

    show l_bling zorder 2:
        xalign 0.002
        yanchor 0.94
        ypos 920
    
    show mc_datar zorder 2:
        xalign 0.99

    l "AKHIRNYA! Kamulah penyelamat kami! Kamu adalah orang dari dunia luar yang selama ini tertulis di dalam gulungan takdir! Sangat tidak disangka..."

    hide mc_datar

    show mc_bingung zorder 2:
        xalign 0.99

    show l_bling zorder 2:
        xalign 0.002
        yanchor 0.94
        ypos 920

    mc "Ha.. apaan sih?? Penyelamat??"
    hide l_bling

    hide mc_bingung
    hide l_datar

    show l_datar zorder 2:
        xalign 0.02
        yanchor 1.0
        ypos 920

    show mc_datar zorder 2:
        xalign 0.99

    l "Eehh.. Sini ikut aku, kamu pasti kebingungan"
    with dissolve

    hide mc_datar
    hide l_datar

    scene jamur asap with Fade(0.8, 0.2, 0.8)

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.4 alpha 0.5
    with dissolve

    show a_bayang zorder 2
    pause 1.0
    hide a_bayang

    show a_bayang zorder 2

    a "Kamu membawa siapa kali ini, wahai kelinci kecil?"

    show l_bling zorder 2:
        xalign 0.02
        yanchor 0.94
        ypos 920

    l "Wahai absolum yang bijaksana, inilah mc yang kita cari-cari"

    hide l_bling
    hide a_bayang

    window hide
    with dissolve

    # closeup
    show mc_full at topbottom zorder 2
    pause 3.5
    hide mc_full

    show a_bayangcrop zorder 2
    a "Sepertinya memang sudah takdirmu untuk datang ke sini…"

    show mc_bingung zorder 2:
        xalign 0.99

    mc "hah..Maksudnya?"

    hide mc_bingung

    show a_bayangcrop zorder 2:
        xalign 2.7
        yanchor 0.82
        ypos 910
    with ease

    pause 0.5

    hide a_bayangcrop

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4
    
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
    a "Ah… maaf kelancangan ku, namaku Absolum."

    show a_datar zorder 2:
        xalign 0.2
    a "Aku dahulu adalah seorang tabib kerajaan… Yaa.. sudah lama sekali"

    hide a_datar

    show gulungan at item_popup zorder 2
    pause 3.0
    hide gulungan

    show a_datar at popup zorder 2
    a "Biar aku jelaskan secara singkat apa yang terjadi di dunia ini…"

    show a_datar zorder 2:
        xalign 0.2
    a "Dahulu, seluruh wilayah di bawah naungan kerajaan dalam keadaan makmur dan jaya."

    show a_datar zorder 2:
        xalign 0.2
    a "Namun, semenjak kenaikan tahta raja yang baru, segalanya berubah drastis."

    show a_datar zorder 2:
        xalign 0.2
    a "Wilayah yang jauh dari perkotaan tidak mendapatkan akses pangan maupun fasilitas yang layak."

    hide a_datar

    show a_datar zorder 2:
        xanchor 0.0
        xalign 0.02
        xoffset -500
    with ease

    show l_takut zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920

    l "dan yang terburuk, rakyat kecil ngga bisa melakukan ngapa-ngapain" 
    l "setiap keluh kesah yang mereka sampaikan dibiarin gitu aja.."

    hide a_datar
    hide l_takut

    show mc_bingung zorder 2:
        xalign 0.99

    mc "{color=#7e6d2f}(lohh.. kok kayak demo tadi ya..){/color}"

    hide mc_bingung

    show mc_hah at vpunch zorder 2:
        xalign 0.99
    mc "Ga mungkin! aku baru aja nyampe di sini, itu pasti cuman dongeng doang!"
    hide mc_hah

    show mc_datar zorder 2:
        xalign 0.99
    mc "Ga mungkin! aku baru aja nyampe di sini, itu pasti cuman dongeng doang!"
    hide mc_hah


    show mc_datar zorder 3:
        xalign 0.089
    with ease

    show a_datarcrop zorder 2:
        xalign 0.89

    a "Gulungan takdir tidak pernah salah, Nak. Semua ini sudah tertulis sejak ratusan tahun."
    
    hide mc_datar

    show a_datarcrop zorder 2:
        xalign 0.089
    with ease

    show l_takut zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920

    l "A-Absolum benar kok! Gulungan takdir tidak mungkin berkehendak lain"
    hide l_takut

    show a_datarcrop zorder 2:
        xalign 0.50
    with ease

    a "Jalan yang kamu hadapi kemungkinan tidak akan mulus, tetapi percayalah bahwa kamu dapat menjalani itu semua, Nak."

    hide a_datarcrop

    show mc_garuk zorder 2:
        xanchor 0.89
        xpos 0.94
        yalign 0.25
        
    mc "(Hah… apaan sih,, ga jelas banget dah, niat buat sembunyi di gotong lah malah masuk universe lain…)"
    
    hide mc_garuk

    show mc_bingung at vpunch zorder 2:
        xalign 0.99
    mc "(Ratu merah..? Ratu putih? Apaan sih ini dikira bawang putih bawang merah kali??)"

    hide mc_bingung

    show mc_huft at vpunch zorder 2:
        xalign 0.99
    mc "(Aku? Beneran jadi pahlawan nih..? Yaelah plis lahh magang aja belom kelar malah disuruh jadi super hero"
    
    hide mc_huft

    show mc_berpikir at vpunch zorder 2:
        xalign 0.99

    mc "(keknya aku harus ngomong deh)"


    mc "(keknya aku harus ngomong deh)"

    # MINIGAME DEBAT ADMIN MALAS
    label minigame2:
        scene jamur
        with dissolve

        show black onlayer master zorder 1 as darkoverlay:
            alpha 0.0
            linear 0.3 alpha 0.5

        show mc_berpikir zorder 2:
            xalign 0.99

        $ renpy.pause(0.2, hard=True)

    $ choice_positions = [
    (-80, 20),
    (1000, 20),
    (800, 350)
    ]

    $ choice_texts = [
        "gimana kalau aku emang bukan penyelamat?",
        "buktinya..ini aja?",
        "kalau aku menang aku bisa pulang kan?"
    ]

    call screen bubble_choice(choice_texts)

    $ hasil = _return

    window show

    hide mc_berpikir
    hide darkoverlay

    if hasil == 0:
        jump act2_pilihan1
    elif hasil == 1:
        jump act2_pilihan2
    elif hasil == 2:
        jump act2_pilihan3


label act2_pilihan1:

    scene jamur
    with dissolve

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    # MC kanan
    show mc_garuk zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "Tapi gimana kalau aku sebenarnya bukan penyelamat yang kalian cari dan malah mati dijalan?"

    hide mc_garuk

    # Lucien kiri
    show l_takut zorder 2:
        xalign 0.02
        yanchor 0.87
        ypos 920

    $ renpy.pause(0.2, hard=True)

    l "K-kamu gak akan mati kok di tengah jalan.. I-iyakan absolum??"

    hide l_takut

    # Absolum kiri / tengah-kiri
    show a_datar zorder 2:
        xalign 0.20
        yanchor 0.82
        ypos 910

    $ renpy.pause(0.2, hard=True)

    a "..."

    hide a_datar

    # Lucien lagi
    show l_takut at vpunch zorder 2:
        xalign 0.02
        yanchor 0.87
        ypos 920

    $ renpy.pause(0.2, hard=True)

    l "KOK DIEM SIH JADI PANIK NIH!!"

    hide l_takut
    hide darkoverlay
    

    jump act2_lanjut


# =========================
# PILIHAN 2
# =========================

label act2_pilihan2:

    scene jamur
    with dissolve

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    # MC kanan
    show mc_bingung zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "Emang ada bukti selain gulungan takdir itu?"

    hide mc_bingung

    # Absolum kiri
    show a_senyum zorder 2:
        xalign 0.20
        yanchor 0.82
        ypos 910

    $ renpy.pause(0.2, hard=True)

    a "Tentu saja ada! Buktinya kamu telah memakan klepon yang ada di dalam ruangan itu kan?"

    # MC kanan
    show mc_kaget at vpunch zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "eh.. Ho'oh lah, emang ada hubungannya?"

    a "Jikalau kamu tidak mengikuti kelinci dan makan klepon tadi, kamu tidak akan bisa masuk ke dunia ini"

    a "(tertawa kecil)"

    a "Asam di gunung, garam di laut, bertemu dalam satu belanga. Takdir hanya memanggil orang yang ditujunya."

    hide mc_kaget
    hide a_senyum

    # Lucien kiri
    show l_bling at vpunch zorder 2:
        xalign 0.02
        yanchor 0.94
        ypos 920

    $ renpy.pause(0.2, hard=True)

    l "Wow sangat puitis"

    hide l_bling

    # Absolum balik
    show a_senyum zorder 2:
        xalign 0.20
        yanchor 0.82
        ypos 910

    $ renpy.pause(0.2, hard=True)

    a "Jika kamu bukan orang yang dituju dunia ini tidak akan memasukkan kamu Nak"

    hide a_senyum

    # MC kanan
    show mc_datar zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(1.0, hard=True)

    hide mc_datar
    hide darkoverlay

    jump act2_lanjut


label act2_pilihan3:

    scene jamur
    with dissolve

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    # MC kanan
    show mc_huft zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "Ada satu hal yang ingin kutanyakan."

    mc "Kalau aku berhasil menyelamatkan dunia ini, aku bisa keluar dari sini dan kembali ke duniaku kan?"

    hide mc_huft

    # Absolum kiri
    show a_senyum zorder 2:
        xalign 0.20
        yanchor 0.82
        ypos 910

    $ renpy.pause(0.2, hard=True)

    a "Jangan khawatir, Nak. Untuk kepulanganmu sudah pasti akan terjadi di saat mala petaka di dunia ini berakhir,"

    a "pintu dunia ini akan terbuka dan membawamu pulang"

    hide a_senyum

    # Lucien kiri
    show l_datar zorder 2:
        xalign 0.02
        yanchor 1.0
        ypos 920

    $ renpy.pause(0.2, hard=True)

    l "T-tuhkan absolum sudah menjamin kepulanganmu!"

    l "Tidak perlu takut, MC!"

    l "A-aku akan membantumu menghadapi mala petaka ini… tapi jangan terlalu gegabah… ya?"

    # MC kanan
    show mc_datar zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "(menghela nafas)"

    mc "Yaudah deh mohon bantuannya kalau gitu.. akan aku pegang perkataan kalian berdua!"

    hide mc_datar
    hide l_datar
    hide darkoverlay

    jump act2_lanjut


label act2_lanjut:

    scene jamur
    with dissolve

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.5

    show a_datar zorder 2:
        xalign 0.20
        yanchor 0.82
        ypos 910

    a "mc kamu mungkin bisa memilih jalur yang berbeda dari gulungan takdir ini.."

    a "Namun, apa pun yang terjadi.. Akhir tersebut akan tetap terjadi"

    hide a_datar

    show mc_datar zorder 2:
        xalign 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "...Baiklah.."

    hide mc_datar
    hide darkoverlay
    window hide

    call play_jalan_puzzle("act_3")
    $add_mc_hp(7)

    jump act_3