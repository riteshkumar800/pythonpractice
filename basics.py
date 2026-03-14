print("Hello world")

## variables

#strings
first_name="bro"
print(f"hello {first_name}")

#integers
age=26
print(f"your age id: {age}")

#float
price=23.34
print(f"price is {price}")

#boolean
is_student=True #T or F should be capital
print(f"are you a student?: {is_student}")

for_sale=True
if for_sale:
    print(f"that item is for sale")
else:
    print(f"not for sale")


##Typecasting
name="bro code"
print(type(name))
gpa=6.3
gpa=int(gpa)
print(type(gpa))
age=str(age)
print(type(age))

##input()

# name=input("whts your name:?")
# print(f"my name is: {name}")
# age=int(input("your aage:? "))
# age+=1
# print(f"your age is: {age}")

##Exercise
# item=input("what do u want to buy:? ")
# price=float(input("what is the price:? "))
# quantity=int(input("what the quantity:? "))
# total=price*quantity


# print(f"you have bought: {quantity}x{item}/s")
# print(f"your total is: ${total}")

##some basics
# import math

# print(math.pi)
# print(math.e)
# x=9
# result=math.sqrt(x)
# print(f"{result}")

##exercises
# import math

# radius=float(input("enter the radius: "))
# circumference=2*math.pi*radius
# print(f"circumference of the circle is: {round(circumference,2)}cm")



# import math
# a=float(input("enter the first: "))
# b=float(input("enter the second: "))

# c=math.sqrt(pow(a,2)+pow(b,2))

# print(f"side c is: {round(c,2)}")


##ifelse
# age=int(input("enter your age: "))

# if age>=100:
#     print(f"you are too old to suign up")
# elif age>=18:
#     print(f"you are now signe up")
# elif age<0:
#     print(f"you hevent been born yet")
# else:
#     print(f"you must be 18+ to sign up")    


# response= input("would u like food?(Y/N): ")

# if response=="Y":
#     print(f"you have food!")
# else:
#     print(f"you have not food") 


# weight=float(input("enter your weight: "))
# unit = input("enter kilograms or pounds?(K or L):  ")

# if unit=="K":
#     weight=weight*2.205
#     unit="Lbs"
#     print(f"your weight is : {round(weight,2)} {unit}")
# elif unit=="L":
#     weight=weight/2.205
#     unit="kgs"
#     print(f"your weight is: {round(weight,1)} {unit}")
# else:
#     print(f"unit {unit} is not valid")


##conditional statement
# num=5
# a=6
# b=7

# print(f"POSITIVE" if num>0 else "NEGATIVE")
# result=True if a>b else False
# print(result)


##important

# name=input("enter your name: ")
# phonenum=input("enter your phone number: ")

# len=len(name)
# print(len)
# res=name.find("o")
# res=name.rfind("o")
# name=name.upper()
# x=phonenum.replace("-","")
# print(x)



# print(help(str))

##EXERCISE

# username=input("enter your username:")

# if len(username)>12:
#     print(f"your username cannot contain more than 12 chars")
# elif not username.find(" ")==-1:
#     print(f"username cannot cont contain  spaces")
# elif not username.isalpha():
#     print(f"username cannot contain numbers")
# else:
#     print(f"welcme {username}")


##INDEXING

# credit_number= "1234-5678-9012-3456"

# print(credit_number[-1])
# print(credit_number[0:6])
# print(credit_number[::3])
# x=credit_number[-4:]
# print(f"your cresitcard no is: XXXX-XXXX-XXXX-{x}")


#WHILE-LOOP

# age=int(input("enter your age: "))

# while age<0:
#     print(f"age cannot be negative")
#     age=int(input("enter your age: "))

# print(f"your age is: {age}")    



#######PYTHON COMPOUND IINTEREST CALCULATOR########

# principal=0
# time=0
# rate=0

# while True:
#     principal=float(input("enter the principal amount: "))
#     if principal<0:
#         print(f"principal cant be negative")
#         principal=float(input("enter the principal amount: "))
#     else:
#         break 

# while True:
#     time=float(input("enter the time amount: "))
#     if time<0:
#         print(f"time cant be negative")
#         time=float(input("enter the time amount: "))
#     else:
#         break  

# while True:
#     rate=float(input("enter the rate amount: "))
#     if rate<0:
#         print(f"time cant be negative")
#         rate=float(input("enter the rate amount: "))
#     else:
#         break    

# total=principal*pow((1+rate/100),time)
# print(f"Balance after {time} years: ${total:.2f}")

##FOR LOOPS


# for x in range(1,11):
#     print(x)

# for x in reversed(range(1,11)):
#     print(x)  


