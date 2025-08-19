class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")    
        
e1 = Employee("John", 30)
e1.show_details()
Employee.show_details(e1)        