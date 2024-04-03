# List of Sandwich Orders
sandwich_orders = ["Ham & Cheese", "Pastrami", "Tuna Fish", "Pastrami", "BLT", "Pastrami", "Vegetarian", "Pastrami", "Club"]

# Empty list for Finished Sandwiches
finished_sandwiches = []

# Print Out of Pastrami Message
print("Apologies, the Deli has run out of Pastrami.")

# Remove Pastrami from Sandwich Orders
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Loop each Sandwich Order
for sandwich in sandwich_orders:
    # Print Message for Order
    print(f"Your {sandwich} Sandwich is Ready!")
    
    # Move Sandwich to Finished Sandwiches List
    finished_sandwiches.append(sandwich)

# Print Message Listing All Finished Sandwiches
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)
