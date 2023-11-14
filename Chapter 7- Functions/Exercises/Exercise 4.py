def make_shirt(size="Large", message="I love Python"):
    """Prints a sentence summarizing the size and message on the shirt."""
    print(f"Making a {size}-sized shirt with the message: '{message}'.")

# Create a large shirt with the default message
make_shirt()

# Create a medium shirt with the default message
make_shirt(size="Medium")

# Create a custom-sized shirt with a different message
make_shirt(size="Small", message="Keep Coding!")