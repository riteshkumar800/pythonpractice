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




            
























