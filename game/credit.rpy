screen credits_screen():
    modal True
    zorder 100

    on "show" action Play("music", "audio/credits-music.mp3")

    add "credits-bg.png"

    fixed:
        xfill True
        yfill True

        vbox:
            id "credits_vbox"
            xalign 0.5
            spacing 40
            at credits_scroll

            null height 800
            text "{b}TERIMA KASIH TELAH BERMAIN{/b}" size 60 xalign 0.5 color "#FFFFFF"
            null height 60
            text "ILLUSTRATOR & FRONT-END" size 40 xalign 0.5 color "#F2A65A"
            text "Nisa" size 34 xalign 0.5 color "#FFFFFF"
            text "Sukma" size 34 xalign 0.5 color "#FFFFFF"
            null height 40
            text "BACK-END" size 40 xalign 0.5 color "#F2A65A"
            text "Afril" size 34 xalign 0.5 color "#FFFFFF"
            null height 40
            text "BACKGROUND SOUND & SFX" size 40 xalign 0.5 color "#F2A65A"
            text "Pixabay:" size 30 xalign 0.5 color "#CCCCCC"
            text "Lux-aeterna" size 30 xalign 0.5 color "#FFFFFF"
            text "luxaeterna2026" size 30 xalign 0.5 color "#FFFFFF"
            text "Kuzu420" size 30 xalign 0.5 color "#FFFFFF"
            text "9JackJack8" size 30 xalign 0.5 color "#FFFFFF"
            text "poorenglishjuggler" size 30 xalign 0.5 color "#FFFFFF"
            text "Tim_Kulig_Free_Music" size 30 xalign 0.5 color "#FFFFFF"
            text "LCWolfMusic" size 30 xalign 0.5 color "#FFFFFF"
            null height 800

    timer 40.0 action Return()

    key "game_menu" action Return()
    button:
        xfill True yfill True
        action Return()
        background None

transform credits_scroll:
    yoffset 0
    linear 40.0 yoffset -3000