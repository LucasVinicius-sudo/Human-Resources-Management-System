from classes import Employee

class Trainee(Employee):
    def __init__(self ,name , job_title , id , age , salary , working_hours, topic, date, duration, location, trainer):
        super().__init__( name, job_title , id , age ,salary , working_hours)
        self.topic = topic
        self.date = date 
        self.duration = duration
        self.location = location
        self.trainer = trainer
        
    
   

    def display_details(self):
        print("Training Topic:", self.topic)
        print("Date:", self.date)
        print("Duration:", self.duration, "hours")
        print("Location:", self.location)
        print("Trainer:", self.trainer)
        
        