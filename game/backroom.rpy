init python:
    renpy.music.register_channel("music", "sfx", loop=False)

label backroom:
    scene backroom
    play music "audio/backroom.mp3"
    pause 0.3
    show k_gelap zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 930

    k "jadi gimana 'penyelamat'"
    hide k_gelap

    show k_gelap at expression_pop zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 930

    k "i owe for everything"
    k "i owe your blood"
    k "i owe this throne"

    hide k_gelap
    show d_mc-neutral at expression_pop zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 650
    d "just because you didn't get to be a great king"
    hide d_mc-neutral
    show k_gelap at expression_pop zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 930
    k "IM A F#### GREAT KING"
    hide k_gelap
    show d_mc-upset at expression_pop zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 650
    d "IM NOT THE SAVIOUR"
    hide d_mc-upset
    show k_gelap at expression_pop zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 930
    k "stay in character!"
    hide k_gelap
    show d_mc-upset at expression_pop zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 650
    d "IM NOT THE SAVIOUR"
    hide d_mc-upset
    show k_gelap at expression_pop zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 930
    k "STAY IN CHARACTER"
    hide k_gelap

    show d_mc-marah at expression_pop zorder 2:
        xalign 0.5
        yanchor 0.7
        ypos 650
    d "######"
    hide d_mc-marah

    call screen credits_screen
    $renpy.full_restart()