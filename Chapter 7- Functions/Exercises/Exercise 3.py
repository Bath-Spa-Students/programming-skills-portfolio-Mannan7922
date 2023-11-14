def make_shirt(size, message):
    """Prints a sentence summarizing the size and message on the shirt."""
    print(f"Making a {size}-sized shirt with the message: '{message}'.")

# Call the function with positional arguments
make_shirt("Medium", "Hello, World!")

# Call the function with keyword arguments
make_shirt(size="Large", message="Python Lover")
