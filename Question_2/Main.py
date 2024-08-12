import sys

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = {}

    def enroll_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None
            print(f"Enrolled in {course_name} successfully.")
        else:
            print(f"Already enrolled in {course_name}")

    def add_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Grade added for {course_name} successfully.")
        else:
            print(f"Not enrolled in {course_name}")

    def calculate_gpa(self):
        total_grades = sum(grade for grade in self.courses.values() if grade is not None)
        num_courses = len([grade for grade in self.courses.values() if grade is not None])
        return total_grades / num_courses if num_courses > 0 else 0.0

    def display_student_info(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Courses and Grades:")
        for course, grade in self.courses.items():
            print(f"  {course}: {grade}")
        print(f"GPA: {self.calculate_gpa()}\n")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            print("Student ID already exists.")
            return
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        self.students[student_id] = Student(student_id, name, age)
        print("Student added successfully.")

    def enroll_student_in_course(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            course_name = input("Enter course name: ")
            self.students[student_id].enroll_course(course_name)
        else:
            print("Student ID not found.")

    def add_student_grade(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            self.students[student_id].add_grade(course_name, grade)
        else:
            print("Student ID not found.")

    def display_all_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students.values():
                student.display_student_info()

    def save_data(self):
        filename = input("Enter filename to save data: ")
        with open(filename, 'w') as file:
            for student_id, student in self.students.items():
                file.write(f"{student_id},{student.name},{student.age},{student.courses}\n")
        print("Data saved successfully.")

    def load_data(self):
        filename = input("Enter filename to load data: ")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    student_id, name, age, courses = line.strip().split(',', 3)
                    student = Student(student_id, name, int(age))
                    student.courses = eval(courses)  # Convert string back to dict
                    self.students[student_id] = student
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

    def menu(self):
        while True:
            print("\nStudent Management System Menu")
            print("1. Add New Student")
            print("2. Enroll Student in Course")
            print("3. Add Student Grade")
            print("4. Display All Students")
            print("5. Save Data")
            print("6. Load Data")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.enroll_student_in_course()
            elif choice == "3":
                self.add_student_grade()
            elif choice == "4":
                self.display_all_students()
            elif choice == "5":
                self.save_data()
            elif choice == "6":
                self.load_data()
            elif choice == "7":
                print("Exiting the system. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.menu()
