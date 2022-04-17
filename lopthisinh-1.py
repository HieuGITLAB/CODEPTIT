# class Student():
#     def __init__(self, name, dob, mark1, mark2, mark3):
#         self.name = name
#         self.dob = dob
#         self.mark1 = mark1
#         self.mark2 = mark1
#         self.mark3 = mark3
#         self.sum = mark1 + mark2 + mark3
#
# ten = input()
# ngaysinh = input()
# diem1 = float(input())
# diem2 = float(input())
# diem3 = float(input())
# s1 = Student(ten, ngaysinh, diem1, diem2, diem3)
# tongdiem = "%.1f"%s1.sum
# print(f"{s1.name} {s1.dob} {tongdiem} ")

def making(*topping):
    print(*topping)
making("pizza", "hambuger")