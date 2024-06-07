# ════════════════════ #

# Import Modules
import time, sys

# Constants
Animation_Sleep = 0.2
Banner_Sleep = 0.02
Progress_Bar_Sleep = 0.4
Column_Padding = 4
Selection_Promt = '\nPlease Enter Desired Item\'s Code (Enter 0 to Proceed): '

# ══════════ Animation Functions ══════════ #

# Animate Loading Process with a Spinning Symbol
def Animate_Loading(msg, dur=2):
    frames = "|/-\\"
    end_time = time.time() + dur
    while time.time() < end_time:
        for frame in frames:
            sys.stdout.write(f'\r{msg} {frame}')
            sys.stdout.flush()
            time.sleep(Animation_Sleep)
    sys.stdout.write(f'\r{msg} Done!{" " * 10}\n')
    sys.stdout.flush()

# ════════════════════ #

# Animate Progress Bar with Percentage Completion
def Animate_Progress_Bar(msg, dur=4):
    steps = 10
    for i in range(steps + 1):
        progress = ' ▰' * i + ' ▱' * (steps - i)
        per_comp = (i / steps) * 100
        bar = f'{msg}: [{progress}  ] {per_comp:.0f}%'
        sys.stdout.write(f'\r{bar.ljust(50)}')
        sys.stdout.flush()
        time.sleep(dur / steps)
    print()

# ══════════ Display Functions ══════════ #

# Print Welcome Banner with Animation
def Print_Welcome_Banner():
    welcome = '''
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
    █ ░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░ █
    █ ░░║║║╠─║─║─║║║║║╠─░░ █
    █ ░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░ █
    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
    '''
    for char in welcome:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(Banner_Sleep)
    time.sleep(1)

# ════════════════════ #

# Print Available Items with Categories & Prices in 2 Columns
def Print_Available_Items(items):
    print('\n════════════════════════════════════════')
    print('\nAvailable Items:')
    time.sleep(1)

    categories = list(items.keys())
    half = len(categories) // 2
    column1, column2 = categories[:half], categories[half:]

    def format_item_text(cat, item_num, item_info):
        return f"Item {item_num} | {item_info['item']} - Price: {item_info['price']} AED"

    max_len = max(len(format_item_text(cat, item_num, item_info)) for cat in items for item_num, item_info in items[cat].items())

    for i in range(max(len(column1), len(column2))):
        left_text = right_text = ""

        if i < len(column1):
            left_cat = column1[i]
            left_text = f"{left_cat}:\n"
            for item_num, item_info in items[left_cat].items():
                left_text += format_item_text(left_cat, item_num, item_info) + "\n"
        
        if i < len(column2):
            right_cat = column2[i]
            right_text = f"{right_cat}:\n"
            for item_num, item_info in items[right_cat].items():
                right_text += format_item_text(right_cat, item_num, item_info) + "\n"
        
        left_lines = left_text.split('\n')
        right_lines = right_text.split('\n')

        for left_line, right_line in zip(left_lines, right_lines):
            print(f"{left_line.ljust(max_len + Column_Padding)}{right_line}")
            time.sleep(0.1)

        if len(left_lines) > len(right_lines):
            for extra_line in left_lines[len(right_lines):]:
                print(f"{extra_line.ljust(max_len)}")
                time.sleep(0.1)
        elif len(right_lines) > len(left_lines):
            for extra_line in right_lines[len(left_lines):]:
                print(f"{' '.ljust(max_len)}{extra_line}")
                time.sleep(0.1)
    
    print('════════════════════════════════════════\n')

# ════════════════════ #

# Print User Selected Items & Their Price
def Print_Selected_Items(sel_items, item_map):
    print('\n════════════════════════════════════════\n')
    print('Selected Items:')
    time.sleep(1)
    total = 0
    for sel_item_num in sel_items:
        sel_item = item_map[sel_item_num]['item']
        price = item_map[sel_item_num]['price']
        print(f"{sel_item} | Price: {price} AED.")
        total += price
        time.sleep(0.5)
    return total

# ════════════════════ #

