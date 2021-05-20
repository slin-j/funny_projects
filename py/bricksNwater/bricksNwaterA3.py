r1 = [0, 3, 2, 4, 0, 2, 0, 4, 2, 0]
r2 = [2,1,0,2]

def how_much_water(bricks_array: list) -> int:
    result = 0 # waterblocks

    arr_max_pos = []
    for i in range(len(bricks_array)):
        if bricks_array[i] == max(bricks_array):
            arr_max_pos.append(i)

    print("amp:",arr_max_pos)

    if len(arr_max_pos) > 1:
        for i in range(arr_max_pos[0],arr_max_pos[-1]):
            result += max(bricks_array) - bricks_array[i]

    return result

print("Function returned: ", how_much_water(r1))