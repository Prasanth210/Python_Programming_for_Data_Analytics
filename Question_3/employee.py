
class Employee:
    def __init__(self, employee_id, name, age, job_title, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.job_title = job_title
        self.salary = salary
        self.performance_metrics = []

    def update_job(self, new_job_title, new_salary):
        self.job_title = new_job_title
        self.salary = new_salary
        print(f"Job updated to {new_job_title} with salary {new_salary}.")

    def add_performance_metric(self, metric):
        self.performance_metrics.append(metric)
        print(f"Performance metric added: {metric}.")

    def calculate_bonus(self):
        average_performance = sum(self.performance_metrics) / len(
            self.performance_metrics) if self.performance_metrics else 0
        bonus = 0.1 * self.salary if average_performance >= 7 else 0.05 * self.salary
        return bonus

    def display_employee_info(self):
        print(f"\nEmployee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Job Title: {self.job_title}")
        print(f"Salary: {self.salary}")
        print(f"Performance Metrics: {self.performance_metrics}")
        print(f"Bonus: {self.calculate_bonus()}\n")
