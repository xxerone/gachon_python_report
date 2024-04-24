#14번 – 2와 20 사이에 있는 모든 소수를 찾는 프로그램을 찾는 프로그램을 작성하라.
N_PRIMES = 8 #찾아야하는 소수 개수
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
