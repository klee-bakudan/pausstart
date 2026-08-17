label act_5:
    scene act5 
    pause 0.5

    scene butut
    pause 0.5
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show mc_hah zorder 2
    mc "itulah masukkan text"
    hide mc_hah

    scene butut2
    pause 0.5
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    show mc_tch zorder 2
    mc "yayaya saya setuju masukkan text"
    hide mc_tch

    scene tea_party
    pause 0.5
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show d_senyum zorder 2
    d "Uweaaa, lihat siapa yang dibawa kelinci imut kali ini~"
    d "Kelinci nackal~, kalau lagi kencan ga perlu pamer sana sini juga kali~"
    hide d_senyum

    show l_datar zorder 2
    l "i-imut? Apasih!! Ini si mc lohh yang ada di gulungan takdir itu"
    hide l_datar

    show d_senyum zorder 2 
    d "owhhhh ternyata kamyu~"
    d "selamat datang di wonderland~ maaf ya kalo berdebu"
    d "habis bakar-bakar kecil soalnya HAHAHAHA~"
    hide d_senyum

    show h_senyum zorder 2
    h "BAWAHAHAHA bakar-bakar kecil katanya!"
    show ar_jengkel
    ar "Aduhh keluar lagi tuh joks garing"

    show mc_bingung zorder 2
    mc "Aneh banget... Ini beneran orang yang bakal bantu aku..?"

    show d_senyum zorder 2
    d "HAHA~ pasti capek kan dijalan, ayok sini kita minum teh dulu sudah waktunya minum teh~"
    hide d_senyum
    show h_senyum zorder 2
    h "IH DORMMOUSE JANGAN AMBIL PISANG GORENG AKU"
    show 

    show mc_datar zorder 2
    mc "Jadi.. aku mau bertanya tentang-"
    # sfx
    hide mc_datar
    # arden

    show d_kesel zorder 2
    d "dih sok ngeklaim lu"
    hide d_kesel

    show mc_datar zorder 2
    mc "Lurcien bantu aku dong..."
    hide mc_datar
    show mc_kaget zorder 2
    mc "lah LU NAPA SEMBUNYI KE BAWAH!?"

    show l_takut zorder 2
    l "E-eh maaf soalnya aku takut sama tikus itu.."
    mc "LAH ITU TIKUS?! Kok gede?"
    l "Co-coba kamu pisahin mereka…"
    l "sekalian jauhin dari aku peliss"

    label minigame5:
        scene tea_party
        show black onlayer master zorder 1 as darkoverlay:
            alpha 0.5
        show mc_berpikir zorder 2 

        $choice_positions = [(50, 50), (100, 50), (200, 50)]
        $choice_texts = ["lumayan nih, pisgor enak nih sama teh",
        "pergi aja kali ya..?", "haduh bisa serius ga sih!"]

        call screen bubble_choice(choice_texts)
        $hasil = _return
        pause 3

        if hasil == 0:
            jump pilihan1
        elif hasil ==  1:
            jump pilihan2
        elif hasil == 2:
            jump pilihan3
    
    label pilihan1:
        scene meja_tea
        pause 0.1
        show mc_ngiler
        mc "Eh… keknya jangan makan dulu deh"
        hide mc_ngiler
    jump act5_lanjut
    
    label pilihan2:
        scene meja_tea
        show mc_tch
        mc "Ini beneran kita minum teh padahal diluar lagi kacau balau??"
        mc "Kalau ga mau diskusi, aku pergi aja"
        hide mc_tch
        # arden
        show h_mingkem zorder 2
        h "Bye-bye~"
        hide h_mingkem
        show mc_kaget
        mc "{eh.. Bener juga sih kalau aku pergi tanpa tujuan nanti ketangkep}"
        hide mc_kaget
    jump act5_lanjut
   
    label pilihan3:
        scene meja_tea
        show mc_tch
        mc "WOI! INI KALIAN BENARAN MAU MENGHADAPI MALA PETAKA!?"
        mc "Aku datang ke dunia ini BUKAN buat minum teh!"
        mc "tapi menghadapi mala petaka sialan yang harus aku selesaikan DEMI KALIAN"
        hide mc_tch
    jump act5_lanjut2 
    
label act5_lanjut:
    scene tea_party
    pause 0.3
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show d_datar zorder 2
    d "Okayy sepertinya pahlawan tidak memiliki jadwal untuk minum teh.."
    d "Ya..seperti yang terlihat wilayah ini udah kebakar habis.."
    hide d_datar
    show d_senyum zorder 2
    d "cuman sisa meja ini doang sih dan rumah si arden yang sekarang ada di tanah tuh~"
    hide d_senyum
    # arden
    show h_senyum zorder 2
    h "hehe rumah aku kebakar sih"
    h "(tertawa)"
    h "Semuanya! semua-muanyaaa terbakar… TERBAKARR"
    hide h_senyum

    show d_senyum zorder 2
    d "yayaya saya setuju~"
    show mc_datar  zorder 2 
    mc "jadi gimana??"
    mc "ini JADINYA GIMANA DIDIT?"
    d "decision~ desicion~"

    label minigame6:
        scene tea_party
        show black onlayer master zorder 1 as darkoverlay:
            alpha 0.5
        show mc_berpikir zorder 2 

        $choice_positions = [(50, 50), (100, 50), (200, 50)]
        $choice_texts = ["aku harus nyelesaiin apa yang udah ditakdirkan biar bisa cepet pulang",
        "ini udah diluar batasku sepertinya aku ga bisa ngerubah apa-apa", "ini semua ga bisa dibiarin gitu aja, aku harus memperjuangkan keadilan!"]

        call screen bubble_choice(choice_texts)
        $hasil = _return
        pause 3

        if hasil == 0:
            jump pilihan12
        elif hasil ==  1:
            jump pilihan22
        elif hasil == 2:
            jump pilihan32
    
    label pilihan12:
    jump act_6
    
    label pilihan22:
    jump act_6
   
    label pilihan32:
    jump act_6
    
    jump act_6


return