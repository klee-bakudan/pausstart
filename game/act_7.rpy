define debat_kastil = [("Diluar banyak gelandangan tapi di kastil ini foya foya", None),
("Di sini terang ya lampunya ga kayak di luar", None), ("Salah ngomong dikit ke raja nyawa hampir melayang", None),
("Liat Chiro sama didit kek langit dan bumi", " yang kerja disini hidupnya enak sedangkan yang ngga mah gembel"),
("Heri jadi gila gegara rumah dan keluarganya terbakar", "kerjaan tutup mata sama masalah rakyat"),
("Kebijakan di sini sama aja kek di dunia nyata", "menguntungkan penghuni kastil saja")]

label act_7:
    scene act7 
    pause 0.5

    scene kastil_merah
    pause 0.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    
    show mc_berpikir zorder 2
    mc "heum kok keknya ada yang aneh ya"
    mc "apa ya..?"

    label minigame_kastil:
        $choice_positions = [(50, 100),  (700, 50), (1350, 100), (50, 450), (700, 450), (1350, 450)]

        call screen bubble_choicef(debat_kastil)
        $ hasil = _return

    hide mc_berpikir
    
    show d_kesel zorder 2
    pause 0.5
    hide d_kesel

    show j_siap zorder 2
    j "LOH LOH DIDIT!!"
    hide j_siap

    show k_terang zorder 2
    show q_terang zorder 2
    pause 0.5

    hide k_terang
    hide q_terang

    show k_gelap zorder 2
    k "PRAJURIT GA BECUS!"
    show q_gelap zorder 2
    q "do you need my help baby~"
    k "OFF WITH THEIR HEAD"
    hide k_gelap
    hide q_gelap

    "semua orang membeku"

    show k_gelap zorder 2 
    k "didit… didit… kali ini kau ga akan bisa lepas"
    k "DAN KAU DAN KAU DAN KALIAN SEMUA MUSNAH HUAHAHAHA"
    k "kau kira kebakaran itu kebetulan aja? Kau pikir sumbangan itu beneran gratis?"
    k "DASAR BODOH!"
    k "Akulah yang mengendalikan semuanya."
    k "SEMUANYA"
    # tolomg bold text
    k "Kau pikir kesenjangan ini t tumbuh kayak rumput liar?"
    k "Infrastruktur yang timpang, daerah yang dibiarkan tertinggal, masyarakat yang dipaksa hidup dalam kekurangan."
    k "Aku yang membiarkannya. Aku yang sengaja menciptakan kesenjangan itu."
    k "Sadar ga kalau orang yang kelaparan lebih mudah dikendalikan"
    k "Orang yang sibuk bertahan hidup nggak punya waktu untuk bertanya kalau mereka yang mulai berani bersuara? Tinggal bungkam."
    k "Kau tahu apa yang lebih mudah daripada membuat orang patuh?"
    k "Memberi mereka sesuatu yang mereka butuhkan, lalu membuat mereka merasa berutang."
    k "Sumbangan, bantuan, jatah, fasilitas kau pikir semua itu cuma kewajiban?"
    k "Semua itu investasi."
    k "Aku beri mereka sedikit, mereka memberiku suara."
    k "Dan yang tidak mau ikut? Yang tidak mau bersuara? Yang berani melawan?"
    k "Mereka akan kehilangan hak. Kehilangan tempat. Kehilangan semuanya."
    k "Sampai akhirnya mereka tidak punya pilihan selain tunduk."
    k "AKULAH RAJA"
    k "Akulah yang menentukan siapa yang mendapat bagian, siapa yang boleh bersuara, dan siapa yang harus disingkirkan."
    k "AKU LAH SANG PENGUASA!!!!"
    # sfx

    call boss
    
    


    return