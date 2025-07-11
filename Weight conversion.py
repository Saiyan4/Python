while True:
    try:
        weight = int(input("Enter your weight: "))
        conversion = str(input("Convert to (K)g or to (L)bs: ").lower())
        if conversion == "k":
            print("Converted to KG is: ", weight * 0.45359237)
        elif conversion == "l":
            print("Converted to LB is: ", weight * 2.20462)
        else:
            print("Invalid input")
        break
    except ValueError:
        print("Please enter a numeric value")











