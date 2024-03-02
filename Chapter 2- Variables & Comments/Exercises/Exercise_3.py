# Demonstrating Whitespace Striping on Variable

# Defining Name with Whitespace Characters
Name = "\n\v Aman Malik \r\t"

# Printing with Whitespace Characters
print(Name)

# Printing with Left-Only Stripping
print(Name.lstrip())

# Printing with Right-Only Stripping
print(Name.rstrip())

# Printing with Total Stripping
print(Name.strip())