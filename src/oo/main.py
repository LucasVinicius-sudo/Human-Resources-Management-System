import sys

class Employee:
    def __init__(self,id,name,birth,gender,contact_info,departament,position,hours,avaliation,salary):
        self.id = id
        self.name = name
        self.birth = birth
        self.gender = gender
        self.contact_info = contact_info
        self.departament = departament
        self.position = position
        self.hours = hours
        self.avaliation = avaliation
        self.salary = salary

    def display(self):
        print(f"Employee ID: {self.id}")
        print(f"name: {self.name}")
        print(f"Date of Birth: {self.birth}")
        print(f"Gender: {self.gender}")
        print(f"contact: {self.contact_info}")
        print(f"Departament: {self.departament}")
        print(f"Position: {self.position}")
        print(f"Hours of Working: {self.hours}")
        print(f"The Avalation Number(0-10): {self.avaliation}")
        print(f"Salary: {self.salary}")
    
    def attendance(self):
        presence = int(input("0-Absent , 1-Presence"))
        if(presence == 0):
            print("Employee is Absent in this day")
        else:
            print("Employee is Present this day")

        print(f"The Employee Works {self.hours} per week")

    
    def payroll(self):
        month = int(input("What's the month of Year(1-12):"))
        if(month != 12):
            print(f"The employee will receive {self.salary} in this month")
        else:
            self.salary = self.salary * 2
            print(f"The employee will receive {self.salary} in this month")
    
    def perfomance(self):
        comments = input("Do you have any comentary of the perfomance of the Employee?")
        print(f"The perfomance of the employee is {self.perfomance}")
        print(comments)
    
    def compliance(self):
        compliance = input("Do you have any recommendations about compliance , regulamentation and other things?")
        print(compliance)

    def requests(self):
        solicitation = input("Do you have any solicitaion?")
        print(solicitation)


class HRSystem:
    def __init__(self):
        self.employees = []
    
    def add_employee(self,employee):#Criando um funcionário
        self.employees.append(employee)
    
    def display_all_profiles(self):#Display de todos os Funcionários
        for employee in self.employees:
            employee.display()
    


hr_system = HRSystem()

employee1 = Employee(1, "Lucas Vinicius", "2000-12-05", "Male", "123-456-7890", "IT", "Developer",36, 8 , 60000)
employee2 = Employee(2, "Gustavo Gomez", "1994-11-04", "Male","987-654-3210", "HR", "Manager",44, 8, 80000)
employee3 = Employee(3, "Brucer", "1999-05-12", "Male", "1920-0210" ,"IT" ,"Manager" ,44, 10 , 200000)
employee1.payroll()#Payroll Processing
employee1.attendance()#Attendance 
employee1.perfomance()#Performance evaluation
employee1.compliance()#Compliance
employee1.requests()#Leave Management



hr_system.add_employee(employee1)
#hr_system.add_employee(employee2)
#hr_system.add_employee(employee3)
    
hr_system.display_all_profiles()
