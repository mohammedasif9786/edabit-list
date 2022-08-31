def get_container(stuff):
    container = None
    if stuff == "bread":
        container = "bag"
    elif stuff == "chai":
        container = "bottle"
    elif stuff == "candy":
        container = "plastic"
    return container
print(get_container("bread"))
print(get_container("chai"))
print(get_container("candy"))
print(get_container("cheese"))

