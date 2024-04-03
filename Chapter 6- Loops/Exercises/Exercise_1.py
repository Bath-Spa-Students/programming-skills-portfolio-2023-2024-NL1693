# Prompt User to Enter Toppings
print("Enter Pizza Toppings. Type 'Quit' to Exit.")

# Loop to Prompt for More Toppings
while True:
    Topping = input("Enter a Topping: ")

    # Check if User Quit    # .lower to Standarize Input
    if Topping.lower() == 'quit':
        break
    
    # Print Topping Added Message
    print(f"Adding {Topping} to your Pizza.")

# Print End Message
print("Enjoy your Pizza!")
