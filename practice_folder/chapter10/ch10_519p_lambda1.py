#직접 타자 안침 주의!! / 슬라이드 21 / 519p lambda1.py

class Student:
        def __init__(self, name, grade, number):
                self.name = name
                self.grade = grade
                self.number = number
        def __repr__(self):
                return repr((self.name, self.grade, self.number))
 students = [
        Student('홍길동', 3.9, 20160303),
        Student('김철수', 3.0, 20160302),
        Student('최자영', 4.3, 20160301),
 ]
 print(sorted(students, key=lambda student: student.number)  
