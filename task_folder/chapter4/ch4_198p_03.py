
#p198 3번 – 1부터 100사이의 모든 3의 배수의 합을 계산하여 출력하는 프로그램을 반복 구조를 사용하여 작성하라. 
b = 0
for i in range(1,101):
    if(i % 3 == 0):
        b = i + b
print(b)
설명 : b를 전역변수로 초기화하고 1부터 100까지 반복 후 i를 3으로 나눌 때 나머지가 없다면 i에 b를 더한 것을 b에 저장해 합을 구하는 방식

