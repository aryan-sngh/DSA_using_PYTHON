#example 1
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"{self.name},{self.age}")
        
#creating an object 
person1 = Person(name="alice",age=30)
person1.greet()
    