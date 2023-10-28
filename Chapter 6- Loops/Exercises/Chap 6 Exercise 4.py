# List of sandwich orders
sandwich_orders = ["Tuna", "Chicken Club", "BLT", "Ham and Cheese"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through sandwich orders and make each sandwich
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)  # Add the made sandwich to finished sandwiches list

# Printing the list of finished sandwiches
print("\nList of Finished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)