def hurdle(hurdle_height , jumpers_height):
    h_1 = hurdle_height
    h_2 = int(max(list(h_1)))
    j_1 = jumpers_height
    if h_2 >= j_1 :
        return True
    return False
print(hurdle([1,2,3,4],6))






