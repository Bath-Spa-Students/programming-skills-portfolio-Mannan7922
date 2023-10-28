# Creating a glossary with programming terms and their meanings
glossary = {
    'Variable': 'A container for storing data values.',
    'Function': 'A block of code that only runs when it is called.',
    'List': 'A collection which is ordered and changeable.',
    'Dictionary': 'A collection which is unordered and changeable. It uses key-value pairs.',
    'Loop': 'A way to repeatedly execute a block of code.',
    'Module': 'A file containing Python code.',
    'Tuple': 'A collection which is ordered and unchangeable.',
    'Boolean': 'A data type that can only have one of two values: True or False.',
    'Method': 'A function that is associated with an object.',
    'Argument': 'A value passed to a function or method when it is called.'
}

# Printing each word and its meaning with a loop
for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")