# for x in range(1,11,3):
#     print(x)    

# credit_card="1234-5678-9012-3456"

# for x in credit_card:
#     print(x) 

# for x in range(1,21):
#     if x==13:
#         break #continue
#     else:
#         print(x)





#######TIME COUUNTDOWN########

# see Timecoundownprogram File


###NESTED LOOP####


# rows=int(input("enter then number of rows: "))
# columns=int(input("enter the number of columns: "))
# symbol=input("enter  symbol to use: ")


# for x in range(rows):
#     for y in range(columns):
#         print(symbol,end ="")
#     print()    



##COLLECTION####

# fruits=["a", "o","b", "c" ]
# # print(fruits[4])
# # print(fruits[::-1])

# for fruit in fruits:
#     print(fruit)

# print("o" in fruits)    
# fruits[0]="d"

# print(fruits)
# fruits.sort()
# fruits.reverse()


#####SHOPING CART PROGRAM#####
#see the file



### 2D ########
# fruits =["apple", "orange", "banana"]
# vegetables=["aloo","bhindi", "ghobhi"]
# meats=["chicken","fish","turkey"]


# groceries=[fruits,vegetables,meats]

# print(groceries[2][2])



##EXERCISE##

# num_pad=((1,2,3),
#          (4,5,6),
#          ("*",0,"#"))
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

###python quiz game####
#see the file

###dictionary####

# capitals={"USA": "Washingtin D.C",
#           "INDIA": "New Delhi",
#           "China": "Bejing",
#           "Russia": "Moscow"
        
#           }

# print(capitals.get("INDIA"))
# print(capitals.get("Japan"))
# capitals.update({"USA":"Detroit"})
# keys=capitals.keys()
# for key in keys:
#     print(key)
# values=capitals.values()
# for value in values:
#     print(value)

# item=capitals.items()....


##CONCESSION STAND PROGRAM####

# see file

##RANDOM##

# import random
# low=1
# high=100
# options=("rock","paper","scissors")
# cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# number=random.randint(low,high)
# number=random.random() #numbers between 0,1
# print(number)

# option=random.choice(options)
# print(option)

# random.shuffle(cards)
# print(cards)

##PYTHON NUMBER GUESSSING GAME##
#see file


##rockpaperscissorgame###
#see file


##FUNCTIONS##
# def happy_birthday(name, age):
#     print(f"Happy birtday to {name}!")
#     print(f"you are {age} years old!")
#     print(f"Happy birthday to you!")
#     print()

# happy_birthday("Bro", 20)    
# happy_birthday("steve", 30)    
# happy_birthday("ritesh", 22)    
# happy_birthday("ravi", 20)    



##RETURN##

# def multiply(x,y):
#     z=x*y
#     return z

# print(multiply(2,3))

# def create_name(first,last):
#     first=first.capitalize()
#     last=last.capitalize()

#     return first+" "+last

# full_name = create_name("ritesh", "kumar")
# print(full_name)

##DEFAULT ARGUMENT##
# import time

# def count(end,start):
#     for x in range(start,end):
#         print(x)
#         time.sleep(1)
#     print("DONE!")


# count(30,15)

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num=get_phone(country=1, first=456, area=123, last=7890)

# print(phone_num)

##*args and **kwargs##

# def add(*args):
#     total=0
#     for arg in args:
#         total+=arg

#     return total

# print(add(1,2,3,4,5))    

##MEMBERSHIP OPERATORS##

# word="APPLE"

# letter= input("Guess a letter in the secret word: ")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")    




# grades={"sandy": "A",
#         "squidward": "B",
#         "spongebob": "C",
#         "patric": "D"
# }

# student=input("enter the nam eof the student: ")

# if student not in grades:
#     print(f"student is not available")
# else:
#     print(f"{student}'s grade is {grades[student]}")
   


# email="ritesh@gmail.com"


# if "@" in email and "." in email:
#     print("valid email")
# else:
#     print("Invalid email")    


##LIST COMPREHENSION##
# doubles=[x*2 for x in range(1,11)]

# print(doubles)

# numbers=[1, -2, 3, -4, 5, -6, 8,9]

# positives_num=[num for num in numbers if num>=0 ]

# print(positives_num)


##SWITCHCASE##

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is sunday"
#         case 2:
#             return "It is moonday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Not a valid day"
        


# print(day_of_week(1))  

# def is_weekend(day):
#     match day:
#         case "saturday" | "sunday":
#             return True
#         case "monday"  | "Tuesday"  | "wednesday"  | "Thursday"  | "Friday":
#             return False
#         case _:
#             return False

# print(is_weekend("monday"))         




       



























            
























