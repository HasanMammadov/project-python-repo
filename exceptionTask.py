while True:
    try:
        no_one = int(input("The first number please : "))
        no_two = int(input("The second number please : "))
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except ZeroDivisionError:
        print("You can't divide by zero!!")
        break
    except ValueError:
        print("You can only enter numbers consisting of digits, not text!!")
        break
    except Exception as e:
        print("Something went wrong...Try again.")
        print("Probably it is because of '{}' error".format(e))
        break