#영준이형 코드!!
#p194 도전문제: 도박사 문제에서 돈을 딸 확룰을 20%로 수정하여 프로그램을 작성하라.

import random

initial_money = 50  #시작 달러
goal = 250  #목표 달러
wins = 0    #성공 횟수
cash = initial_money    #보유 달러를 시작 달러로 초기화한다.

for i in range(100):
    if 0 < cash < goal:
        number = random.randint(1,5)    #1부터 5까지의 랜덤 숫자를 저장하여 확률을 20%로 맞춘다.
        if number == 1:
            cash = cash+1   #1$ 벌음
            wins = wins+1   #승리수 1 추가
        else:
            cash = cash-1   #1$ 잃음
        if cash == goal:    #목표 금액과 보유 금액이 같아지면 멈춘다.
            break
    else:   #cash가 0이 되면 도박사 프로그램 나가기
        print("%d번째에 몽땅 다 잃었어요 8ㅅ8" % (i+1))
        break

#책에 코드가 이상하게 짜여있어요…
print("초기 금액 $%d" % initial_money)
print("목표 금액 $%d" % goal)
print("보유 금액 $%d" % cash)
print("%d/100번 중에서 %d번 성공" % (i+1, wins))
#설명 : 반복문을 통해 100번 반복하고 돈을 다 잃거나 목표 금액이 다 될때까지 계속 반복하여 randint를 통해 난수를 뽑고 0부터 4까지 난수 중 하나를 뽑아 1이 나오면 20퍼 확률이므로 이 때 돈이 추가되고 돈이 목표가 된다면 승리 횟수를 채운다. 
