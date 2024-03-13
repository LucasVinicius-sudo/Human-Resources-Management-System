import sys
from classes import EmployeeComponent , Employee , Department
from performance import Perfomance
from training import Trainee
from benefits import BenefitsAdmin
from compliance import Right
from leave_managment import LeaveManagement
from attendance import Attendance

def main():
    print("Welcome to the HR System Portal by Lucas Vinicius")
    print("Type Help to see avaliabe commands")

    while True:
        user_input = input("What's you command\n").strip().lower()

        if(user_input == "help"):
            display_help()
        elif(user_input == "create"):
            print("Create a company with the Data of it")
            print("Firts put the data of a Employee")
            name = input("What's the name?")
            job = input("What's the Job?")
            id = input("What's the Id?")
            age = int(input("What's the Age?"))
            salary = input("What's the salary?")
            working_hours = input("What's the Working Hours?")
            employee1 = Employee(name,job,id,age,salary,working_hours)

            it_department = Department("IT Department")
            it_department.add_employee(employee1)
            
            company = Department("Software House")
            company.add_employee(it_department)

        elif(user_input == "view"):
            company.display()
        elif(user_input == "edit"):
            new_name = input("What's the new name:")
            employee1.edit_employee(new_name)#Ok just implemented new def to edit the self things(name, age and ETV)
        elif(user_input == "attendance"):
            employee1_attendance = Attendance(employee1.name, employee1.job_title , employee1.id , employee1.age , employee1.salary , employee1.working_hours)
            employee1_attendance.manage_presence()
        elif(user_input == "payroll"):
            month = input("Type the month of the payroll of the Employee").strip().lower()
            num_month = 0
            if(month == "January"):#January, February, March, April, May, June, July, August, September, October, November, and December
                num_month = 1
            elif(month == "February"):
                num_month = 2
            elif(month == "March"):
                num_month = 3
            elif(month == "April"):
                num_month = 4
            elif(month == "May"):
                num_month = 5
            elif(month == "June"):
                num_month = 6
            elif(month == "July"):
                num_month = 7
            elif(month == "August"):
                num_month = 8
            elif(month == "September"):
                num_month = 9
            elif(month == "October"):
                num_month = 10
            elif(month == "November"):
                num_month = 11
            elif(month == "December"):
                num_month = 12
            employee1.payroll(num_month)
        elif(user_input == "portal"):
            print("If you are a Employee you can edit your documentation in the portal.py")
        elif(user_input == "perfomance"):
            Perfomance.evaluation(employee1,Employee)
        elif(user_input == "leave"):
            requests = input("What's the request of the Employee(Vacation - Sick - Military - Jury - )")
            status = "Working"
            employee1_leave_management = LeaveManagement(employee1.name, employee1.job_title , employee1.id , employee1.age , employee1.salary , employee1.working_hours ,requests , status)
            employee1_leave_management.manage_requests()
        elif(user_input == "trainning"):
            print("Enter training details:")
            topic = input("Topic: ")
            date = input("Date: ")
            duration = input("Duration ?")
            location = input("Location?")
            trainer = input("type of Trainning?")

            employee1_training = Trainee(employee1.name ,employee1.job_title, employee1.id, employee1.age , employee1.salary , employee1.working_hours ,topic , date , duration , location , trainer)
            employee1.display()
            employee1_training.display_details()
        elif(user_input == "compliance"):
            text = input("The Summary of the Employee Compliance")
            employee1_compliance = Right(employee1.name, employee1.job_title , employee1.id , employee1.age , employee1.salary , employee1.working_hours , text)
            employee1_compliance.display_compliance()
        elif(user_input == "benefits"):
            BenefitsAdmin.manage(employee1,Employee)
        elif(user_input == "exit"):
            print("Exiting the HR System Portal")
            break
        else:
            print("Type help for see the avaliabe commands")


        
    
def display_help():
    print("Type : 'create', to create a company in the system")#Done
    print("Type : 'view' , to see information about Company,Department and Employee")#Done
    print("Type : 'edit' , to edit information about Company,Department and Employee")#Parcial-Done
    print("Type : 'attendance' , to recording and  analyzing  employee  attendance  and  working hours ")#Parcial
    print("Type : 'payroll ', to calculate the payroll of the employee")#Done
    print("Type : 'benefits' ,to create or edit employee benefits like insurance and pensions ")#Done
    print("Type : 'portal' and go to other file ,if you are a employee and Want to managing your only information")#not Implemented
    print("Type : 'perfomance' , to tracking and evaluating employee performance")#Done
    print("Type : 'leave managment',to handling employee leave requests and balances")#Done
    print("Type : 'trainning' , to organizing and tracking employee training sessions;")#Done
    print("Type : 'compliance', to see the compliance rules of our company")#Done
    print("Type : 'exit' , to stop the terminal")#Done
    

if __name__ == "__main__" :
    main()

