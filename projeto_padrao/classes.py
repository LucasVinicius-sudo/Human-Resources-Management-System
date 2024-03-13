from abc import ABC, abstractmethod

# Component interface
class EmployeeComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf component representing an individual employee
class Employee(EmployeeComponent):
    def __init__(self, name, job_title , id , age ,salary , working_hours):
        self.name = name
        self.job_title = job_title
        self.id = id
        self.age = age
        self.salary = salary
        self.working_hours = working_hours
        self.insurance_covering = None
        self.pension = None
        self.perfomance = None
        self.claims = None
        self.level = None
    
    def edit_employee(self, new_name):
        self.name = new_name


    def payroll(self, month):#Funtion to implement payroll 
        print("whats the mont of the year in numbers?(1-12)")
        if(month == 12):
            print("The employee will receive"+(2*self.salary))
        elif(month != 12):
            print("The employee will receive"+self.salary)

    


    def display(self):
        print(f"Employee: {self.name}, Job Title: {self.job_title} , ID: {self.id} , Age :{self.age} , Salary: {self.salary} , Working Hours: {self.working_hours} , Perfomance: {self.perfomance} , Insurance Covering: {self.insurance_covering} , Pension: {self.pension}")

# Composite component representing a department
class Department(EmployeeComponent):
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display(self):
        print(f"Department: {self.name}")
        for employee in self.employees:
            employee.display()


