import time


def calculate_polynomial(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def calculate_derivative(a, b, c, d, x):
    return 3 * a * x ** 2 + 2 * b * x + c


def time_measurement(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return round(end_time - start_time, 4)


def get_valid_interval():
    while True:
        a = float(input("Enter 'a' value: "))
        b = float(input("Enter 'b' value: "))

        if a * b >= 0:
            print("The values 'a' and 'b' must have opposite signs.")
        else:
            c = float(input("Enter 'c' value: "))
            d = float(input("Enter 'd' value: "))
            return a, b, c, d


def choose_precision():
    while True:
        print("Choose precision level:")
        print("1. 1e-1")
        print("2. 1e-2")
        print("3. 1e-3")
        print("4. 1e-4")
        print("5. 1e-5")
        print("6. 1e-6")
        choice = input("Pick precision you want to use (1-6): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            precision_mapping = {'1': 1e-1, '2': 1e-2, '3': 1e-3, '4': 1e-4, '5': 1e-5, '6': 1e-6}
            epsilon = precision_mapping[choice]
            return epsilon
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def newton_method(epsilon, a, b, c, d):
    x = calculate_polynomial(a, b, c, d, -b / (2 * a)) # Start with a reasonable initial guess
    f_x = calculate_polynomial(a, b, c, d, x)
    derivative = calculate_derivative(a, b, c, d, x)

    while abs(f_x) >= epsilon:
        if derivative == 0: # If derivative is zero, newton's method diverges
            print("Derivative is zero, method diverges")
            return None
        x = x - f_x / derivative
        f_x = calculate_polynomial(a, b, c, d, x)
        derivative = calculate_derivative(a, b, c, d, x)

    return x


def newton_wrapper(epsilon, a, b, c, d):
    solution = newton_method(epsilon, a, b, c, d)
    if solution is not None:
        abs_error = abs(calculate_polynomial(a, b, c, d, solution))
        print("The approximate root is: ", solution)
        print(f"The error is: {abs_error:.10f}")
    else:
        print("No solution was found")


precision = choose_precision()
a, b, c, d = get_valid_interval()

time_taken = time_measurement(lambda: newton_wrapper(precision, a, b, c, d))
print("The time taken for calculation is: ", time_taken, "seconds")