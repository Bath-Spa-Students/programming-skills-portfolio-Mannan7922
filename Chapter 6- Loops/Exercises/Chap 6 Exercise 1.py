topping = ''  # Initialize the variable for topping

# Loop to prompt the user for pizza toppings
while topping != 'quit':
    topping = input("Enter a topping to add to your pizza (Enter 'quit' to finish): ")
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
