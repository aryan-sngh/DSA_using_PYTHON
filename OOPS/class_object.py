#example 1
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"{self.name},{self.age}")
        
# #creating an object 
# person1 = Person(name="alice",age=30)
# person1.greet()
    
    
#example 2 encapsulation
# class Computer:
#     def __init__(self):
#         self.__max_price=900
#     def sell(self):
#         print(f"selling price:{self.__max_price}")
        
#     def set_max_price(self,price):
#         self.__max_price=price

# #creating object
# c = Computer()
# c.sell()

# #attempt to change price directly
# c.__max_price = 1000
# c.sell()

# #change the price using setter
# c.set_max_price(1000)
# c.sell()


#example 3 inheritance
# class Animal:
#     def eat(self):
#         print("i can eat")
#     def sleep(self):
#         print("i can sleep")
        
# class Dog(Animal):
#     def bark(self):
#         print("i ca  bark! woof woof!!")
        
# dog1 = Dog()
# dog1.eat()
# dog1.sleep()
# dog1.bark()