import time

# values for polynomial
def calculate_polynomial(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d

# calculate derivative
def calculate_derivative(a, b, c, d, x):
    return 3 * a * x ** 2 + 2 * b * x + c


def time_measurement(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return round(end_time - start_time, 5)


def parameters_input():
    while True:
        a = float(input("Enter 'a' value: "))
        b = float(input("Enter 'b' value: "))
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


def bisection_method(a, b, c, d, eps, max_iterations=1000):
    # values for points a and b - setting range
    f_a = calculate_polynomial(a, b, c, d, a)
    f_b = calculate_polynomial(a, b, c, d, b)

    # if a or b == 0 then a or b are roots
    if f_a == 0:
        return a
    elif f_b == 0:
        return b
    # if finction doesn't change sign  there is no root between then
    elif (f_b > 0) == (f_a > 0):
        print("No solution exists")
        return None

    iterations = 0  # iteration counter

    while (b - a) >= eps:
        # Iteracyjne obliczanie
        midpoint = (a + b) / 2
        f_midpoint = calculate_polynomial(a, b, c, d, midpoint)

        if abs(f_midpoint) < eps:
            # Szukanie stopnia wielokrotności
            degree = 1
            while abs(calculate_polynomial(a, b, c, d, midpoint + eps)) < eps:
                degree += 1
                midpoint += eps
            print(f"Found a root of multiplicity {degree} at x = {midpoint}")
            return midpoint

        if f_midpoint == 0:
            return midpoint
        elif (f_midpoint > 0) == (f_a > 0):
            a = midpoint
        else:
            b = midpoint

        iterations += 1
        if iterations > max_iterations:
            print("Exceeded maximum iterations, method may not converge")
            return None

    return (a + b) / 2


def newton_method(epsilon, a, b, c, d):
    # Metoda Newtona dla ustalonego przedziału [a, b]
    x = calculate_polynomial(a, b, c, d, -b / (2 * a))  # Start with a reasonable initial guess
    f_x = calculate_polynomial(a, b, c, d, x)
    derivative = calculate_derivative(a, b, c, d, x)

    iterations = 0  # Licznik iteracji

    while abs(f_x) >= epsilon:
        if derivative == 0:  # Jeśli pochodna wynosi zero, metoda Newtona rozbiega się
            print("Derivative is zero, method diverges")
            return None
        elif iterations > 1000:  # Ograniczenie liczby iteracji
            print("Exceeded maximum iterations, method may not converge")
            return None

        x = x - f_x / derivative
        f_x = calculate_polynomial(a, b, c, d, x)
        derivative = calculate_derivative(a, b, c, d, x)

        if abs(f_x) < epsilon:
            # Stopień wielokrotności
            degree = 1
            while abs(calculate_polynomial(a, b, c, d, x + epsilon)) < epsilon:
                degree += 1
                x += epsilon
            print(f"Found a root of multiplicity {degree} at x = {x}")
            return x

        iterations += 1

    return x


def method_wrapper(method_name, epsilon, a, b, c, d):
    method_name = "Bisection" if method_name == bisection_method else "Newton"
    print(f"\n==================== {method_name} method ========================")

    if method_name == bisection_method:
        solution = bisection_method(a, b, c, d, epsilon)
    else:
        solution = newton_method(epsilon, a, b, c, d)

    if solution is not None:
        abs_error = abs(calculate_polynomial(a, b, c, d, solution))
        print(f"The approximate root is: {solution} ")
        print(f"The error is: {abs_error:.10f}")
    else:
        print("No solution was found")


precision = choose_precision()
a, b, c, d = parameters_input()

time_taken = time_measurement(lambda: method_wrapper(bisection_method, precision, a, b, c, d))
print(f"The time taken for calculation (bisection method) is: {time_taken: .5f} seconds")

time_taken = time_measurement(lambda: method_wrapper(newton_method, precision, a, b, c, d))
print(f"The time taken for calculation (Newton's method) is: {time_taken: .5f} seconds")
