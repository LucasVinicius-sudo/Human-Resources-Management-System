from classes import Employee
class BenefitsAdmin:
    

    def manage(obj , Employee):
        if not isinstance(obj , Employee):
           raise TypeError("Object must be an instance of Employee")
        try:
            if(obj.age < 30 ):
                obj.insurance_covering = "Basic"
                obj.pension = "35%"
            elif (obj.age >= 30 and obj.age < 60):
                obj.insurance_covering = "Medium"
                obj.pension = "50%"
            else :
                obj.insurance_covering = "High"
                obj.pension = "100%"
           
            
        except ValueError:
           print("Invalid")
      