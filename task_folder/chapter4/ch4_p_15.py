#15번 – 다음 수열의 합을 계산하는 프로그램을 작성하라
n = i = b = 0
for i in range (1,10):
    n = i
    a = (2*n-1) / (2*n+1)
    b = a
    c = a + b
설명 : n,I,b를 전역변수로 선언하고 i를 반복문으로 사용한다. 1부터 9까지 반복 후 n을 i랑 같게 두고 a를 1,3,5 등 홀수로 가므로 2n-1, 2n+1로 둔다. 이 때 그냥 놔두면 초기화 되므로 b에 옮기고 새로운 변수 c를 선언해 2개를 더한다.