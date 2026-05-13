print("===== STUDENT MANAGEMENT SYSTEM =====")

students = {}

name = input("Enter student name: ")
marks = input("Enter student marks: ")

students[name] = marks

print("\nStudent Records")

for key, value in students.items():
    print(key, ":", value)