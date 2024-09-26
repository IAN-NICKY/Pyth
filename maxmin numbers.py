largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done":  # Exit the loop if the user types 'done'
        break
    
    try:
        # Convert the input to an integer
        num = int(num)
        
        # Update largest if it's None or if the current number is larger
        if largest is None or num > largest:
            largest = num
        
        # Update smallest if it's None or if the current number is smaller
        if smallest is None or num < smallest:
            smallest = num
    
    except ValueError:  # Catch invalid input that cannot be converted to an integer
        print("Invalid input")

# Output the results after the loop ends
print("Maximum is", largest)
print("Minimum is", smallest)
