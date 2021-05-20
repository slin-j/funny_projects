r1 = [0, 3, 2, 4, 0, 2, 0, 4, 2, 0]
r2 = [2,1,0,2]

def how_much_water(bricks_array: list) -> int:
    result = 0 # waterblocks
    running = True
    # bricks_array.append(0)
    i = 0

    while running and (i-1) < len(bricks_array):    # for every it in bricks_array
        start_height = bricks_array[i]
        max_height = 0
        len_of_hole = 0
        
        i += 1
        try:
            while running and bricks_array[i] < start_height:
                if bricks_array[i] > max_height:
                    max_height = bricks_array[i]

                i += 1

                if i == len(bricks_array):
                    running = False
                else:
                    result += start_height - bricks_array[i]
                    len_of_hole += 1
        except IndexError:
            break

        if start_height > max_height:
            result -= len_of_hole * (start_height - max_height)

            

            
    
    return result

print("Function returned: ", how_much_water(r2))