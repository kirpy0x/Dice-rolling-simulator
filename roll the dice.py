rolls = 0
while rolls != 1 and rolls != 2:
    rolls = int(input("1 die or 2? : "))

    import random
    if rolls == 1:
        num = random.randint(1,6)
    elif rolls == 2:
        num = random.randint(1,6)*2
    else:
        print("only two dice available")
        
    print(num)
    rolls = 0
