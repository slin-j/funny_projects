from time import time, time_ns

r1 = [0, 3, 2, 4, 0, 2, 0, 4, 2, 0]
r2 = [2,1,0,2]
r3 = [6,2,3,4,5,6,5,4,6,2,1]
r4 = [0, 3, 2, 4]
r5 = [0,1,3,2,4,0,4,3]
r6 = [1,0,3,0,500,0,3,0,1]
r7 = [144, 49, 274, 106, 729, 626, 995, 209, 670, 825, 960, 653, 980, 124, 509, 517, 928, 712, 915, 726, 962, 907, 37, 83, 599, 678, 692, 117, 326, 451, 861, 366, 173, 433, 162, 617, 308, 859, 27, 60, 843, 50, 190, 908, 160, 347, 413, 298, 426, 835, 341, 985, 543, 793, 827, 826, 918, 360, 236, 197, 398, 952, 997, 403, 11, 52, 555, 145, 618, 389, 18, 311, 195, 17, 533, 717, 433, 247, 70, 34, 518, 291, 641, 112, 51, 88, 209, 698, 116, 80, 
947, 734, 176, 467, 144, 323, 521, 95, 757, 877]


def how_much_water(bricks_array: list) -> int:
    result = 0 # waterblocks
    arr_max_pos = []

    while len(arr_max_pos) <= 1:
        arr_max_pos = []

        for i in range(len(bricks_array)):
            if bricks_array[i] == max(bricks_array):
                arr_max_pos.append(i)

        if len(arr_max_pos) > 1:
            for i in range(arr_max_pos[0],arr_max_pos[-1]):
                result += max(bricks_array) - bricks_array[i]
            result += how_much_water(bricks_array[:arr_max_pos[0]+1])
            result += how_much_water(bricks_array[arr_max_pos[-1]:])  
        else:
            bricks_array[arr_max_pos[0]] -= 1
            if len(bricks_array) < 3:
                break

    return result

n = 1000
time_n = time_ns()

for i in range(n):
    how_much_water(r7)

print("took: ", (time_ns() - time_n) / n / 1000,"us / run", sep="")
print("took: ", (time_ns() - time_n) / 1000,"us all in all", sep="")