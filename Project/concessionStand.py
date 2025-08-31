menu = {
    "pizza" : 500,
    "nachos" : 200,
    "burger" : 300,
    "popcorn" : 400,
    "fries" : 150,
    "chips" : 100,
    "soda" : 60,
    "lemonade" : 50,
    }
cart = []
total = 0

print("--------MENU--------")
for key,value in menu.items():
    print(f"{key:10} : ₹{value:}")
    
while True:
    food = input("Select an item (q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
        
print("---------YOUR ORDER--------")
for food in cart:
    total += menu.get(food)
    print(food, end= " ")
    
print()
print(f"Total : ₹{total}")
    