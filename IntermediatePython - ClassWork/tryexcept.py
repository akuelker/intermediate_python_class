while(True):
    try:
        intNumber = int(input("Enter an integer "))
    except ValueError:
        print("That was not an int")
        break;
    else:
        print("Your number is %d" %intNumber)
    finally:
        print("Yay")
