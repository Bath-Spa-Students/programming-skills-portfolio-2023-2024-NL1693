# Dictionary to Store Items
Items = {
    'Snacks': {
        1: {'Item': 'Doritos', 'Price': 3.00},
        2: {'Item': 'KitKat', 'Price': 2.50},
        3: {'Item': 'Lays', 'Price': 1.50},
        4: {'Item': 'Snickers', 'Price': 4.00},
        5: {'Item': 'Cheez-its', 'Price': 2.50}
    },
    'Drinks': {
        6: {'Item': 'Cold Coffee', 'Price': 3.00},
        7: {'Item': 'Diet Soda', 'Price': 2.50},
        8: {'Item': 'Energy Drink', 'Price': 5.00},
        9: {'Item': 'Water Bottle', 'Price': 1.00},
        10: {'Item': 'Juice', 'Price': 2.00}
    }
}

# Welcome Customer
print("Welcome!")
print("\nItems Available:")

# Print Category Name
for category, category_items in Items.items():
    print(f"\n{category.capitalize()}:")

    # Print Item Code, Name, & Price
    for item_number, item_details in category_items.items():
        print(f"Item {item_number} | {item_details['Item'].capitalize()} - Price: {item_details['Price']} AED")

# Input User Cash
while True:
    try:
        Cash = float(input("\nPlease Insert Cash: "))
        break
    except ValueError:
        print("\nError! Please Re-Enter.")

# Input User's Selected Items
Sel_Items = []
while True:
    try:
        Sel_Item_Num = int(input("\nPlease Enter Desired Item's Code: "))
        print(f'\nNOTE: Select Items Sequencially; Enter 0 to Proceed.')
        if Sel_Item_Num == 0:
            break
        elif Sel_Item_Num in [num for cat in Items.values() for num in cat.keys()]:
            Sel_Items.append(Sel_Item_Num)
        else:
            print("Invalid Item Code. Please Re-Enter.")
    except ValueError:
        print("Invalid Item Code. Please Re-Enter.")

# Calculate Total & Print Dispensing Message
Total = 0
for Sel_Item_Num in Sel_Items:
    for category, category_items in Items.items():
        if Sel_Item_Num in category_items:
            Sel_Item = category_items[Sel_Item_Num]['Item']
            Price = category_items[Sel_Item_Num]['Price']
            print(f"\nSelected Item | {Sel_Item.capitalize()} | Price: {Price} AED.\nYour Item is being Dispensed...")
            Total += Price

# Show Total
if Cash >= Total:
    Change = Cash - Total
    print(f"\nTotal: {Total} AED")
    print(f"Change: {Change} AED")
else:
    print(f"\nTotal: {Total} AED")
    print(f"Appologies, Your Cash is Insufficient")