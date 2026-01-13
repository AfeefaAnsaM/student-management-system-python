from database import create_table
from student import Student

# Step 1: Create table if it doesn't exist
create_table()

while True:
    # Step 2: Show menu
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    # Step 3: Take user choice
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Step 4: Get student details from user
        id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = int(input("Enter Year: "))
        Student.add_student(id, name, branch, year)
        print("✅ Student added successfully!")

    elif choice == '2':
        students = Student.view_students()
        if students:
            print("\nID | Name | Branch | Year")
            print("----------------------------")
            for s in students:
                print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]}")
        else:
            print("No students found.")

    elif choice == '3':
        id = int(input("Enter Student ID to delete: "))
        Student.delete_student(id)
        print("✅ Student deleted successfully!")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter 1-4.")
