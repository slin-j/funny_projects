import time

def get_pascals_triangle_row(row_number: int) -> list:
    lst = [1]

    for _ in range(row_number):
        lst.append(1)   # new row is longer by 1 than before
        # no calculation needed for row 0 and 1
        if len(lst) > 2:
            old_lst = lst[:-1]
            # calculate the values for for all positions except the outer ones
            for i in range(1,len(lst) - 1):
                lst[i] = old_lst[i] + old_lst[i - 1]

    return lst

time_start = time.time()

for i in range(500):
    print(get_pascals_triangle_row(i))

print("=======================================")
print("Took: ", time.time()-time_start)

