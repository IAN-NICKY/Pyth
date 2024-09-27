fname = input("Enter filename:")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fhandler = open(fname)

# Initialize an empty dictionary to hold email counts
count = dict()

for lines in fhandler:
    if not lines.startswith('From '):
        continue
    words = lines.split() # Split the line into words
    sender = words[1]   # Extract the sender's email (second word)

    # Update the dictionary with the sender's email
    count[sender] = count.get(sender, 0) + 1  # Increment the count, default to 0 if not found

# Initialize variables to find the most prolific sender    
prolificsender = None
bigcount = None

# Find the sender with the maximum count
for sender,count_value in count.items():
    if  prolificsender is None or count_value > bigcount:
        prolificsender = sender
        bigcount = count_value
        

print(prolificsender,bigcount)