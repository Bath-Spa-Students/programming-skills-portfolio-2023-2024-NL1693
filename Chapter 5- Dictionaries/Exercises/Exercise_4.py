# Dictionary with Major Rivers & Countries
Rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Ganges": "India"
}

# Print Sentence about Each River       # .items for Both Key and Value
print("Information about Major Rivers:")
for River, Country in Rivers.items():
    print(f"The {River} runs through {Country}.")

# Print River Names                     # .keys for Only Key
print("\nNames of Major Rivers:")
for River in Rivers.keys():
    print(River)

# Print Country Names                   # .values for Only Value
print("\nNames of Countries:")
for Country in Rivers.values():
    print(Country)
