# Importing Modules
import time
import sys

# Function to Animate Loading
def Animate_Loading(Msg, Dur=2):
    Frames = "|/-\\"
    End_Time = time.time() + Dur
    while time.time() < End_Time:
        for Frame in Frames:
            sys.stdout.write(f'\r{Msg} {Frame}')
            sys.stdout.flush()
            time.sleep(0.2)
    # Clear the Loading Animation
    sys.stdout.write(f'\r{Msg} Done!{" " * 10}\n')
    sys.stdout.flush()

# Function to Animate Progress Bar
def Animate_PBar(Msg, Dur=4):
    Steps = 10  # Number of Total Sections in the Progress Bar
    for i in range(Steps + 1):
        Progress = ' ▰' * i + ' ▱' * (Steps - i)
        Per_Comp = (i / Steps) * 100
        Bar = f'{Msg}: [{Progress}  ] {Per_Comp:.0f}%'
        sys.stdout.write(f'\r{Bar.ljust(50)}')  # Pad Output to Overwrite Previous Progress Bar
        sys.stdout.flush()
        time.sleep(Dur / Steps)
    print()

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

# Map Item Numbers to Item Info
Item_Map = {Num: Info for Cat in Items.values() for Num, Info in Cat.items()}

# Print Welcome Banner
Welcome = '\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█ ░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░ █\n█ ░░║║║╠─║─║─║║║║║╠─░░ █\n█ ░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░ █\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n'
for char in Welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)
time.sleep(1)

# Print Available Items
print('\n- - - - - - - - - - - - - - - - - - - -')
print('\nAvailable Items:')
time.sleep(1)
for Cat, Cat_Items in Items.items():
    print(f"\n{Cat}:")
    time.sleep(0.5)
    for Item_Num, Item_Info in Cat_Items.items():
        print(f"Item {Item_Num} | {Item_Info['Item']} - Price: {Item_Info['Price']} AED")
        time.sleep(0.25)
print('\n- - - - - - - - - - - - - - - - - - - -\n')

# Input User Cash
while True:
    try:
        Cash = float(input("Please Insert Cash: "))
        time.sleep(0.25)
        Animate_Loading("Processing Cash ")
        break
    except ValueError:
        print("Error! Please Re-Enter.\n")
        time.sleep(0.25)

# Input & Show User's Selected Items
Sel_Items = []
while True:
    try:
        print('\n- - - - - - - - - - - - - - - - - - - -\n')
        Sel_Item_Num = int(input("Please Enter Desired Item's Code (Enter 0 to Proceed): "))
        time.sleep(0.25)
        if Sel_Item_Num == 0:
            break
        elif Sel_Item_Num in Item_Map:
            Sel_Items.append(Sel_Item_Num)
            Sel_Item = Item_Map[Sel_Item_Num]['Item']
            Price = Item_Map[Sel_Item_Num]['Price']
            print(f'Item Selected [ {Sel_Item} | {Price} AED ]')
            time.sleep(0.25)
            Animate_PBar("Adding item to cart")
            time.sleep(0.25)
        else:
            print("Invalid Item Code. Please Re-Enter.")
    except ValueError:
        print("Invalid Item Code. Please Re-Enter.")

# Calculate Total & Print Dispensing Message
print('\n- - - - - - - - - - - - - - - - - - - - -\n')
print('Selected Items:')
time.sleep(1)
Total = 0
for Sel_Item_Num in Sel_Items:
    Sel_Item = Item_Map[Sel_Item_Num]['Item']
    Price = Item_Map[Sel_Item_Num]['Price']
    print(f"{Sel_Item} | Price: {Price} AED.")
    Total += Price
    time.sleep(0.5)

# Show Total & Change
print(f'\n- - - - - - - - - - - - - - - - - - - -\n')
print(f"Total: {Total} AED")
if Cash >= Total:
    Change = Cash - Total
    print(f"Change: {Change} AED")
    print('\nDispensing Item(s)...')
    Animate_PBar("Dispensing items")
else:
    print(f"\nApologies, Your Cash is Insufficient\nReturning {Cash} AED")
print(f'\n- - - - - - - - - - - - - - - - - - - - -\n')

ThankYou = '.▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█\n─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█\n'
for char in ThankYou:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)
time.sleep(1)