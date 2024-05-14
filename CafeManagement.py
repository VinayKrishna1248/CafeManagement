menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80
}

#Greet
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

order_total = 0

item = input("Enter the name of item you want to order = ")

while item in menu:
    order_total += menu[item]
    another_order = input("Do you want to add another item? (Yes/No) ")
    if another_order == 'Yes':
        item = input("Enter the name of item you want to order = ")
    else:
        print(f"The total amount of items to pay is {order_total}")
        break
