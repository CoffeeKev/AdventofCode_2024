import numpy
import logging

source_file = "sourcetest.txt"

# Set the logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)

# Initialize two empty lists to store the columns
list1 = []
list2 = []


try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into two parts
            columns = line.split()
            
            # Convert the parts to integers and append to respective lists
            list1.append(int(columns[0]))  # First column
            list2.append(int(columns[1]))  # Second column
            
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")

sorted_list1 = list1.sort()
sorted_list2 = list2.sort()

