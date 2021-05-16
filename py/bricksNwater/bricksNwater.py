def how_much_water(bricks_array: list) -> int:
    result = 0
    calc_vol = []
    #bricks_array = [5,4,3,1,0,0,5]
    print(bricks_array)
    print("len",len(bricks_array))
    i = 0

    while i < len(bricks_array):
        start_height = bricks_array[i]
        max_height = 0
        min_height = -1
        is_height_reached = False
        calc_vol = []
        print("startheight:",start_height, "at i =",i)
        i += 1

        while i < len(bricks_array) and start_height > bricks_array[i]:
            if i + 1 == len(bricks_array):
                pass
            else:
                if start_height <= bricks_array[i+1]:
                    is_height_reached = True
                if bricks_array[i] > max_height:
                    max_height = bricks_array[i]
                if bricks_array[i] < min_height:
                    min_height = bricks_array[i]

            print("br",bricks_array[i],"at i =", i)

            calc_vol.append(start_height - bricks_array[i])
            

            i += 1
            #if i != len(bricks_array) and (bricks_array[i] > max_height):
            #    max_height = bricks_array[i]
            


        print("`???????????????????????????????final i:",i,is_height_reached,"arr=",calc_vol,"max=",max_height)
        if is_height_reached:
            for v in calc_vol:
                margin = start_height - max_height
                print("marg:",margin)
                result += v
                if margin > 0:
                    pass
                    #result -= margin
                print("zwischenres:",result)

        else:
            for v in calc_vol:
                if bricks_array[-1] != 0:
                    margin = start_height - bricks_array[-1]
                else:
                    break
                print("marg:",margin)
                result += v
                if margin > 0:
                    result -= margin
                print("zwischenres:",result)


    return result            
        

print("Function returned: ", how_much_water([0, 3, 2, 4, 0, 2, 0, 4, 2, 0]))