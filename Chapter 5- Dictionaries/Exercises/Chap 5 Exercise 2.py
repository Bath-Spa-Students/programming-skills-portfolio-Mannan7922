# Creating a glossary with programming terms and their meanings
glossary = {
    'Variable': 'A container for storing data values.',
    'Function': 'A block of code that only runs when it is called.',
    'List': 'A collection which is ordered and changeable.',
    'Dictionary': 'A collection which is unordered and changeable. It uses key-value pairs.',
    'Loop': 'A way to repeatedly execute a block of code.'
}

# Printing each word and its meaning with formatted output
for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")