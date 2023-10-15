# Define the cost of one USB stick and the total budget
usb_stick_cost = 6  # £6 each
total_budget = 50  # £50 budget

# Calculate the number of USB sticks she can buy
num_usb_sticks = total_budget // usb_stick_cost

# Calculate how much money she will have left
money_left = total_budget % usb_stick_cost

# Display the results
print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{money_left} left.")