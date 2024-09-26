try:
    # Try block to attempt the input and conversion of the score
    score = input("Enter Score: ")
    
    # Convert the user input to a float for numerical comparison
    score = float(score)

    # Check if the score is outside the valid range (0.0 to 1.0)
    if score > 1.0 or score < 0.0:
        print("Invalid score. Please enter a score between 0.0 and 1.0.")
    
    # Assign grades based on the score
    elif score >= 0.9:   # 90% or higher gets an "A"
        print("A")
    elif score >= 0.8:   # 80% to 89% gets a "B"
        print("B")
    elif score >= 0.7:   # 70% to 79% gets a "C"
        print("C")
    elif score >= 0.6:   # 60% to 69% gets a "D"
        print("D")
    else:
        # Any score below 60% gets an "F"
        print("F")

# Handle the case where the user input is not a valid number
except ValueError:
    # Except block will run if the input cannot be converted to a float
    print("Invalid input. Please enter a numeric value.")
