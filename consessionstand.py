


menu={"pizza": 3.00,
      "nachos":4.00,
      "popcorn":6.00,
      "fries":8.00,
      "chips":7.00

      
      
      }

cart=[]
total=0

print(f"------------MENU----------")

for keys, values in menu.items():
    print(f"{keys:10}: ${values:.2f}")
print(f"-----------------------")

while True:
    food=input("select an item (q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(f"----------YOUR ORDER--------")
for food in cart:
    total+=menu.get(food)
    print(food, end=" ")

print()
print(f"total is: ${total:.2f}")
    

       

