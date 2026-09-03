define debat_kastil = [("apa maksudnya?", None),
("Heri jadi gila gegara rumah dan keluarganya terbakar", None), ("nyawa udah ga ada harganya", None),
("darah? muda?", "jadi ini tumbal darah biar muda"),
("Banyak kebakaran dan kerusakan", "itu disengaja"),
("monster itu ratu", "ratu meminum darah")]

label act_7:
    play sound "audio/transition-act.mp3"
    pause 1.0

    scene act7
    with dissolve
    
    pause 6.0
    stop sound


    scene kastil_merah
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show mc_baju_datar zorder 2:
        xalign 0.9
        yalign 0.2
    # anu ini ganti aset mc baju datar
    # anu kasih warna text dalam hati yang text dia pake ()
    mc "(wah kastinya ngastil banget)"
    mc "(tapi hawanya aneh)"
    hide mc_baju_datar

    show pelayan zorder 2
    pl "anda ini siapa?"
    show mc_baju_kaget zorder 2
    mc "eum a- ano-"
    show c_mangap zorder 2
    c "tch dasar gak sopan"
    mc "(huft dat so kripi)"
    hide mc_baju_kaget
    c "dia ini bangsawan"
    pl "o-oh maaf yang mulia hamba sudah lancang.."
    c "ya, sana minggir"
    hide pelayan 
    show mc_baju_senang zorder 2
    mc "eh kucing? makasi ya"
    hide c_mangap
    show c_mingkem zorder 2
    c "chiro"
    mc "ah"
    mc "makasi ya chiro"
    c "yh"
    hide c_mingkem

    #bg taman kastil merah 
    show l_datar zorder 2
    "/bisik"
    l "hey"
    show mc_baju_senang zorder 2
    mc "EH LUR-"
    l "ssstt"
    mc "uh.. jadi ini tempatnya?"
    l "iya, btw kamu nanti pura-pura ga kenal aku ya"
    l "takut ketauan ih"
    hide l_datar
    hide mc_baju_senang

    show k_terang zorder 2
    k "baby you look so soo magnificent"
    show q_terang zorder 2
    q "apasih sayang ih"
    show mc_baju_datar
    # ganti mc datar
    pause 0.2
    hide mc_baju_datar
    q "honey can i get that"
    q "dia terlihat sangat muda dan manis, pasti darahnya juga manis"
    k "tentu saja istriku, akan aku sajikan dia sebagai dessert mu malam ini"
    k "so you can stay magnificent forever and ever baby"
    hide q_terang
    hide k_terang
    
    show mc_baju_takut zorder 2
    # ganti mc baju takut
    mc "(what the hell is going on)"
    mc "(ini maksudnya aku kah)"
    mc "(what do they mean?)"
    hide mc_baju_takut

    show mc_baju_berpikir
    label minigame_kastil:
        $choice_positions = [(50, 100),  (700, 50), (1350, 100), (50, 450), (700, 450), (1350, 450)]
        
        $ renpy.music.set_volume(1.0, channel="music")
        $ renpy.music.play("audio/debat-bg.mp3", channel="music", loop=True)

        call screen bubble_choicef(debat_kastil)
        $ hasil = _return
        
        $ renpy.music.stop(channel="music", fadeout=1.0)

    hide mc_baju_berpikir

    show k_gelap zorder 2
    k "bawakan aku anak itu"
    show j_bayang
    j "SIAP LAKSANAKAN!"
    hide k_gelap

    show mc_baju_berpikir zorder 2
    pause 0.3
    show j_bayang zorder 2
    hide j_bayang
    hide mc_baju_berpikir

    scene hitam
    d "huhft untung aja aku ga telat"
    mc "D-D-dit!"
    scene kastil_merah 
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show mc_baju_takut zorder 2
    # ganti takut
    mc "aku mendengarnya"
    mc "mereka minum darah!"
    show d_kesel zorder 2
    d "mereka sudah menargetkanmu"
    d "kita udah ga bisa tinggal diam"
    mc "apa maksudmu?"
    d "sekarang"
    d "KITA AKAN LAWAN"
    hide mc_baju_takut
    hide d_kesel

    
    show d_datar zorder 2:
        xalign 1.0
        yalign 0.25
    pause 0.5
    hide d_datar

    show j_siap zorder 2:
        xalign 1.0
        yalign 0.25
    j "LOH LOH DIDIT!!"
    hide j_siap
    window hide 

    show k_terang zorder 2:
        xalign 0.008
        yalign 0.5
    show q_terang zorder 2:
        xalign 1.0
        yalign 0.5

    pause 0.5

    hide k_terang
    hide q_terang

    show k_gelap zorder 2:
        xalign 1.0
        yalign 0.5
    k "PRAJURIT GA BECUS!"
    hide k_gelap

    show q_gelap zorder 2:
        xalign 1.0
        yalign 0.5

    q "do you need my help baby~"
    hide q_gelap

    show k_gelap zorder 2:
        xalign 1.0
        yalign 0.5
    k "OFF WITH THEIR HEAD"
    hide k_gelap

    "/semua orang membeku"

    show k_gelap zorder 2:
        xalign 1.0
        yalign 0.5
    k "didit… didit… kali ini kau ga akan bisa lepas"
    k "DAN KAU DAN KAU DAN KALIAN SEMUA MUSNAH HUAHAHAHA"
    k "dan istriku akan jelita selamanya"
    show mc_takut zorder 2
    # ganti ke takut 
    show d_senyum zorder 2
    d "ampyunn dech masih aja sok sok an"
    d "hey mc sudah saatnya kita musnahkan raja bodoh dan ratu jelek itu"
    mc "..."
    hide d_senyum
    hide mc_baju_takut

    call battle
    
label ending_a:
    scene hitam
    pause 0.5
    scene tea_party
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show a_datar zorder  2
    d "akhirnya kamu bangun setelah 4 bulan tidur"
    hide a_datar
    mc "hah...aku kalah..?"
    scene hutan_bakar
    pause 0.5
    scene jamur asap
    pause 0.5
    scene hitam
    pause 0.3
    call screen credits_screen
    $mc_hp = 0
    $ renpy.full_restart()

label ending_b:
    scene putih
    pause 0.5
    scene ruangs 
    pause 0.5
    show l_bling
    l "terima kasih penyelamat.."
    hide l_bling
    mc "selamat tinggal....."
    "(sedih)"
    scene putih
    "(mc kembali ke dunia nyata)"
    scene gorong
    pause 0.3
    call screen credits_screen
    $renpy.full_restart()