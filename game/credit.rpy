screen credits_screen():
    modal True
    zorder 100

    on "show" action Play("music", "audio/credit-bg.mp3")

    add "hitam.png"

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
            text "Drowning Teddy (Dreamcore Ambient) — 9JackJack8" size 26 xalign 0.5 color "#FFFFFF"
            text "Drowsy (Liminal Dreamcore) — 9JackJack8" size 26 xalign 0.5 color "#FFFFFF"
            text "Glass Breaking — Charlie_Raven" size 26 xalign 0.5 color "#FFFFFF"
            text "pajama parties — chiikawa" size 26 xalign 0.5 color "#FFFFFF"
            text "Dramatic Whoosh Trailer — DRAGON-STUDIO" size 26 xalign 0.5 color "#FFFFFF"
            text "Demonstration 1 — freesound_community" size 26 xalign 0.5 color "#FFFFFF"
            text "complex — Kane Parsons" size 26 xalign 0.5 color "#FFFFFF"
            text "China in Space (Cosmic melody) — Kuzu420" size 26 xalign 0.5 color "#FFFFFF"
            text "Weirdcore — LCWolfMusic" size 26 xalign 0.5 color "#FFFFFF"
            text "woosh-building- — Liecio" size 26 xalign 0.5 color "#FFFFFF"
            text "exit-the-simulation-slowed-cinematic-music — Lux-aeterna" size 26 xalign 0.5 color "#FFFFFF"
            text "Hollow Loop (Sped up) — Lux-aeterna" size 26 xalign 0.5 color "#FFFFFF"
            text "Liminal deep ambient — Luxaeterna2026" size 26 xalign 0.5 color "#FFFFFF"
            text "Dark Liminal Void Ambient — Luxaeterna2026" size 26 xalign 0.5 color "#FFFFFF"
            text "ambient-monster-behemoth-dragon-voice-angry-scream-cry-roar-grow — PhatPhrogStudio" size 26 xalign 0.5 color "#FFFFFF"
            text "Zephyrcade — Pixelmaniaxx" size 26 xalign 0.5 color "#FFFFFF"
            text "Simplicity — Tim_Kulig_Free_Music" size 26 xalign 0.5 color "#FFFFFF"
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