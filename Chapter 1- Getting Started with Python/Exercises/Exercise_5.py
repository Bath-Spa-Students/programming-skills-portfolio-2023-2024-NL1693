# Calculating the Area of a User-Defined Circle

# Taking Input from User    # Using Float in case of Radius Values with Decimals
Radius = float(input("Enter the Circle's Radius: "))

# Value of π up to 10 decimal places
Pi = 3.1415926535

# Calculating Area using Formula: Area = π*R^2 (R^2 = R*R)
Area = Pi * Radius * Radius

# Printing the Area of Circle
print("Area of Circle with Radius", Radius, "is:", Area)