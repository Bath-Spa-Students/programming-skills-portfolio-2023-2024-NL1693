# List of Guests Invited to Dinner
Guests = ['Sir Isaac Newton', 'Charles Darwin', 'Albert Einstein']

# Inviting 1st Guest
Name = Guests[0]
print (f"\n{Name}, I'd be honored to have you for dinner.")

# Inviting 2nd Guest
Name = Guests[1]
print (f"{Name}, Would you kindly attend our dinner?")

# Inviting 3rd Guest
Name = Guests[2]
print (f"{Name}, Could you grace our table for dinner?\n")

# Printing the Guest who can't make it
Name = Guests[0]
print (f"{Name} can't make it to Dinner.\n")

# Replacing Guest with New Guest
Guests[0] = 'Alan Turing'

# Inviting New 1st Guest
Name = Guests[0]
print (f"{Name}, I'd be honored to have you for dinner.")

# Inviting 2nd Guest Again
Name = Guests[1]
print (f"{Name}, Would you kindly attend our dinner?")

# Inviting 3rd Guest Again
Name = Guests[2]
print (f"{Name}, Could you grace our table for dinner?\n")

# Printing Limit to Guests for Dinner
print ("Only 2 Guests can be invited to Dinner.\n")

# Removing Guests until 2 Remain
while len(Guests) > 2:
    Popped_Guest = Guests.pop()
    print(f"Unfortunately, {Popped_Guest}, I can no longer invite you to Dinner. My Apologies.")

# Printing Messages to Remaining Guests
for Remaining_Guest in Guests:
    print(f"{Remaining_Guest}, you're still invited to Dinner.")

# Emptying the List
del Guests[:]

# Printing to Verify List is Empty
print("\nEmpty List:", Guests)