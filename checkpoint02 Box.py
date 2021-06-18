import math

def boxneed(items,itemsBox):
    return math.ceil(items/itemsBox)


items = int(input("Enter The Number of Items "))
itemsBox = int(input("Enter the Number of Items per Box: "))

print(boxneed(items,itemsBox))