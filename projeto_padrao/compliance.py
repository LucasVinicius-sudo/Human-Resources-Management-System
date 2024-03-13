from classes import Employee

class Right(Employee):

    def __init__(self, name,job_title, id, age, salary, working_hours,text):
        super().__init__(name, job_title , id , age ,salary , working_hours)
        print("At this Company, we are committed to upholding the highest standards of ethical behavior, legal compliance, and workplace integrity. Our HR System ensures that all employees, managers, and stakeholders adhere to applicable laws, regulations, and company policies.")
        print("1ª Equal Employment Opportunity (EEO)")
        print("2º Labor Laws and Regulations")
        print("3º Safety and Workplace Environment")
        print("4º Confidentiality and Data Privacy")
        print("5º Ethical Conduct and Business Integrity")
        print("6º Training and Awareness")
        print("Do you have any problem with our compliance or Reporting , type below")
        self.text = text
    
    def display_compliance(self):
        print(f"The compliance of the Employee is {self.text}")


   
    