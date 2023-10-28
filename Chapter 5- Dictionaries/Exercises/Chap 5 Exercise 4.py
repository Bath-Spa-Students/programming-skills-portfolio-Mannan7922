# Creating a dictionary of rivers and the countries they run through
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# Printing a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Printing the names of each river
print("\nRivers:")
for river in rivers.keys():
    print(river)

# Printing the names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
