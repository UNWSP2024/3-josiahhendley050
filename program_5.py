# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
#Josiah Hendley
#2/5/26
#Hot dog eater
def hot_dog_order():
    print("Hot Dog ($3.50) or Chili Dog ($4.50)")
    dog_type = input("Enter type of hot dog: ").lower()

    # Base price
    if dog_type == "hot dog":
        subtotal = 3.50
    elif dog_type == "chili dog":
        subtotal = 4.50
    else:
        print("Invalid choice.")
        return

    # Optional toppings
    cheese = input("Add cheese? (yes/no): ").lower()
    if cheese == "yes":
        subtotal += 0.50

    peppers = input("Add peppers? (yes/no): ").lower()
    if peppers == "yes":
        subtotal += 0.75

    onions = input("Add grilled onions? (yes/no): ").lower()
    if onions == "yes":
        subtotal += 1.00

    # Tax and total
    tax = subtotal * 0.07
    total = subtotal + tax

    print("Hot Dog Cost: $", format(subtotal, ".2f"))
    print("Tax: $", format(tax, ".2f"))
    print("Total Cost: $", format(total, ".2f"))


if __name__ == '__main__':
    hot_dog_order()
