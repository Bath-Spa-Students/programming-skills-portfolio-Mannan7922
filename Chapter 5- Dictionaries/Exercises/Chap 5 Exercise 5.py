# Create a list of dictionaries representing different pets
pets = [
    {'kind': 'Dog', 'owner': 'Alice'},
    {'kind': 'Cat', 'owner': 'Bob'},
    {'kind': 'Bird', 'owner': 'Charlie'},
    {'kind': 'Rabbit', 'owner': 'Diana'}
]

# Loop through the list and print all information about each pet
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()  # Print a newline to separate each pet's details
