class BadAge(Exception):
    message = "Too old or too young to be a real humanoid"

try:
    intAge = int(input("Enter age"))
    if (intAge >122 or intAge <0):
        print("Throw Exception")
    else:
        print("Nice")
except ValueError as ex:
    print("Not a real number")
except BadAge as ex:
    print("You entered: ", ex)
    print(ex.message)
finally:
    print("See ya")
