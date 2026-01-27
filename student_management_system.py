# Student Management System
# Beginner Python Mini Project

students = {}

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))
    students[sid] = {"name": name, "marks": marks}
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    for sid, data in students.items():
        print(f"ID: {sid}, Name: {data['name']}, Marks: {data['marks']}")
    print()

def search_student():
    sid = input("Enter Student ID to search: ")
    if sid in students:
        s = students[sid]
        print(f"Found → Name: {s['name']}, Marks: {s['marks']}\n")
    else:
        print("Student not found.\n")

def average_marks():
    if not students:
        print("No students to calculate average.\n")
        return
    avg = sum(s["marks"] for s in students.values()) / len(students)
    print(f"Average Marks: {avg:.2f}\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Average Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        average_marks()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice\n")
