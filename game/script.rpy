# define mc = Character("[mcname]")
define mc = Character("MC")
define d = Character("D'dit")
define k = Character("Raja Merah")
define q = Character("Ratu Merah")
define l = Character("Lucien")
define a = Character("Absolum")
define ar = Character("Arden")
define c = Character("Chiro")
define h = Character("Heiry")


label start:

    # python:
    #     mcname = renpy.input("Ketik nama").strip() or "kei"

    scene act1
    with dissolve

    scene reporter1
    with dissolve
    pause 10.0
    "Reporter" "Breaking news saudara, berikut adalah cuplikan real time demo yang terjadi"

    scene demo 1
    with Dissolve(.5)
    pause .5

    scene demo text
    "Mahasiswa" "HIDUP MAHASISWA!"

    scene demo 1
    show pulisi:
        xalign 0.80
    "WOI MUNDUR GA!"
    hide pulisi


    show mc_demo_1:
        xalign 0.75
    mc "E-EHHH"
    hide mc_demo_1

    show mc_demo_2:
        xalign 0.75
    mc "AWAS AWAS GAS AIR MATAAA"
    hide mc_demo_2


    scene run
    mc "KYAAAHH"

    show mc_takut zorder 2:
        xalign 0.75
        yalign 0.25
        

    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    with dissolve

    mc "huh..huh..huh..."
    hide mc_takut

    scene gorong
    pause 1.5

    show mc_bingung zorder 2:
        xalign 0.75
        yalign 0.25

    pause 1.5
    
    show black onlayer master zorder 1 as darkoverlay:
        alpha 0.5
    with dissolve


    return