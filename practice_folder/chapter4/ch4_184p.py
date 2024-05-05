import random
i = 0
k = 0
while (i < 1000):
    rand1 = random.randint(1,6)
    print("rand1 = " + str(rand1))
    rand2 = random.randint(1,6)
    print("rand2 = " + str(rand2))
    if(rand1 + rand2 == 6) :
        k = k + 1
        print("k = " + str(k))
    i+=1
print(str(k) + " / 1000")
