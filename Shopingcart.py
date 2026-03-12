



foods=[]
prices=[]
total=[]

while True:
    food=input("enter the food to buy (q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input("enter the price of a {food}: $ "))
        foods.append(food)
        prices.append(price)
total=0
print("----YOUR CART----")
for price in prices:
    total+=price

for food in foods:
    print(food,end=" ")

print()
print(f"your total is: ${total}")        

