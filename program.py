FILENAME = "students.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    if search_by_roll(roll):
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILENAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Student added successfully.")

def view_students():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found.")
                return
            print("\n--- All Students ---")
            for line in lines:
                roll, name, marks = line.strip().split(",")
                print(f"Roll: {roll} | Name: {name} | Marks: {marks}")
    except FileNotFoundError:
        print("No student file found yet.")

def search_by_roll(roll):
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                r, name, marks = line.strip().split(",")
                if r == roll:
                    return {'roll': r, 'name': name, 'marks': marks}
    except FileNotFoundError:
        return None
    return None

def search_student():
    roll = input("Enter Roll Number to search: ")
    student = search_by_roll(roll)
    if student:
        print(f"Roll: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}")
    else:
        print("Student not found.")

def update_student():
    roll = input("Enter Roll Number to update: ")
    updated_lines = []
    found = False

    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            for line in lines:
                r, name, marks = line.strip().split(",")
                if r == roll:
                    new_name = input("Enter new name: ")
                    new_marks = input("Enter new marks: ")
                    updated_lines.append(f"{r},{new_name},{new_marks}\n")
                    found = True
                else:
                    updated_lines.append(line)

        if found:
            with open(FILENAME, "w") as file:
                file.writelines(updated_lines)
            print("Student updated successfully.")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("Student file not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    updated_lines = []
    found = False

    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            for line in lines:
                r, name, marks = line.strip().split(",")
                if r != roll:
                    updated_lines.append(line)
                else:
                    found = True

        if found:
            with open(FILENAME, "w") as file:
                file.writelines(updated_lines)
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    except FileNotFoundError:
        print("Student file not found.")

def menu():
    while True:
        print("\n====== Student Dashboard (Using TXT) ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the dashboard
menu()
