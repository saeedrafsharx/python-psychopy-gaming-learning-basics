import random
slot1 = random.randint(1,5)
slot2 = random.randint(1,5)
slot3 = random.randint(1,5)
print("The numbers are %d,%d,and %d."%(slot1,slot2,slot3))
if slot1 == slot2 == slot3:
    print("Three of a kind!")
else:
    if slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        print("Paaareeeee!!")
    elif not slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        print("Meh...")