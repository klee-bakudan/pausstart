screen notify(message):
    zorder 200

    frame:
        pos (config.screen_width - 20, 20)
        anchor (1.0, 0.0)
        padding (20, 12)
        background Solid("#162d6ac0")

        text message:
            size 32
            color "#FFFFFF"
            outlines [(absolute(2), "#00000080", absolute(2), absolute(2))]
            font "IrishGrover.ttf"

    timer 3.0 action Hide('notify')

    # edit notif disini nis