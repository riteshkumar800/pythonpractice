# from car import Car

# car1=Car("Mustang",2024,"red",False)
# car2=Car("corvette",2025,"blue",True)
# car3=Car("Charger",2026,"yellow",True)

# print(car3.model)
# print(car3.color)
# print(car3.year)
# print(car3.for_sale)
# print(car2.model)


# car1.drive()
# car3.stop()
# car2.describe()


#############################################################################################################################

#class variables

# class Student:
#     class_year=2024
#     num_students=0

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#         Student.num_students+=1




# student1=Student("ritesh", 22)
# student1=Student("ravih", 22)
# student1=Student("rihaan", 32)

# print(f"my graduating class of {Student.class_year} has {Student.num_students}. students")

# print(student1.name)

#############################################################################################################################

# class Animal:
#     def __init__(self,name):
#         self.name=name
#         self.isalive=True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")


# class Dog(Animal):
#     def speak(self):
#         print("bhow!")

# class Cat(Animal):
#     def speak(self):
#         print("meow!")

# class Mouse(Animal):
#     def speak(self):
#         print("squeek!")

# dog = Dog("Scoopy")
# cat= Cat("Garfield")
# mouse=Mouse("mickey")


# print(mouse.name)
# print(mouse.isalive)
# mouse.eat()
# cat.sleep()

# dog.speak()

#############################################################################################################################
#super()
class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled


class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
        














