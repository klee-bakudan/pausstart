init python:
    def setup_jalan_game():
        global jalans
        global connected_jalans

        jalans = []
        connected_jalans = []

        generate_grid_path()
        create_jalans()
    
    def get_direction(from_cell, to_cell):
        if to_cell == from_cell + 1:
            return "right"
        elif to_cell == from_cell - 1:
            return "left"
        elif to_cell == from_cell + jalan_columns:
            return "bottom"
        elif to_cell == from_cell - jalan_columns:
            return "top"
    
    def create_jalans():
        max_t = renpy.random.choice([2, 3])
        max_cross = renpy.random.choice([1,2])
        t_used = 0
        cross_used = 0

        for i in range(1, amount_of_jalans + 1):
            if i in grid_path:
                idx = grid_path.index(i)
                dirs = set()

                if idx == 0:
                    dirs.add("left")
                else:
                    dirs.add(get_direction(grid_path[idx], grid_path[idx - 1]))
                
                if idx == len(grid_path)  - 1:
                    dirs.add("right")
                else: 
                    dirs.add(get_direction(grid_path[idx], grid_path[idx + 1]))
                
                if dirs in ({"top", "bottom"}, {"left", "right"}):
                    minimal_type = "straight"
                else:
                    minimal_type = "curved"
                
                choices = [minimal_type] * 8
                if t_used < max_t:
                    choices += ["t"] * 2
                if cross_used < max_cross:
                    choices += ["cross"] * 1
                
                jalan_type = renpy.random.choice(choices)
                if jalan_type == "t":
                    t_used += 1
                elif jalan_type == "cross":
                    cross_used += 1
                
                create_jalan(type = jalan_type, cell = i)

            else:
                decoy_choices = ["straight", "curved"] * 4
                if t_used < max_t:
                    decoy_choices += ["t"] * 2
                if cross_used < max_cross:
                    decoy_choices += ["cross"] * 1
                
                random_type = renpy.random.choice(decoy_choices)
                if random_type == "t":
                    t_used += 1
                elif random_type == "cross":
                    cross_used += 1

                create_jalan(type = random_type, cell = i)
            
    def create_jalan(type, cell):
        jalan_image = "%s-jalan.png" % type
        jalan_end_points = list(jalan_type[type])
        final_jalan = [jalan_image, type, jalan_end_points, cell, 0]
        jalans.append(final_jalan)
            
    def generate_grid_path():
        global grid_path

        grid_path = [1]

        for i in range(jalan_columns + jalan_rows - 2):
            if grid_path[-1] % jalan_columns == 0 and grid_path[-1] <= amount_of_jalans - jalan_columns:
                grid_path.append(grid_path[-1] + jalan_columns)

            elif grid_path[-1] % jalan_columns != 0 and grid_path[-1] <= amount_of_jalans - jalan_columns:
                potential_cells = ["right", "down"]
                random_pick = renpy.random.choice(potential_cells)
                if random_pick == "right":
                    grid_path.append(grid_path[-1] + 1)
                elif random_pick == "down":
                    grid_path.append(grid_path[-1] + jalan_columns)
                    
            elif grid_path[-1]  > amount_of_jalans - jalan_columns:
                grid_path.append(grid_path[-1] + 1)
            
    def update_jalan_endpoins(cell):
        for jalan in jalans:
            if jalan[3] == cell:
                for endpoint in jalan[2]:
                    if endpoint == "top":
                        endpoint_index = jalan[2].index("top")
                        jalan[2][endpoint_index] = "right"
                    elif endpoint == "right":
                        endpoint_index = jalan[2].index("right")
                        jalan[2][endpoint_index] = "bottom"
                    elif endpoint == "bottom":
                        endpoint_index = jalan[2].index("bottom")
                        jalan[2][endpoint_index] = "left"
                    elif endpoint == "left":
                        endpoint_index = jalan[2].index("left")
                        jalan[2][endpoint_index] = "top"
                break
    
    def check_jalan_connections():
        global connected_jalans

        connected_jalans = []

        jalan_by_cell = {}
        for j in jalans:
            jalan_by_cell[j[3]] = j
        
        start = jalan_by_cell.get(1)
        if start is None or "left" not in start[2]:
            return

        directions = {"right" : (1, "left"), "left" : (-1, "right"), "top" : (-jalan_columns, "bottom"), "bottom" : (jalan_columns, "top")}

        visited_cells = {1}
        connected_jalans.append(start)
        queue = [start]

        while queue:
            current = queue.pop(0)
            cell = current[3]

            for direction, (offset, needed_endpoint) in directions.items():
                if direction not in current[2]:
                    continue
                if direction == "right" and cell % jalan_columns == 0:
                    continue
                if direction == "left" and cell % jalan_columns == 1:
                    continue
                if direction == "top" and cell <= jalan_columns:
                    continue
                if direction == "bottom" and cell > amount_of_jalans - jalan_columns:
                    continue
                
                neighbor_cell = cell + offset
                neighbor = jalan_by_cell.get(neighbor_cell)
                if neighbor is None or neighbor_cell in visited_cells:
                    continue

                if needed_endpoint in neighbor[2]:
                    visited_cells.add(neighbor_cell)
                    connected_jalans.append(neighbor)
                    queue.append(neighbor)
                
        last_jalan = jalan_by_cell.get(amount_of_jalans)
        if last_jalan is not None and amount_of_jalans in visited_cells:
            if "right" in last_jalan[2]:
                renpy.hide_screen("connect_the_jalans")
                add_mc_hp(7)
                renpy.jump(jalan_next_label)
        
    def rotate_jalan(cell):
        if jalans[cell - 1][4] == 360:
            jalans[cell - 1][4] = 90
        else:
            jalans[cell - 1][4] += 90
            
        update_jalan_endpoins(cell)
        check_jalan_connections()
    
screen connect_the_jalans:
    add "backgroundj.png"

    grid jalan_columns  jalan_rows:
        spacing 0
        pos(640, 140)
        anchor(0.0, 0.0)
        for jalan in jalans:
            if jalan in connected_jalans:
                imagebutton idle Transform(jalan[1] + "-jalan-connected.png", rotate = jalan[4], rotate_pad = False) action Function(rotate_jalan, cell=jalan[3])
            else:
                imagebutton idle Transform(jalan[0], rotate = jalan[4], rotate_pad = False) action Function(rotate_jalan, cell = jalan[3])

default jalan_rows = 4
default jalan_columns = 4
default amount_of_jalans = jalan_rows * jalan_columns
default grid_path = []
default jalans = []
default jalan_type = {"straight": ("top", "bottom"), "curved": ("right", "bottom"), "t": ("top", "bottom", "left"), "cross": ("top", "bottom", "left", "right")}
default connected_jalans = []
default jalan_next_label = None

label play_jalan_puzzle(next_label):
    $jalan_next_label = next_label
    $setup_jalan_game()
    call screen connect_the_jalans
    return

