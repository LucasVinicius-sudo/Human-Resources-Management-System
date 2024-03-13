from classes import Employee

class LeaveManagement(Employee):
    def __init__(self, name, job_title, id, age, salary, working_hours , requests , status):
        super().__init__(name, job_title, id, age, salary, working_hours)
        self.requests = requests
        self.status = status
    

    def manage_requests(self):
        if(self.requests == "Vacation"):
            guarantee = input("The Employee wants a Vacation? ")
            if(guarantee == "Agree"):
                self.status = "Vacation Time"
            elif(guarantee == "Disagree"):
                self.status = "Normal"
        elif(self.requests == "Sick"):
            guarantee = input("The Employee wants for Sickness Leave? ")
            if(guarantee == "Agree"):
                self.status = "Vacation Time"
            elif(guarantee == "Disagree"):
                self.status = "Normal"
        elif(self.requests == "Maternity/Paternity"):
            guarantee = input("The Employee wants a Maternity/Paternity leave? ")
            if(guarantee == "Agree"):
                self.status = "Vacation Time"
            elif(guarantee == "Disagree"):
                self.status = "Normal"
        elif(self.requests == "Bereavment"):
            guarantee = input("The Employee wants a Bereavment time? ")
            if(guarantee == "Agree"):
                self.status = "Vacation Time"
            elif(guarantee == "Disagree"):
                self.status = "Normal"
        elif(self.requests == "Jury"):
            guarantee = input("The Employee wants a Vacation to solve Jury questions? ")
            if(guarantee == "Agree"):
                self.status = "Vacation Time"
            elif(guarantee == "Disagree"):
                self.status = "Normal"
        elif(self.requests == "Military "):
            guarantee = input("The Employee wants a Vacation for Military Obligations? ")
            if(guarantee == "Agree"):
                self.status = "Vacation Time"
            elif(guarantee == "Disagree"):
                self.status = "Normal"

    