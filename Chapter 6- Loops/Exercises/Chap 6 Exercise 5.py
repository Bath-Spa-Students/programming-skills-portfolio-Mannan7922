# List of sandwich orders
sandwich_orders = ["Tuna", "Pastrami", "Chicken Club", "BLT", "Pastrami", "Ham and Cheese", "Pastrami", "Turkey"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Printing a message about running out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Removing all occurrences of 'pastrami' from sandwich_orders
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Loop through sandwich orders and make each sandwich
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)  # Add the made sandwich to finished sandwiches list

# Printing the list of finished sandwiches
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)