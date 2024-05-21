#직접 타자 안침 주의!! / 슬라이드 21 / 519p lambda1.py

class MyCounter(object):
 # 생성자 메소드를 정의한다. 
 def __init__(self, low, high):
 self.current = low
 self.high = high
 # 이터레이터 객체로서 자신을 반환한다. 
 def __iter__(self):
 return self
 def __next__(self):
 # current가 high 보다 크면 StopIteration 예외를 발생한다.
 # current가 high 보다 작으면 다음 값을 반환한다. 
 if self.current > self.high:
 raise StopIteration
 else:
 self.current += 1
 return self.current - 1
