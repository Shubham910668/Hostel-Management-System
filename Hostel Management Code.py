def display_menu():
    print("\nHostel Management System")
    print("1. Add a New Student")
    print("2. Search for a Student")
    print("3. Delete a Student")
    print("4. List All Students")
    print("5. Exit")

def add_student(students):
    name = input("Enter the student's name: ").strip()
    if name in students:
        print(f"Student '{name}' already exists.")
    else:
        phone = input("Enter the student's phone number: ").strip()
        students[name] = phone
        print(f"Student '{name}' added successfully.")

def search_student(students):
    name = input("Enter the name to search: ").strip()
    if name in students:
        print(f"Name: {name}, Phone: {students[name]}")
    else:
        print(f"Student '{name}' not found.")

def delete_student(students):
    name = input("Enter the name to delete: ").strip()
    if name in students:
        del students[name]
        print(f"Student '{name}' deleted successfully.")
    else:
        print(f"Student '{name}' not found.")

def list_students(students):
    if students:
        print("\nList of Students:")
        for name, phone in students.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No students found.")

def main():
    students = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            search_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            list_students(students)
        elif choice == '5':
            print("Exiting the Hostel Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
