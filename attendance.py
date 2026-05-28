students = ["Rahul", "Anjali", "Kiran"]

name = input("Enter student name: ")

if name.capitalize() in students:
    print(name, "is Present")
else:
    print("Student not found")