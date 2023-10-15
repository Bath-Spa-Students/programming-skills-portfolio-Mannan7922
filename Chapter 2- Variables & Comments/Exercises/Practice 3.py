# Defining a person's name with whitespace characters at the beginning and end
name = "\t\n  Abdul Mannan  \n\t"

# Printing the name with whitespace
print("Name with whitespace:")
print(name)

# Printing the name using the three stripping functions
print("\nName using lstrip():")
print(name.lstrip())

print("\nName using rstrip():")
print(name.rstrip())

print("\nName using strip():")
print(name.strip())