while True:
    try:
        score = input("Enter Score: ")
        score = float(score)

        if score < 0.0 or score > 1.0 :
            print("Enter value between 0.0 and 1.0:")
            continue

        elif score >= 0.9 :
            print ("A")

        elif score >= 0.8 :
            print ("B")

        elif score >= 0.7 :
            print("C")

        elif score >= 0.6 :
            print("D")

        else :
            print("F")  

        break
    except ValueError:

        print("Enter valid value which is a number between 0.0 and 1.0")