<<<<<<< HEAD
﻿init python:
    import random 
    mc_hp = 0
    def add_mc_hp(amount):
        global mc_hp
        mc_hp += amount


define mc = Character("MC")
=======
﻿define mc = Character("[mcname]")
>>>>>>> ef9fb53b1f18594770b58338440e815e42937679
define d = Character("D'dit")
define k = Character("Raja Merah")
define q = Character("Ratu Merah")
define l = Character("Lucien")
define a = Character("Absolum")
define ar = Character("Arden")
define c = Character("Chiro")
define h = Character("Heiry")
define j = Character("Jendral")
define s = Character("Seroquin")
define reporter = Character("Reporter", what_color="#453a12")

transform item_popup:
    xalign 0.5
    yalign 1.1
    alpha 0.0
    zoom 0.8

    parallel:
        easeout 0.4 yalign 0.5

    parallel:
        linear 0.25 alpha 1.0

    parallel:
        easeout 0.2 zoom 1.05
        easein 0.1 zoom 1.0
    
transform slightleft:
    xalign 0.25
    yalign 1.0


transform topbottom:
    xalign 0.5
    yalign 0.0
    zoom 1.0

    ease 1.5 zoom 1.5
    ease 1.5 yalign 1.0


transform glitch_flicker:
    alpha 1.0

    block:
        linear 0.12 alpha 0.3
        linear 0.12 alpha 1.0
        linear 0.08 alpha 0.6
        linear 0.1 alpha 1.0
        linear 0.15 alpha 0.2
        linear 0.12 alpha 1.0
        pause 0.25
        repeat False
    
label start:

<<<<<<< HEAD
    $renpy.notify("MASUK SINI")
    
    $ mcname = renpy.input(
        "Siapa namamu?",
            allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ",
            length=10).strip()
=======
    $ renpy.notify("MASUK SINI")
    
    $ mcname = renpy.input(
        "Siapa namamu?", 
        allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ",
        length=7
    ).strip()
>>>>>>> ef9fb53b1f18594770b58338440e815e42937679

    $ renpy.notify("Captured: [mcname]")

    if not mcname:
<<<<<<< HEAD
        $mcname = "MC"
=======
        $ mcname = "MC"
>>>>>>> ef9fb53b1f18594770b58338440e815e42937679

    play sound "audio/transition-act.mp3"
    pause 1.0

    scene act1
    with dissolve
    
    pause 6.0
    stop sound

    scene reporter1
    with Fade(0.8, 0.2, 0.8)
  
    play sound "audio/breaking-news.mp3"
    pause 6.0

<<<<<<< HEAD
    reporter "Breaking news saudara, berikut adalah cuplikan real time demo yang terjadi"
=======
    reporter "Kita awali informasi pertama, dimana terjadi aksi unjuk rasa mahasiswa yang menuntut keadilan atas kasus korupsi fasilitas umum"
    reporter "yang melibatkan pejabat tinggi di kota ini. Aksi ini berlangsung damai, namun pihak kepolisian telah mengerahkan pasukan untuk mengamankan situasi."
>>>>>>> ef9fb53b1f18594770b58338440e815e42937679
    scene demo 1
    with Dissolve(.5)
    pause .5

    stop sound fadeout 1.0

    scene demo text with Dissolve(0.7)
    "Mahasiswa" "HIDUP MAHASISWA!"
<<<<<<< HEAD
=======
    play music "audio/demo-mhs.mp3"
>>>>>>> ef9fb53b1f18594770b58338440e815e42937679

    scene demo 1

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.35

    show pulisi zorder 2:
        xalign 0.99

    $ renpy.pause(0.2, hard=True)

    "Polisi" "WOI MUNDUR GA!"

    hide pulisi


    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.35

    show mc_demo_1 zorder 2:
        xalign 0.75

    $ renpy.pause(0.2, hard=True)

    mc "E-EHHH"

    hide mc_demo_1

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.35

    show mc_demo_2 at vpunch zorder 2:
        xalign 0.75

    $ renpy.pause(0.2, hard=True)

    mc "AWAS AWAS GAS AIR MATAAA"

    hide mc_demo_2
    hide darkoverlay
<<<<<<< HEAD

    scene run
    with Dissolve(0.5)
=======
    stop music fadeout 0.5

    scene run
    with Dissolve(0.5)
    play music "<from 22.0 to 30.0>audio/run.mp3"
>>>>>>> ef9fb53b1f18594770b58338440e815e42937679

    mc "SIAL"

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.4 alpha 0.5

    show mc_takut zorder 2:
        xanchor 0.85
        xpos 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "huh..huh..huh..."

    hide mc_takut
    hide darkoverlay
<<<<<<< HEAD


    scene gorong
    with Dissolve(0.7)

    pause 1.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4

    show mc_bingung zorder 2:
        xanchor 0.89
        xpos 0.94
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "hoh?"

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.4
        linear 0.4 alpha 0.7

    $ renpy.pause(0.3, hard=True)

    hide mc_bingung
    hide darkoverlay


    scene kelinci masuk
    with Dissolve(0.4)

    pause 0.5


    scene gorong 2
    with Dissolve(0.5)

    pause 1.5

=======

    scene gorong
    with Dissolve(0.7)

    pause 1.5

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4

    show mc_bingung zorder 2:
        xanchor 0.89
        xpos 0.94
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "hoh?"

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.4
        linear 0.4 alpha 0.7

    $ renpy.pause(0.3, hard=True)

    hide mc_bingung
    hide darkoverlay


    scene kelinci masuk
    with Dissolve(0.4)

    pause 0.5


    scene gorong 2
    with Dissolve(0.5)

    pause 1.5

>>>>>>> ef9fb53b1f18594770b58338440e815e42937679
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4

    show mc_kaget at vpunch zorder 2:
        xanchor 0.85
        xpos 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "LOHH?? KELINCI?? aku harus mengikutinya"

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.4
        linear 0.4 alpha 0.7

<<<<<<< HEAD
    $ renpy.pause(0.3, hard=True)

    hide mc_kaget
    hide darkoverlay

    scene masuk
    with Dissolve(0.6)

    pause 1.0

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.45

=======
    stop music fadeout 0.5

    $ renpy.pause(0.3, hard=True)

    hide mc_kaget
    hide darkoverlay

    scene masuk
    with Dissolve(0.6)


    pause 1.0

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.45

>>>>>>> ef9fb53b1f18594770b58338440e815e42937679
    show mc_takut zorder 2:
        xanchor 0.85
        xpos 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    play music "<from 0.0 to 8.0>audio/gorong.mp3"

<<<<<<< HEAD
=======
    mc "KYAAAHH" with vpunch
    stop music fadeout 0.5
>>>>>>> ef9fb53b1f18594770b58338440e815e42937679
    hide darkoverlay
    

    call play_jalan_puzzle("act_2")
<<<<<<< HEAD
    $add_mc_hp(7)
=======
>>>>>>> ef9fb53b1f18594770b58338440e815e42937679
    jump act_2
    return