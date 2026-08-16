define mc = Character("MC")
define d = Character("D'dit")
define k = Character("Raja Merah")
define q = Character("Ratu Merah")
define l = Character("Lucien")
define a = Character("Absolum")
define ar = Character("Arden")
define c = Character("Chiro")
define h = Character("Heiry")
define j = Character("Jendral")
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

    # $ renpy.notify("MASUK SINI")
    
    # $ mcname = renpy.input(
    #     "Siapa namamu?",
    #     allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ",
    #     length=10
    # ).strip()

    # $ renpy.notify("Captured: [mcname]")

    # if not mcname:
    #     $ mcname = "MC"

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

    reporter "Breaking news saudara, berikut adalah cuplikan real time demo yang terjadi"
    scene demo 1
    with Dissolve(.5)
    pause .5

    stop sound fadeout 1.0

    scene demo text with Dissolve(0.7)
    "Mahasiswa" "HIDUP MAHASISWA!"

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

    scene run
    with Dissolve(0.5)

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

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.4

    show mc_kaget zorder 2:
        xanchor 0.85
        xpos 0.99
        yalign 0.25

    $ renpy.pause(0.2, hard=True)

    mc "LOHH?? KELINCI?? aku harus mengikutinya" with vpunch

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.4
        linear 0.4 alpha 0.7

    $ renpy.pause(0.3, hard=True)

    hide mc_kaget
    hide darkoverlay

    scene masuk
    with Dissolve(0.6)

    pause 1.0

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.0
        linear 0.3 alpha 0.45

    show mc_takut zorder 2:
        xanchor 0.85
        xpos 0.99
        yalign 0.25

    $ renpy.pause(0.5, hard=True)

    mc "KYAAAHH" with vpunch

    hide darkoverlay
    

    jump act_2
    return