from classes import Employee

class Attendance(Employee):
    def __init__(self, name, job_title, id, age, salary, working_hours , presence=None):
        super().__init__(name, job_title, id, age, salary, working_hours)
        
    
    def manage_presence(self):
        question = input("What's the Presence of the Employee?")
        if(question == "Present"):
            self.presence = "Present"
        elif(question == "Absent"):
            self.presence = "Absent"
    
   

