class ManagementApp:
    def __init__(self):
        self.employee_db = EmployeeDatabase()

    def run(self):
        while True:
            print("\n1. Add Employee\n2. Remove Employee\n3. Display Employees\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter employee name: ")
                employee_id = input("Enter employee ID: ")
                department = input("Enter department: ")
                emp = Manager(name, employee_id, department)
                self.employee_db.add_employee(emp)
                print("Employee added successfully!")

            elif choice == '2':
                employee_id = input("Enter employee ID to remove: ")
                self.employee_db.remove_employee(employee_id)
                print("Employee removed successfully!")

            elif choice == '3':
                self.employee_db.display_employees()

            elif choice == '4':
                break

            else:
                print("Invalid choice. Please try again.")
