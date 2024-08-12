import sys
from employee import Employee


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        employee_id = input("Enter employee ID: ")
        if employee_id in self.employees:
            print("Employee ID already exists.")
            return
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        job_title = input("Enter job title: ")
        salary = float(input("Enter salary: "))
        self.employees[employee_id] = Employee(employee_id, name, age, job_title, salary)
        print("Employee added successfully.")

    def update_employee_job(self):
        employee_id = input("Enter employee ID: ")
        if employee_id in self.employees:
            new_job_title = input("Enter new job title: ")
            new_salary = float(input("Enter new salary: "))
            self.employees[employee_id].update_job(new_job_title, new_salary)
        else:
            print("Employee ID not found.")

    def add_performance_metric(self):
        employee_id = input("Enter employee ID: ")
        if employee_id in self.employees:
            metric = float(input("Enter performance metric (0-10): "))
            self.employees[employee_id].add_performance_metric(metric)
        else:
            print("Employee ID not found.")

    def display_all_employees(self):
        if not self.employees:
            print("No employees available.")
        else:
            for employee in self.employees.values():
                employee.display_employee_info()

    def save_data(self):
        filename = input("Enter filename to save data: ")
        with open(filename, 'w') as file:
            for employee_id, employee in self.employees.items():
                file.write(
                    f"{employee_id},{employee.name},{employee.age},{employee.job_title},{employee.salary},{employee.performance_metrics}\n")
        print("Data saved successfully.")

    def load_data(self):
        filename = input("Enter filename to load data: ")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    employee_id, name, age, job_title, salary, performance_metrics = line.strip().split(',', 5)
                    employee = Employee(employee_id, name, int(age), job_title, float(salary))
                    employee.performance_metrics = eval(performance_metrics)  # Convert string back to list
                    self.employees[employee_id] = employee
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

    def menu(self):
        while True:
            print("\nEmployee Management System Menu")
            print("1. Add New Employee")
            print("2. Update Employee Job")
            print("3. Add Performance Metric")
            print("4. Display All Employees")
            print("5. Save Data")
            print("6. Load Data")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.update_employee_job()
            elif choice == "3":
                self.add_performance_metric()
            elif choice == "4":
                self.display_all_employees()
            elif choice == "5":
                self.save_data()
            elif choice == "6":
                self.load_data()
            elif choice == "7":
                print("Exiting the system. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
