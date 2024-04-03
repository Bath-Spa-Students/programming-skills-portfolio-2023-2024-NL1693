# Loop to Ask for User Age
while True:
    Age = input("Please Enter your Age (type 'Quit' to exit): ")

    # Check if User Quit    # .lower to Standarize Input
    if Age.lower() == 'quit':
        break

    # Convert to Integer
    Age = int(Age)

    # Determine Price based on Age
    if Age < 3:
        print("Your Ticket is Free!")
    elif Age <= 12:
        print("Your Ticket costs $10.")
    else:
        print("Your Ticket costs $15.")
