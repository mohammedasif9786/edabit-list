def yesno(name , num):
    v = name
    if num == 1:
        return "hello " + v.upper()
    return "bye " + v.upper()
print(yesno("alon" , 1))
print(yesno("tom" , 0))
print(yesno("jose" , 1))
