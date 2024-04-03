# List of Sandwich Orders
sandwich_orders = ["Ham & Cheese", "Tuna Fish", "BLT", "Vegetarian", "Club"]

# Empty list for Finished Sandwiches
finished_sandwiches = []

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