# Print Thank You Banner with Animation
def Print_Thank_You_Banner():
    thank_you = '''
    .▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█
    ─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█
    '''
    for char in thank_you:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(Banner_Sleep)
    time.sleep(1)
    print('\n════════════════════════════════════════\n')

# ══════════ User Interaction Functions ══════════ #

# Get User Input for Cash Amount
def Get_User_Cash():
    while True:
        try:
            cash = float(input("Please Insert Cash: "))
            if cash < 0:
                raise ValueError
            time.sleep(0.25)
            Animate_Loading("Processing Cash ")
            return cash
        except ValueError:
            print("Error! Please enter a valid amount.\n")
            time.sleep(0.25)
            print(f'════════════════════════════════════════\n')

# ════════════════════ #

# Get User Input for Selected Items & Display Relative Suggestions
def Get_Selected_Items(item_map):
    sel_items = []
    while True:
        try:
            print(Selection_Promt)
            sel_item_num = int(input())
            time.sleep(0.25)
            if sel_item_num == 0:
                break
            elif sel_item_num in item_map:
                sel_items.append(sel_item_num)
                sel_item = item_map[sel_item_num]['item']
                price = item_map[sel_item_num]['price']
                print(f'Item Selected [ {sel_item} | {price} AED ]')
                time.sleep(0.25)
                Animate_Progress_Bar("Adding item to cart")
                time.sleep(0.25)
                suggestions = item_map[sel_item_num].get('suggestions', [])
                if suggestions:
                    print("\nYou might also like:")
                    for suggestion in suggestions:
                        print("-", suggestion)
                print(f'\n════════════════════════════════════════')
            else:
                print("Invalid Item Code. Please Re-Enter.")
                print(f'\n════════════════════════════════════════')
        except ValueError:
            print("Invalid Item Code. Please Re-Enter.")
            print(f'\n════════════════════════════════════════')
    return sel_items

# ════════════════════ #

# Display Total Cost & Handle Cash Transaction
def Show_Total(total, cash):
    print(f'\n════════════════════════════════════════\n')
    print(f"Total: {total} AED")
    if cash >= total:
        change = cash - total
        print(f"Change: {change} AED")
        Animate_Progress_Bar("Dispensing Change")
        Animate_Progress_Bar("Dispensing Items")
        print(f'\n════════════════════════════════════════\n')
    else:
        print(f"\nApologies, Your Cash is Insufficient\nReturning {cash} AED")
        print(f'\n════════════════════════════════════════\n')

# ══════════ Main Vending Machine Function ══════════ #

