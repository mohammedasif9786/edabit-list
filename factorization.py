def factorization(factor):
    f_1 = factor
    f_l = []
    for i in range(1 , f_1+1):
        if f_1 % i == 0:
            f_l.append(i)
    print(f_l)

(factorization(45))








