student_grade = {}

def add_students():
    while True:
        name = input("Enter Student's name: ").capitalize()

        if name == "":
            print("Name can't be empty")
        else:
            break

    while True:
        grade = list(map(int, input("Enter student' grades separated by space: "). split()))
        
        if not grade:
            print("You did not enter anything")
        else:
            break
    
    student_grade[name] = tuple(grade)
    print(f"You added {name} with grades {grade}")



add_students()