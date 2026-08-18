init python:
    def setup_puzzle():
        initial_piece_coordinates.clear()
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def piece_drop(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.hide_screen("reassemble_puzzle")
                renpy.end_interaction("puzzle_done")

screen reassemble_puzzle:

    image "backgroundp.png"

    frame:
        background "puzzle-frame.png"
        xysize full_page_size
        anchor(0.0, 0.0)
        pos(550, 135)

    draggroup:
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "%s/piece-%s.png" % (current_puzzle_folder, i + 1)
    
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "%s/piece-%s.png" % (current_puzzle_folder, i + 1): 
                    alpha 0.4


define page_pieces = 9
define full_page_size = (970, 1059)
define piece_coordinates = [(711, 286), (990, 286), (1269, 286), (711, 565), (990, 565), (1269, 565), (711,844), (990, 844), (1269, 844)] 
default initial_piece_coordinates = []
default finished_pieces = 0
default current_puzzle_folder = ""

label play_reassemble_puzzle(image_folder):
    $current_puzzle_folder = image_folder
    $finished_pieces =  0
    $setup_puzzle()
    call screen reassemble_puzzle
    $add_mc_hp(7)
    return