def Vending_Machine():
    # Dictionary to Store Available Items & Their Details (Price & Suggestions)
    items = {
        'Savory Delights': {
            1: {'item': 'Doritos', 'price': 3.00, 'suggestions': ['6: KitKat', '11: Skittles', '16: Coca-Cola']},
            2: {'item': 'Lays', 'price': 1.50, 'suggestions': ['7: Snickers', '12: M&M\'s', '17: Pepsi']},
            3: {'item': 'Pringles', 'price': 2.50, 'suggestions': ['8: Twix', '13: Reese\'s Pieces', '18: Sprite']},
            4: {'item': 'Cheetos', 'price': 2.00, 'suggestions': ['9: Hershey\'s', '14: Gummy Bears', '19: Dr. Pepper']},
            5: {'item': 'Ruffles', 'price': 2.75, 'suggestions': ['10: Milky Way', '15: Sour Patch Kids', '20: Mountain Dew']}
        },
        'Decadent Chocolate': {
            6: {'item': 'KitKat', 'price': 2.50, 'suggestions': ['11: Skittles', '16: Coca-Cola', '21: Dasani']},
            7: {'item': 'Snickers', 'price': 4.00, 'suggestions': ['12: M&M\'s', '17: Pepsi', '22: Aquafina']},
            8: {'item': 'Twix', 'price': 2.25, 'suggestions': ['13: Reese\'s Pieces', '18: Sprite', '23: Evian']},
            9: {'item': 'Hershey\'s', 'price': 2.75, 'suggestions': ['14: Gummy Bears', '19: Dr. Pepper', '24: Fiji']},
            10: {'item': 'Milky Way', 'price': 3.00, 'suggestions': ['15: Sour Patch Kids', '20: Mountain Dew', '25: Sparkling']}
        },
        'Sweet Indulgences': {
            11: {'item': 'Skittles', 'price': 1.00, 'suggestions': ['16: Coca-Cola', '21: Dasani', '26: Cookies']},
            12: {'item': 'M&M\'s', 'price': 1.25, 'suggestions': ['17: Pepsi', '22: Aquafina', '27: Donuts']},
            13: {'item': 'Reese\'s Pieces', 'price': 1.50, 'suggestions': ['18: Sprite', '23: Evian', '28: Muffins']},
            14: {'item': 'Gummy Bears', 'price': 1.75, 'suggestions': ['19: Dr. Pepper', '24: Fiji', '29: Croissants']},
            15: {'item': 'Sour Patch Kids', 'price': 1.50, 'suggestions': ['20: Mountain Dew', '25: Sparkling', '30: Cinnamon Rolls']}
        },
        'Fizzing Delights': {
            16: {'item': 'Coca-Cola', 'price': 1.75, 'suggestions': ['21: Dasani', '26: Cookies', '1: Doritos']},
            17: {'item': 'Pepsi', 'price': 1.75, 'suggestions': ['22: Aquafina', '27: Donuts', '2: Lays']},
            18: {'item': 'Sprite', 'price': 1.50, 'suggestions': ['23: Evian', '28: Muffins', '3: Pringles']},
            19: {'item': 'Dr. Pepper', 'price': 2.00, 'suggestions': ['24: Fiji', '29: Croissants', '4: Cheetos']},
            20: {'item': 'Mountain Dew', 'price': 1.75, 'suggestions': ['25: Sparkling', '30: Cinnamon Rolls', '5: Ruffles']}
        },
        'Refreshing Hydration': {
            21: {'item': 'Dasani', 'price': 1.25, 'suggestions': ['26: Cookies', '1: Doritos', '6: KitKat']},
            22: {'item': 'Aquafina', 'price': 1.25, 'suggestions': ['27: Donuts', '2: Lays', '7: Snickers']},
            23: {'item': 'Evian', 'price': 1.50, 'suggestions': ['28: Muffins', '3: Pringles', '8: Twix']},
            24: {'item': 'Fiji', 'price': 2.00, 'suggestions': ['29: Croissants', '4: Cheetos', '9: Hershey\'s']},
            25: {'item': 'Sparkling', 'price': 1.75, 'suggestions': ['30: Cinnamon Rolls', '5: Ruffles', '10: Milky Way']}
        },
        'Delectable Treats': {
            26: {'item': 'Cookies', 'price': 2.00, 'suggestions': ['1: Doritos', '6: KitKat', '11: Skittles']},
            27: {'item': 'Donuts', 'price': 2.50, 'suggestions': ['2: Lays', '7: Snickers', '12: M&M\'s']},
            28: {'item': 'Muffins', 'price': 2.25, 'suggestions': ['3: Pringles', '8: Twix', '13: Reese\'s Pieces']},
            29: {'item': 'Croissants', 'price': 2.75, 'suggestions': ['4: Cheetos', '9: Hershey\'s', '14: Gummy Bears']},
            30: {'item': 'Cinnamon Rolls', 'price': 3.00, 'suggestions': ['5: Ruffles', '10: Milky Way', '15: Sour Patch Kids']}
        }
    }

    # Item Map for Easier Lookup
    item_map = {num: info for cat in items.values() for num, info in cat.items()}
    
    Print_Welcome_Banner()
    Print_Available_Items(items)
    
    cash = Get_User_Cash()
    sel_items = Get_Selected_Items(item_map)
    
    total = Print_Selected_Items(sel_items, item_map)
    Show_Total(total, cash)
    
    Print_Thank_You_Banner()

# ══════════ Run Vending Machine ══════════ #

Vending_Machine()

# ════════════════════ #