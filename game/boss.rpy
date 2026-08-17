init python:
    import random

    def get_target_zoom(row):
        if row == 1:
            return target_row_1_zoom
        elif row == 2:
            return target_row_2_zoom
        else:
            return target_row_3_zoom

    def corkGunTransform(t, st, at):
        global cork_gun_pos
        global cork_gun_opos
        mousepos = renpy.get_mouse_pos()
        if mousepos[0] - cork_gun_size[0] / 2 <= config.screen_width - cork_gun_size[0] and mousepos[0] >= cork_gun_size[0] / 2:
            cork_gun_pos = (int(mousepos[0] - cork_gun_size[0] / 2),cork_gun_opos[1])
        cork_gun_pos = (cork_gun_pos[0], int(cork_gun_opos[1] + (mousepos[1] - config.screen_height / 2) / 7))
        t.xpos = cork_gun_pos[0]
        t.ypos = cork_gun_pos[1]
        return 0

    def setupTargets():
        target_start_x = 500
        target_row_1_y = 160
        target_row_2_y = 500
        target_row_3_y = 700
        target_spacing = 200
        target_down_time = (0.0, 2.0)
        target_up_time = 2.0
        current_column = 0

        for i in range(12):
            if i < 3:
                row = 1
                size_key = "top"
                y = target_row_1_y
                col = i
            elif i < 7:
                row = 2
                size_key = "middle"
                y = target_row_2_y
                col = current_column
                current_column += 1
            else:
                row = 3
                size_key = "bottom"
                y = target_row_3_y
                if i == 7:
                    current_column = 0
                else:
                    current_column += 1
                col = current_column

            target_transform = Transform(child="images/target-1-4.png",zoom=get_target_zoom(row))
            target_sprites.append(target_SM.create(target_transform))
            target_sprites[-1].row = row
            target_sprites[-1].down_time = random.uniform(target_down_time[0],target_down_time[1])
            target_sprites[-1].up_time = target_up_time
            target_sprites[-1].x = (target_start_x + (target_sizes[size_key][0] * col) + (target_spacing * col))
            target_sprites[-1].y = y
            target_sprites[-1].idle_animation_direction = "up"
            target_sprites[-1].current_frame = 5
            target_sprites[-1].animation_time = 0.0
            target_sprites[-1].hit = False

    def targetUpdate(st):
        global target_last_time
        if target_last_time is None:
            target_last_time = st
        dt = st - target_last_time
        target_last_time = st
        for target in target_sprites:
            zoom = get_target_zoom(target.row)
            if target.hit:
                if target.current_frame == 1:
                    target.current_frame = 2
                    if target.row == 1:
                        target.animation_time = 0
                    target.set_child(Transform(child="images/target-1-2.png",zoom=zoom))
                elif target.current_frame == 2:
                    target.current_frame = 3
                    target.set_child(Transform(child="images/target-1-3.png",zoom=zoom))
                elif target.current_frame == 3 and target.animation_time >= 0.1:
                    target.current_frame = 4
                    target.set_child(Transform(child="images/target-1-4.png",zoom=zoom))
                elif target.current_frame == 4 and target.animation_time >= 0.12:
                    target.current_frame = 5
                    target.set_child(Transform(child="images/target-1-3.png",zoom=zoom))
                elif target.current_frame == 5 and target.animation_time >= 0.13:
                    target.current_frame = 5
                    target.animation_time = 0
                    target.hit = False
                    target.set_child(Transform(child="images/target-1-4.png",zoom=zoom))
            else:
                if target.idle_animation_direction == "up":
                    if target.animation_time >= target.down_time:
                        if target.current_frame == 5:
                            target.current_frame = 3
                            target.set_child(Transform(child="images/target-1-3.png",zoom=zoom))
                        elif target.current_frame == 3 and target.animation_time >= target.down_time + 0.1:
                            target.current_frame = 2
                            target.set_child(Transform(child="images/target-1-2.png",zoom=zoom))
                        elif target.current_frame == 2 and target.animation_time >= target.down_time + 0.12:
                            target.current_frame = 1
                            target.idle_animation_direction = "down"
                            target.animation_time = 0
                            target.set_child(Transform(child="images/target-1-1.png",zoom=zoom))
                elif target.idle_animation_direction == "down":
                    if target.animation_time >= target.up_time:
                        if target.current_frame == 1:
                            target.current_frame = 2
                            target.set_child(Transform(child="images/target-1-2.png",zoom=zoom))
                        elif target.current_frame == 2:
                            target.current_frame = 3
                            target.set_child(Transform(child="images/target-1-3.png",zoom=zoom))
                        elif target.current_frame == 3 and target.animation_time >= target.up_time + 0.1:
                            target.current_frame = 4
                            target.set_child(Transform(child="images/target-1-4.png",zoom=zoom))
                        elif target.current_frame == 4 and target.animation_time >= target.up_time + 0.12:
                            target.current_frame = 5
                            target.set_child(Transform(child="images/target-1-3.png", zoom=zoom))
                        elif target.current_frame == 5 and target.animation_time >= target.up_time + 0.13:
                            target.current_frame = 5
                            target.idle_animation_direction = "up"
                            target.animation_time = 0
                            target.hit = False
                            target.set_child(Transform(child="images/target-1-4.png", zoom=zoom))
            target.animation_time += dt
        return 0

    def corkEvents(event, x, y, st):
        import pygame_sdl2 as pygame
        global gallery_ammo
        global gallery_over
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and y < config.screen_height - 10:
                if gallery_ammo <= 0 or gallery_over:
                    return
                gallery_ammo -= 1
                cork_spirets.append(cork_SM.create(cork_transform))
                cork_spirets[-1].original_size = (110, 138)
                cork_spirets[-1].x = (cork_gun_pos[0] + cork_spirets[-1].original_size[0])
                cork_spirets[-1].y = cork_gun_pos[1]
                cork_spirets[-1].original_pos = (cork_spirets[-1].x,cork_spirets[-1].y)
                cork_spirets[-1].zoom = 1.0
                cork_spirets[-1].move_to_pos = (cork_gun_pos[0],y)
                cork_spirets[-1].travel_time = 0.0
                cork_SM.redraw(0)

    def corkUpdate(st):
        global score
        global gallery_ammo
        global gallery_over
        corks_to_remove = []
        for cork in cork_spirets:
            if cork.travel_time < 0.25:
                cork.travel_time += 0.01
                progress = min(cork.travel_time / 0.25,1.0)
                cork.y = (cork.original_pos[1] + (cork.move_to_pos[1] - cork.original_pos[1]) * progress)
                cork.zoom = max(1.0 - 0.9 * progress,0.1)
                cork.x += 2.4
                t = Transform(child=cork_image,zoom=cork.zoom)
                cork.set_child(t)
            else:
                hit_something = False
                for target in target_sprites:
                    if target.current_frame == 1 and not target.hit:
                        size_key = {1: "top",2: "middle",3: "bottom"}[target.row]
                        w, h = target_sizes[size_key]

                        hitbox_extra_x = 50
                        hitbox_extra_y = 50

                        extra = 120 if target.row == 1 else 0

                        if (target.x - hitbox_extra_x <= (cork.x - cork.original_size[0] / 2) <= target.x + w + hitbox_extra_x and target.y - hitbox_extra_y <= (cork.y - cork.original_size[1] / 2)  <= target.y + h - extra + hitbox_extra_y):
                            target.hit = True
                            points = { 1: 5, 2: 10, 3: 15 }[target.row]
                            score = max(0,score - points)
                            target_SM.redraw(0)
                            hit_something = True
                            break
                corks_to_remove.append(cork)
                if hit_something:
                    renpy.restart_interaction()

        for cork in corks_to_remove:
            cork.destroy()
            cork_spirets.remove(cork)

        if gallery_ammo <= 0 and not cork_spirets and not gallery_over:
            gallery_over = True
            renpy.end_interaction("gallery_finished")

        return 0

    def prepareShootingGallery():
        global score
        global target_last_time
        global gallery_ammo
        global gallery_over
        score = 100
        target_last_time = None
        gallery_ammo = mc_hp
        add_mc_hp(-mc_hp) 
        renpy.notify("HP terpakai jadi %d peluru!" % gallery_ammo)
        gallery_over = False

        for target in target_sprites:
            target.hit = False
            target.idle_animation_direction = "up"
            target.animation_time = 0.0
            target.current_frame = 5
            target.set_child(Transform(child="images/target-1-4.png",zoom=get_target_zoom(target.row)))
