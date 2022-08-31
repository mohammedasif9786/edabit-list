def jackpot(j_1 , j_2 ,j_3 , j_4):
    if j_1 == "@" and j_2 == "@" and j_3 == "@" and j_4 == "@":
        return True
    if j_1 == "abc" and j_2 == "abc" and j_3 == "abc" and j_4 == "abc":
        return True
    if j_1 == "SS" and j_2 == "SS" and j_3 == "SS" and j_4 == "SS":
        return True
    return False
print(jackpot("ssc","abc","abc","abc"))
