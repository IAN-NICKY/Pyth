# Use words.txt as the file name
fname = input("Enter file name: ")
fhandler = open(fname)

for lines in fhandler:
    lines = lines.rstrip()
    print(lines.upper())
    
