label sikrit1:
    scene bgl 

    image mc_dance = Animation(
        "images/mc_dance-1.1.png", 0.15,
        "images/mc_dance-1.2.png", 0.15,
        "images/mc_dance-2.1.png", 0.15,
        "images/mc_dance-2.2.png", 0.15,
        "images/mc_dance-3.1.png", 0.15,
        "images/mc_dance-3.2.png", 0.15,
        repeat=True
    )

    show mc_dance:
        xalign 0.1

    play music "audio/uwa-uwa_dance.mp3"

    $ renpy.pause(67, hard=True)
    pause 4

    call screen credits_screen
    $ renpy.full_restart()