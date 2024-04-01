# Demonstrating Whitespace Striping on Variable

# Defining Name with Whitespace Characters
Name = "\r\v Aman Malik \n\t"

# Printing with Whitespace Characters
print(Name)

# Printing with Left-Only Stripping
print(Name.lstrip())

# Printing with Right-Only Stripping
print(Name.rstrip())

# Printing with Total Stripping
print(Name.strip())