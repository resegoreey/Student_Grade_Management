student_grade = {}

def add_students():
    while True:
        name = input("Enter Student's name: ").capitalize()

        if name == "":
            print("Name can't be empty")
        else:
            break

    while True:
        grades = list(map(int, input("Enter student' grades separated by space: "). split()))
        
        if not grades:
            print("You did not enter anything")
        else:
            break
    
    if name in student_grade:
        print(f"{name} already exists")
    else:
        student_grade[name] = tuple(grades)
        print(f"You added {name} with grades {grades}")

#add_students()


def update_grades():
    name = input("Enter student name: ").capitalize()
    new_grades = list(map(int, input("Enter new grades separated by space: "). split()))

    if name in student_grade:
        student_grade[name] = tuple(new_grades)
        print(f"You updated {name}'s grades to {new_grades}")
    else:
        print(f"{name} not found")
#update_grades()

def remove_student():
    name = input("Enter student name to remove: ").capitalize()

    if name in student_grade:
        del student_grade[name]
        print(f"You removed {name}")
    else:
        print(f"{name} not found")

def display_students():
    if not student_grade:
        print("No students in record")
        return
    for student, grades in student_grade.items():
        print(f"""Name: {student}
        Grades: {grades}""")


def statistics():
    all_grades = []
    for grades in student_grade.values():
        for grade in grades:
            all_grades.append(grade)
    
    if not all_grades:
        print("Student records empty, can't calculate statistics")
    else:
        average = sum(all_grades) / len(all_grades)
        highest_mark = max(all_grades)
        lowest_mark = min(all_grades)
        print(f"""Average: {round(average, 2)}
Highest Mark: {highest_mark}
Lowest Mark: {lowest_mark}""")


while True:
    print("""What would you like to do?
          1. Add Student
          2. Update Grades
          3. Remove student
          4. Display students
          5. Stats
          6. Exit""")
    
    choice = input("Enter choice(1-6): ")
    if choice == "1":
        add_students()
    elif choice == "2":
        update_grades()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        statistics()
    elif choice == "6":
        print("Exiting the program, Bye!")
        break
    else:
        print("Make a valid choice from 1 to 6")