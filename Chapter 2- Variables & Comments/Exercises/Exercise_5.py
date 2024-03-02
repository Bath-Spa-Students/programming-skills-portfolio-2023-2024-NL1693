# Calculating the Maximum Number of USB Sticks Purchasable and the Remainder

# Price of Individual USB Stick
Price = 6

# Girl's Total Budget
Budget = 50

# Maximum Number of Sticks Purchasable  # We use // to Ensure No Decimal Digits
Total = Budget // Price

# Remaining Pounds after Purchase
Remainder = Budget % Price

# Printing the Total & Remainder
print("The Girl can Buy", Total, "USB Sticks.", "She will have £" + str(Remainder), "Left.")