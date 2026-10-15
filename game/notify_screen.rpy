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

screen hp_indicator():
    zorder 100
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        xpadding 12
        ypadding 8
        background "#162d6ac0"

        hbox:
            spacing 8
            text "HP:" style "hp_label_text"
            bar range mc_hp_max value mc_hp:
                style "gui_bar"
                xysize (150, 18)
            text "[mc_hp]/[mc_hp_max]" style "hp_value_text"
    
style hp_label_text:
    size 16
    color "#fff"
    outlines[(absolute(1), "#000", absolute(1), absolute(1))]
    
style hp_value_text:
    size 16
    color "#fff"
    outlines[(absolute(1), "#000", absolute(1), absolute(1))]

    