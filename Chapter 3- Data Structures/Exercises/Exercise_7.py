# Using Different Operators on a List

# Places I'd Like to Visit
Places = ["Tokyo, Japan", "Farari World, Abu Dhabi", "Big Ben, London", "Rome, Italy", "Riot Games, Los Angeles"]

# Printing the Original List
print("Original List:", Places)

# Printing in Alphabetical Order
print("Sorted List:", sorted(Places))

# Showing Original List is Unchanged
print("Original List (Unchanged):", Places)

# Printing in Revesere Alphabetical Order
print("Reverse Sorted List:", sorted(Places, reverse=True))

# Showing Original List is Unchanged
print("Original List (Unchanged):", Places)

# Reversing Order of Original List      # Printing Original List to Show Reversed Order
Places.reverse()
print("Reversed List:", Places)

# Reversing Order of Reversed List      # Printing Original List to Show Orignal Order is Restored
Places.reverse()
print("Orignal List (Restored):", Places)

# Sorting Orignal List                  # Printing Original List to Show Sorted
Places.sort()
print("Sorted List:", Places)

# Reverse Sorting Original List         # Printing Original List to Show Reverse Sorted
Places.sort(reverse=True)
print("Reverse Sorted List:", Places)