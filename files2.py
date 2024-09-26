# Ask the user to input the file name
fname = input("Enter file name: ")

# Open the file (this currently ignores the user input and opens 'mbox-short.txt')
fh = open(fname)

# Initialize variables to count lines and accumulate the total value
counter = 0
total = 0.0

# Loop through each line in the file
for line in fh:
    
    # Skip lines that do not start with "X-DSPAM-Confidence:"
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # Find the position of the colon and extract the number after the colon
    colpos = line.find(':')
    value = line[colpos+1:].strip()  # Remove any spaces from the extracted value

    # Convert the extracted string value to a floating-point number
    fvalue = float(value)

    # Increment the counter for each valid line
    counter = counter + 1

    # Add the floating-point value to the total
    total = total + fvalue

# After the loop, check if at least one valid line was found
if counter > 0:
    # Calculate the average of the spam confidence values
    average = total / counter
    # Print the calculated average
    print("Average spam confidence:", average)
else:
    # If no valid lines were found, print an appropriate message
    print("No 'X-DSPAM-Confidence' lines found.")

# Print "Done" to indicate that the program has finished
print("Done")