transform half_size:
    zoom 1.0

transform spotlights:
    zoom 1.0
    blend "add"
    alpha 0.5

screen scene_1:

    image "images/scene-1-background.png" at half_size

    textbutton "Shooting Gallery":
        align (0.7, 0.3)

        text_size 40
        text_color "#FFFFFF"
        text_hover_color "#FFBF5F"

        background None
        hover_background Solid("#00000080")

        padding (20, 12)

        action Show("shooting_gallery")


screen shooting_gallery:

    on "show" action [Function(prepareShootingGallery),SetVariable("default_mouse", "targetname"),SetVariable("shooting_gallery", True)]
    image "images/targets-background.png" at half_size
    add target_SM
    image "images/shooting-gallery-background.png" at half_size
    image "images/spotlights.png" at spotlights
    add cork_gun_transform
    add cork_SM

    frame:
        pos (20, 0)
        background Solid("#00000090")
        xysize (400, 160)
        padding (0, 0)

    text "Score: [score]":
        color "#FFFFFF"
        outlines [(absolute(2), "#00000050", absolute(2), absolute(2))]
        size 50
        pos (110, 80)
        anchor (0.0, 0.0)

label shooting_gallery_setup:
    $ cork_gun_image = Image("images/cork-gun.png")
    $ cork_gun_size = (330, 384)
    $ cork_gun_pos = (0, 0)
    $ cork_gun_opos = (int(config.screen_width / 2 - cork_gun_size[0] / 2),int(config.screen_height - cork_gun_size[1]))
    $ cork_gun_transform = Transform(child=cork_gun_image,zoom=1.0, pos=(cork_gun_opos[0], cork_gun_opos[1]),function=corkGunTransform)
    $ cork_image = Image("images/cork.png")
    $ cork_transform = Transform(child=cork_image,zoom=1.0)
    $ cork_spirets = []
    $ cork_SM = SpriteManager(update=corkUpdate,event=corkEvents)
    $ target_SM = SpriteManager(update=targetUpdate)
    $ target_row_1_zoom = 1.2
    $ target_row_2_zoom = 0.8
    $ target_row_3_zoom = 0.6
    $ target_sizes = {"top": ( 376 * target_row_1_zoom, 455 * target_row_1_zoom),"middle": (376 * target_row_2_zoom, 455 * target_row_2_zoom),"bottom": (376 * target_row_3_zoom,455 * target_row_3_zoom)}
    $ target_sprites = []
    $ target_last_time = None
    $ setupTargets()
    $ score = 100
    $ shooting_gallery = False
    call screen scene_1
    return


label boss:
    call shooting_gallery_setup
    return