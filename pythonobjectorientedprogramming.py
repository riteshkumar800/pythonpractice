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
# class Shape:
#     def __init__(self,color,is_filled):
#         self.color=color
#         self.is_filled=is_filled

#     def describe(self):
#         print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")




# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         super().__init__(color,is_filled)
#         self.radius=radius

#     def describe(self):
#         print(f"it is a ircle with an area of {3.14*self.radius*self.radius}m^2")
#         super().describe()

        
# class Square(Shape):
#     def __init__(self,color,is_filled,width):
#         super().__init__(color,is_filled)
#         self.width=width
# class Triangle(Shape):
#     def __init__(self,color,is_filled,width,height):
#         super().__init__(color,is_filled)
#         self.width=width
#         self.height=height


# circle=Circle(color="red",is_filled=True,radius=2)
# square=Square("blue",False,6)

# print(square.width)
# # square.describe()
# circle.describe()

#############################################################################################################################
##POLYMORPHISM
# from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius**2
    


# class Square(Shape):
#     def __init__(self,side):
#         self.side=side

#     def area(self):
#         return self.side**2
    


# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height

#     def area(self):
#         return self.base*self.height*0.5
    

# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         self.topping=topping
#         self.radius=radius



# shapes=[Circle(4),Square(5),Triangle(10,8),Pizza("perponi",15)]

# for shape in shapes:
#     print(f"{shape.area()}cm^2")

#############################################################################################################################
##STATIC METHOD

# class Employee:

#     def __init__(self,name,position):
#         self.name=name
#         self.position=position

#     def get_info(self):
#         return f"{self.name}={self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions=["manager", "cashier", "cook","janitor"]

#         return position in valid_positions
    


# employee1=Employee("ritesh","manager")
# employee2=Employee("riteshaa","cook")
# employee1=Employee("rit","cook")


# print(Employee.is_valid_position("Rocket Scientist"))
# print(employee1.get_info())

#############################################################################################################################

##CLASS METHOD

# class Student:

#     count=0
#     total_gpa=0

#     def __init__(self,name,gpa):
#         self.name=name
#         self.gpa=gpa

#         Student.count+=1
#         Student.total_gpa+=gpa

#     #INSTANCE METHOD

#     def get_info(self):
#         return "{self.name} {self.gpa}"
    

#     @classmethod
#     def get_count(cls):
#         return cls.count
    
#     @classmethod
#     def get_avg_gpa(cls):
#         if cls.count==0:
#             return 0

#         else:
#             return f"Average gpa: {cls.total_gpa/cls.count:.2f}" 
        
# student1=Student("spongebob",3.0)
# student2=Student("patric",1.0)
# student3=Student("sandy",5.0)

# print(Student.get_count())
# print(Student.get_avg_gpa())


        


        
























