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

#############################################################################################################################
##MAGIC METHODS

# class Book:


#     def __init__(self,title,author,num_pages):
#         self.title=title
#         self.author=author
#         self.num_pages=num_pages

    
#     def __str__(self):
#         return f"{self.title} by {self.author}"
    

#     def __eq__(self,other):
#         return self.title==other.title and self.author==other.author
    
#     def __lt__(self,other):
#         return self.num_pages<other.num_pages
    

#     def __lt__(self,other):
#         return self.num_pages>other.num_pages
    
#     def __add__(self,other):
#         return f"{self.num_pages + other.num_pages}"
    
#     def __getitem__(self,key):
#         if key=='title':
#             return self.title
#         elif key=="author":
#             return self.author
#         elif key=="num_pages":
#             return self.num_pages
#         else:
#             return f"key {key} was not found"




# book1=Book("dfghj","qwerty",96)
# book2=Book("mnbvc","poiuyt",77)
# book3=Book("tyu","sdfg",89)
# print(book1)
# print(book1==book2)
# print(book1>book2)
# print(book1<book2)
# print(book1+book2)
# print(book1["author"])


#############################################################################################################################
##PROPERTY
# class Rectangle:
#     def __init__(self,width,height):
#         self._width=width
#         self._height=height


# rectangle=Rectangle(3,4)


# print(rectangle._width)
# see scsrshot

#############################################################################################################################
##DECORATOR
# # def add_sprinklers(func):
# #     def wrapper():
# #         print("*You added sprinklers!...*")
# #         func()
# #     return wrapper


# # @add_sprinklers
# # def get_icecream():
# #     print("Here is your icecream!")

# # get_icecream()

# def add_sprinklers(func):
#     def wrapper(*args,**kwargs):
#         print("*You added sprinklers!...*")
#         # func(*args,**kwargs)
#         func()
#     return wrapper


# def add_fudge(func):
#     def wrapper(*args,**kwargs):
#         print("*you add fudge*")
#         func()

#     return wrapper



# @add_sprinklers
# @add_fudge
# def get_icecream():
#     print("Here is your icecream!")

# get_icecream("chocolate")

#############################################################################################################################
##EXCEPTION-HANDLING



# number=int(input("enter a number: "))
# print(1/number)

# try:
#     number=int(input("enter a number: "))
#     print(1/number)
# except ValueError:
#     print("enter numbers only")

# except ZeroDivisionError:
#     print("you cant divide by zero idiot! ")

# except Exception:
#     print("something went error! ")
# finally:
#     print("this is printed always")

#############################################################################################################################
##FILE DETECTION

# import os


# # file_path="test.txt"
# # file_path="stuff/test.txt"
# file_path="/Users/riteshkumar/Desktop"

# if os.path.exists(file_path):
#     print(f"the location '{file_path}' exists")

#     if os.path.isfile(file_path):
#         print("that is a file")

#     elif os.path.isdir(file_path):
#         print("that is a directory")
# else:
#     print("That location doesn't exists")

#############################################################################################################################
##WRITING FILES
# txt_data = "I like Pizza"
# file_path = "/Users/riteshkumar/Desktop/test.txt"

# try:
#     # with open(file_path, "w") as file:
#     # with open(file_path, "x") as file:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path}' is created")

# except FileNotFoundError:
#     print("That path does not exist")

# employees=["asdfg", "qwert","yuiop","vbnm"]
# file_path="/Users/riteshkumar/Desktop/test1.txt"


# try:
#     with open(file_path,"w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#             print(f"txt file '{file_path}' is created")

# except FileNotFoundError:
#     print("That path does not exist")

##JSON

# import json

# employee={
#     "name":"Spsdfgh",
#     "age":"30",
#     "job":"cook"

# }


# file_path= "/Users/riteshkumar/Desktop/test2.json"

# try:
#     with open(file_path, "w") as file:
#         # json.dump(employee,file)
#         json.dump(employee,file,indent=4)
#         print(f"json file '{file_path}' was created")

# except FileNotFoundError:
#     print("that was not exists")

##CSV
# import csv
# employees=[["Name", "Age", "Job"],
#            ["ertyu",30,"rtyui"],
#            ["qwer",34,"nm,"],
#            ["vbnm,",45,"bnm,"]


#            ]

# file_path= "/Users/riteshkumar/Desktop/test3.csv"

# try:
#     with open(file_path,"w") as file:
#         writer=csv.writer(file)
#         for row in employees:
#             writer.writerow(row)

#         print(f"csv file '{file_path}' was created")

# except FileNotFoundError:
#     print("that was not exists")


#############################################################################################################################
##READING FILES
# import json
# import csv

# # file_path="/Users/riteshkumar/Desktop/test.txt"
# # file_path="/Users/riteshkumar/Desktop/test2.json"
# file_path="/Users/riteshkumar/Desktop/test3.csv"

# try:
#     with open(file_path,"r") as file:
#         # content =file.read()
#         # content =json.load(file)
#         content =csv.reader(file)
#         # print(content)
#         # print(content["name"])
#         for line in content:
#             print(line)

# except FileNotFoundError:
#     print("That file was not found")

# except PermissionError:
#     print("you do not have permission to read that file")

#############################################################################################################################
##DATE TIME

# import datetime
# date=datetime.date(2025,12,5)
# today=datetime.date.today()

# time=datetime.time(12,30,0)
# now= datetime.datetime.now()

# now =now.strftime("%H:%M:%S %d-%m-%y")


# print(date)
# print(today)
# print(now)

##SEE FILE ALARM CLOCK

#############################################################################################################################
##THREADING

# import threading
# import time

# def walk_dog(first,last):
#     time.sleep(8)
#     print(f"you finished out walking the {first} {last}")

# def take_out_trash():
#     time.sleep(2)
#     print("you take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("you get the mail")

# # walk_dog()
# # take_out_trash()
# # get_mail()

# chore1=threading.Thread(target=walk_dog, args=("scooby","doo"))
# chore1.start()

# chore2=threading.Thread(target=take_out_trash)
# chore2.start()

# chore3=threading.Thread(target=get_mail)
# chore3.start()

#############################################################################################################################
##API

# import requests
# import json


# base_url="https://pokeapi.co/api/v2"

# def get_pokemon_info(name):
#     url=f"{base_url}/pokemon/{name}"
#     response=requests.get(url)

#     if response.status_code==200:
#         pokemon_data=response.json()
#         return pokemon_data
#     else:
#         print(f"failed to retrieve the data {response.status_code}")


# pokemon_name="pikachu"
# pokemon_info=get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"]}")
#     print(f"weight: {pokemon_info["weight"]}")
#     print(f"height: {pokemon_info["height"]}")

#############################################################################################################################
##PYQt5
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#         self.setGeometry(0, 0, 600, 400)
#         self.setWindowTitle("My cool first GUI")

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())   


# if __name__ == "__main__":
#     main()


# ##see more in scrshot notes

























































        


        
























