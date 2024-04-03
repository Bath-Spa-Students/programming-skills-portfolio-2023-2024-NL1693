# make_shirt Function(Parameter="Default Value", Parameter="Default Value")
def make_shirt(size="Large", message="I Love Python"):
    print(f'Size of Shirt is {size} & Printed Message is "{message}".')

# Call Function with Default Arguments
make_shirt()

# Call Function with Only Size Argument
make_shirt("Medium")

# Call Function with Both Arguments
make_shirt(message="Eat Sleep Code Repeat", size="Extra-Large")
