# Parent class for all employes
class Employee:
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age

    # this function print employee info
    def display_info(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Age:", self.age)

    # this will be override in child class
    def calculate_salary(self):
        return 0


# Parent class
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, age, monthly_salary):
        super().__init__(emp_id, name, age)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Part time employee
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, age, hourly_rate, hours_worked):
        super().__init__(emp_id, name, age)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # salary = rate * hours
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Frelancer cass
class Freelancer(Employee):
    def __init__(self, emp_id, name, age, project_rate, completed_projects):
        super().__init__(emp_id, name, age)
        self.project_rate = project_rate
        self.completed_projects = completed_projects

    def calculate_salary(self):
        return self.project_rate * self.completed_projects


# creating some employee object
employees = []

employees.append(FullTimeEmployee(1, "Ali", 30, 5000))
employees.append(PartTimeEmployee(2, "Sara", 22, 20, 80))
employees.append(Freelancer(3, "Omar", 27, 1200, 4))


total_salary = 0
max_salary = 0
top_employee = None

#loop
for emp in employees:
    emp.display_info()

    salary = emp.calculate_salary()
    print("Salary:", salary)
    print("--------------------")

    total_salary += salary

    # check if this is the heighest salary
    if salary > max_salary:
        max_salary = salary
        top_employee = emp


# report
print("\nEmployee Report")
print("Total Employees:", len(employees))
print("Total Salary:", total_salary)
print("Highest Salary Employee:", top_employee.name)
print("Highest Salary:", max_salary)
