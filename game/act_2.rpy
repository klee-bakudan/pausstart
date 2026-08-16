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

    show mc_kaget at vpunch zorder 2:
        xalign 0.99


    "/menyenggol meja"
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

    scene white
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

    mc "alamak"

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

    mc "Hah……..eennggg"
    

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

    l "AKHIRNYA! Kamulah penyelamat kami! Kamu adalah orang dari dunia luar yang selama ini tertulis di dalam gulungan takdir! blablabla…."

    hide mc_datar
    hide l_bling

    show mc_bingung zorder 2:
        xalign 0.99

    show l_datar zorder 2:
        xalign 0.02
        yanchor 1.0
        ypos 920

    mc "Ha.. apaan sih?? Penyelamat??"

    hide mc_bingung
    hide l_datar

    show l_bling zorder 2:
        xalign 0.002
        yanchor 0.94
        ypos 920

    show mc_datar zorder 2:
        xalign 0.99

    l "Eehh.. Sini ikut aku, kamu pasti kebingungan"
    with dissolve

    hide mc_datar
    hide l_bling

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
    

    show a_datarcrop zorder 2
    a "Ah… maaf kelancangan ku, namaku Absolum."

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4

    show a_datarcrop at vpunch zorder 2:
        xalign 0.5
    a "Aku dahulu adalah seorang tabib kerajaan… Yaa.. sudah lama sekali"

    hide a_datarcrop

    show gulungan at item_popup zorder 2
    pause 3.0
    hide gulungan

    show a_datarcrop zorder 2
    a "Biar aku jelaskan secara singkat apa yang terjadi di dunia ini…"

    show a_datarcrop at vpunch zorder 2:
        xalign 0.5
    a "Dahulu, seluruh wilayah di bawah naungan kerajaan dalam keadaan makmur dan jaya."

    show a_datarcrop at vpunch zorder 2:
        xalign 0.5
    a "Namun, semenjak kenaikan tahta raja yang baru, segalanya berubah drastis."

    show a_datarcrop at vpunch zorder 2:
        xalign 0.5
    a "Wilayah yang jauh dari perkotaan tidak mendapatkan akses pangan maupun fasilitas yang layak."

    show a_datarcrop zorder 2:
        xalign 0.002
    with ease

    show l_takut zorder 2:
        xalign 0.99
        yanchor 0.87
        ypos 920

    l "dan yang terburuk, rakyat kecil ngga bisa melakukan ngapa-ngapain" 
    l "setiap keluh kesah yang mereka sampaikan dibiarin gitu aja.."

    hide a_datarcrop
    hide l_takut

    show mc_bingung zorder 2:
        xalign 0.99

    mc "{color=#7e6d2f}(lohh.. kok kayak demo tadi ya..){/color}"

    hide mc_bingung

    show mc_hah at vpunch zorder 2:
        xalign 0.99

    mc "Ga mungkin! aku baru aja nyampe di sini, itu pasti cuman dongeng doang!"
    show mc_datar zorder 2:
        xalign 0.99

    mc "Ga mungkin! aku baru aja nyampe di sini, itu pasti cuman dongeng doang!"
    hide mc_hah


    show mc_datar zorder 2:
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

    

#     # MINIGAME DEBAT ADMIN MALAS
#     label minigame2:
#         scene jamur
#         show black onlayer master zorder 1 as darkoverlay:
#             alpha 0.5
#         show mc_berpikir zorder 2 

#         $choice_positions = [(50, 50), (100, 50), (200, 50)]
#         $choice_texts = ["gimana kalau aku emang bukan penyelamat?",
#         "buktinya..ini aja?", "kalau aku menang aku bisa pulang kan?"]

#         call screen bubble_choice(choice_texts)
#         $hasil = _return
#         pause 3

#         if hasil == 0:
#             jump pilihan1
#         elif hasil ==  1:
#             jump pilihan2
#         elif hasil == 2:
#             jump pilihan3
    
#     label pilihan1:
#         scene jamur
#         show black onlayer master zorder 1 as darkoverlay:
#             alpha 0.5
#         show mc_garuk zorder 2
#         mc "Tapi gimana kalau aku sebenarnya bukan penyelamat yang kalian cari dan malah mati dijalan?"
#         show l_takut zorder 2
#         l "K-kamu gak akan mati kok di tengah jalan.. I-iyakan absolum??"
#         hide mc_garuk
#         hide l_takut
#         show a_datar zorder 2
#         a "..."
#         show l_takut zorder 2
#         l "KOK DIEM SIH JADI PANIK NIH!!"
#     jump act2_lanjut
    
#     label pilihan2:
#         scene jamur
#         show black onlayer master zorder 1 as darkoverlay:
#             alpha 0.5
#         show mc_bingung zorder 2
#         mc "Emang ada bukti selain gulungan takdir itu?"
#         show a_senyum zorder 2
#         a "Tentu saja ada! Buktinya kamu telah memakan klepon yang ada di dalam ruangan itu kan?"
#         hide mc_bingung
#         show mc_kaget zorder 2
#         mc "eh.. Ho’oh lah, emang ada hubungannya?"
#         a "Jikalau kamu tidak mengikuti kelinci dan makan klepon tadi, kamu tidak akan bisa masuk ke dunia ini"
#         a "(tertawa kecil)"
#         a "Asam di gunung, garam di laut, bertemu dalam satu belanga. Takdir hanya memanggil orang yang ditujunya."
#         hide mc_kaget
#         show l_bling zorder 2
#         l "Wow sangat puitis"
#         hide l_bling
#         a "Jika kamu bukan orang yang dituju dunia ini tidak akan memasukkan kamu Nak"
#         show mc_datar zorder 2
#         pause 1.0
#         hide mc_datar
#     jump act2_lanjut
   
#     label pilihan3:
#         scene jamur
#         show black onlayer master zorder 1 as darkoverlay:
#             alpha 0.5
#         show mc_huft zorder 2
#         mc "Ada satu hal yang ingin kutanyakan."
#         mc "Kalau aku berhasil menyelamatkan dunia ini, aku bisa keluar dari sini dan kembali ke duniaku kan?"
#         show a_senyum zorder 2
#         a "Jangan khawatir, Nak. Untuk kepulanganmu sudah pasti akan terjadi di saat mala petaka di dunia ini berakhir,"
#         a "pintu dunia ini akan terbuka dan membawamu pulang"
#         hide a_senyum
#         show l_datar zorder 2
#         l "T-tuhkan absolum sudah menjamin kepulanganmu!"
#         l "Tidak perlu takut, MC!"
#         l "A-aku akan membantumu menghadapi mala petaka ini… tapi jangan terlalu gegabah… ya?"
#         mc "(menghela nafas)"
#         mc "Yaudah deh mohon bantuannya kalau gitu.. akan aku pegang perkataan kalian berdua!"
#     jump act2_lanjut 
    
# label act2_lanjut:
#     scene jamur
#     show black onlayer master zorder 1 as darkoverlay:
#         alpha 0.5
#     hide mc_garuk

#     show a_datar zorder 2
#     a "mc kamu mungkin bisa memilih jalur yang berbeda dari gulungan takdir ini.."
#     a "Namun, apa pun yang terjadi.. Akhir tersebut akan tetap terjadi"
#     show mc_datar zorder 2
#     mc "...Baiklah.."

    # call play_jalan_puzzle("act_3")
        
    jump act_3