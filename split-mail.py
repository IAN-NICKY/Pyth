# Prompt the user for a file name
fname = input("Enter file name: ")

# If the user does not enter a file name, set a default file name
if len(fname) < 1:
    fname = "mbox-short.txt"

# Open the specified file for reading
fhandler = open(fname)

# Initialize a counter to keep track of lines starting with "From "
count = 0

# Iterate through each line in the file
for line in fhandler:
    # Skip lines that do not start with "From "
    if not line.startswith("From "):
        continue  # Continue to the next iteration of the loop

    # Increment the counter for each line that starts with "From "
    count = count + 1

    # Split the line into words and store it in 'mail'
    mail = line.split()

    # Print the second word (email address) from the line
    print(mail[1])

# After processing all lines, print the total count of lines that started with "From "
print("There were", count, "lines in the file with From as the first word")
