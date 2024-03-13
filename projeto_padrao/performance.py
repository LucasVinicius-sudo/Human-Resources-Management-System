from classes import Employee

class Perfomance:
    
    def evaluation(obj , Employee):
        if not isinstance(obj , Employee):
            raise TypeError("Object must be an instance of MyClass")
        try:
            score = int(input("What score do you rate the employee?"))
            if(score == 1):
                obj.perfomance = "Low"
            elif(score == 2):
                obj.perfomance = "Medium"
            elif(score == 3):
                obj.perfomance = "High"
            else:
                print("Invalid Score")
                return False
            return True
        except ValueError :
            print("Invalid Input. Please Enter a number")
            return False
        