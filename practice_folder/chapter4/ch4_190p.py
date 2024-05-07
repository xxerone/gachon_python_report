//P190 : 수열을 반복 루프를 사용하여서 계산하는 프로그램을 작성하고 테스트하라(while문 + for문)
//1.
divisor = 1.0
divident = 4.0
sum = 0
loop_count = int(input("반복 횟수 : "))
while(loop_count > 0) :
    #sum = sum + divident / divisor
    sum = 3 + divident / ((divisor + 1) * (divisor + 2) * (divisor + 3))
    #print("분모 : " + str(divident) + str(divisor + 1) + str(divisor + 2) + str(divisor + 3))
    divident = -1.0 * divident
    print("divient : " + str(divident))
    divisor = divisor + 2
    print("divisor : " + str(divisor))
    loop_count = loop_count - 1
    print("loop : " + str(loop_count))
    
//print("Pi = %f" % sum)
//설명 : 반복문으로 divisor를 2씩 늘려가며 분모와 분자 표시 후 분수로 표현해 더하고 divident 분자를 -1씩 곱해 부호를 변경한다.

//2.
from decimal import *
getcontext().prec = 300 #300자까지 출력된다

result = Decimal(3.0)
op = 1
n = 2
for n in range(2, 2*300+1, 2):
    result += 4/Decimal(n*(n+1)*(n+2)*op)
    op *= -1

print(result)
