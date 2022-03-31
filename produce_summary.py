"""A delivered melons report program
that prints the delivered message with details about 
the quantity, description of item, and total delivery cost."""

# A function declaration with two parameters
def delivered_melons_report(day_number, delivery_filepath):
    """
    Prints total count of melons, melon description, and delivery cost.
    
    :param day: day of delivery as a string
    :param deliveries_day_file: text file for delivery day as a string
    :return: None
    """

    print(day_number)                              # Prints day to output
    the_file = open(delivery_filepath)    # Creates a file object to read from .txt file
    for line in the_file:                   # Repeats for each line read in the file object
        line = line.rstrip()                # Removes extra whitespace to the right of the end of the line
        words = line.split('|')             # Tokenizes the string of each line by the | delimiter, creating a list of the string elements

        melon = words[0]                    # Stores the element at index 0 as a variable for later use
        count = words[1]                    # Stores the element at index 1 as a variable for later use
        amount = words[2]                   # Stores the element at index 2 as a variable for later use

        print(f"Delivered {count} {melon}s for total of ${amount}")     # Uses string-format to print the delivery message
    the_file.close()                        # Closes the file 

# Calls the function for Day 1 and wraps in a print statement to display in output
print(delivered_melons_report("Day 1", "um-deliveries-day-1.txt"))

# Calls the function for Day 2 and wraps in a print statement to display in output
print(delivered_melons_report("Day 2", "um-deliveries-day-2.txt"))

# Calls the function for Day 3 and wraps in a print statement to display in output
print(delivered_melons_report("Day 3", "um-deliveries-day-3.txt"))
