fname = input("Enter file name:")
fhandler = open(fname)
# Initialize the list to hold unique words
lst = list()

# Process the file line by line
for line in fhandler:

    # Strip leading/trailing whitespace and split the line into words
    words = line.strip().split()
    
     # Check each word in the line
    for w in words:

        # Append the word if it's not already in the list
        if w not in lst:
            lst.append(w)

#sort the unique word list
lst.sort()

print(lst)
