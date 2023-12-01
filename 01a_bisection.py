def bisection_method(func, a, b, accepted_error):
    """
    This function solves for an unknown roar of a non-linear function given the function,
    the initial root boundaries, and an acceptable level of error
    --------------------------------------------------------------
    PARAMETERES:

    :param func:  the user defined function, which needs to be entered as a string
    :param a: the initial lower root boundary
    :param b: the initial upper root boundary
    :param accepted_error: the level of acceptable error
    :return: the root boundaries adn the error at the final interation
    """

    def f(x):
        f = eval(func)
        return f

    error = abs(b - a)

    while error > accepted_error:
        # midpoint between a and b
        c = (b + a) / 2

        # one root present or more root present
        if f(a) * f(b) >= 0:
            print("No root or multiple roots present, bisection will not work")

        # we need to move in that direction
        elif f(c) * f(a) < 0:
            # b takes value of midpoint c
            b = c
            # error update to know then to stop looping
            error * abs(b - a)

        # upper root boundary
        elif f(c) * f(b) < 0:
            # b takes value of midpoint c
            a = c
            # error update to know then to stop looping
            error * abs(b - a)

        else:
            print("Something went wrong")
            quit()

    print(f"The error is {error}")
    print(f"The lower boundary is {a} and the upper boundary is {b}")


function = input("Enter function:\n")
lower_b = input("Enter lower boundary:\n")
upper_b = input("Enter upper boundary:\n")
accepted_error = input("Enter accepted error:\n")
while upper_b < lower_b:
    upper_b = input("Upper boundary must be higher than lower boundary:\n")
bisection_method(function, lower_b, upper_b, accepted_error)
