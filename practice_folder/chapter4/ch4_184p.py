//p184 - 2개를 주사위를 던져서 6이 나올 확률은 5/36이다. 1000번 가상적인 주사위를 던진 후에 6이 나오는 횟수를 세어서 이론적인 확률값과 비교하는 프로그램을 작성해보자
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
//설명 : random 라이브러리 import 후 0~999까지 반복 후 주사위 눈을 randint로 rand난수를 생성 후 주사위 눈 2개를 더했을 때 6이 나오는 경우의 수를 1000번 반복한거로 횟수를 세는걸 i로 한다.
