//p188 도전문제: 1부터 100사이의 소수를 구하는 프로그램을 작성하라. (이해하기!)
//1. 
N_PRIMES = 50
number = 2
count = 0

while count < N_PRIMES :
    divisor = 2
    prime = True

    while divisor < number :
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    if prime:
        count += 1
        print(number, end=" ")
    if number >= 100:
        break
    
    number += 1
//설명 : 구해야하는 소수를 N_PRIMES로 둔 후 count보다 작을 때 까지 반복 후 divisor를 늘려가며 나누는 수를 늘리고 만약 나누어진다면 소수가 아니라 이중 반복문 중 하나를 탈출하고 그것이 아니라면 number로 출력하고 number를 하나 더한다.

//2. 
#188
for i in range(2,101):
    isSosu = True
    for j in range(2,i):
        if i%j == 0:
            isSosu = False
            break
    if isSosu == True:
        print(i, end = " ")
