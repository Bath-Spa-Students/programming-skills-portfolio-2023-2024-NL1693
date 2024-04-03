# Dictionaries for Different Pets & Owner Names
Pet_1 = {"Animal": "Dog", "Owner": "Alan Abalos"}
Pet_2 = {"Animal": "Cat", "Owner": "Abdur Rahman"}
Pet_3 = {"Animal": "Fish", "Owner": "John Melves"}
Pet_4 = {"Animal": "Bird", "Owner": "Vinz Patrick"}
Pet_5 = {"Animal": "Rabbit", "Owner": "Aman Malik"}

# List of Pets
Pets = [Pet_1, Pet_2, Pet_3, Pet_4, Pet_5]

# Loop through List & Print Information about Each Pet
for Pet in Pets:
    print(f"{Pet['Owner']} owns a Pet {Pet['Animal']}.")
