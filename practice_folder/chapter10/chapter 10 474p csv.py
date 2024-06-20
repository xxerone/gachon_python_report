#chapter 10 474p csv.py

import csv

f = open('weather.csv')
data = csv.reader(f) #csv 파일 전체 읽음
header = next(data) #헤더 부분 안읽기 위함
temp = 0 #1000이였던건 제일 첫줄 시행 위함 (이렇게하면 temp가 무조건 바뀜) / 
for row in data:
    if temp < float(row[3]):
        temp = float(row[3]) # 최저 기온 중 가장 높은거 / -> : row
print("the hottest weather :", temp, ".")

f.close()

# 강의 안본거 확인하고 시험계획에 쓰고 계획짜기(안본건 이번주에 볼 예정)
