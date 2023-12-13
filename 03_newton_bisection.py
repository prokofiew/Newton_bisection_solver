import time


def calculate_polynomial(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def calculate_derivative(a, b, c, d, x):
    return 3 * a * x ** 2 + 2 * b * x + c


def time_measurement(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return round(end_time - start_time, 5)


def polynomial_expression_protector(input_value, value_name):
    if input_value == 0:
        print(f"The value '{value_name}' cannot be equal to 0!")
        return False
    return True


def parameters_input():
    while True:
        a = int(input("Enter 'a' value: "))
        if not polynomial_expression_protector(a, 'a'):
            continue

        b = int(input("Enter 'b' value: "))
        if not polynomial_expression_protector(b, 'b'):
            continue
        # if a == b:
        #     print("The values 'a' nad 'b' cannot be equal")
        #     continue

        c = int(input("Enter 'c' value: "))
        if not polynomial_expression_protector(c, 'c'):
            continue

        d = int(input("Enter 'd' value: "))
        if not polynomial_expression_protector(d, 'd'):
            continue

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


def set_iteration_limit():
    while True:
        max_iterations = int(input("Enter your limit of iterations: "))
        if max_iterations < 0 or max_iterations == 0:
            print(f"Invalid input: {max_iterations}. Setting iterations limit to 1000")
            max_iterations = 1000
            return max_iterations
        else:
            return max_iterations



def bisection_method(a, b, c, d, epsilon, max_iterations):
    # counting a and b values
    a_values = calculate_polynomial(a, b, c, d, a)
    b_values = calculate_polynomial(a, b, c, d, b)

    # checking if they are qual zero, if yes they're returned as solutions
    if a_values == 0:
        return a
    elif b_values == 0:
        return b
    # checking sign of a and b. if its the same function cannot find root in given range and the is no solutions
    elif (b_values > 0) == (a_values > 0):
        print("No solution exists")
        return None

    iterations = 0  # iteration counter

    # staring loop, count till range is >= than set precision
    while (b - a) >= epsilon:
        # calculating middle point
        c = (a + b) / 2
        c_value = calculate_polynomial(a, b, c, d, c)

        # checking multiplicity of root. if values for c are close to zero
        if abs(c_value) < epsilon:
            degree = 1
            # finding another roots in main c range that are close to 0 as well.
            while abs(calculate_polynomial(a, b, c, d, c + epsilon)) < epsilon:
                degree += 1
                c += epsilon
            print(f"Found a root of multiplicity {degree} at x = {c}")
            return c
        # if c = 0 - found solution root
        if c_value == 0:
            return c
        # checking sign of c and a. If its different thats the range where we look for the root. c becomes new value for the range on the left side
        elif (c_value > 0) == (a_values > 0):
            a = c
        else:
            b = c

        iterations += 1
        if iterations > max_iterations:
            print("Exceeded maximum iterations, method may not converge")
            return None

    return (a + b) / 2


def newton_method(epsilon, a, b, c, d, max_iterations):
    # Starting with a zero of polynomial - ustalenie punktu startowego poprzez wyznaczenie miejsca zerowego
    x = calculate_polynomial(a, b, c, d, -b / (2 * a))
    x_value = calculate_polynomial(a, b, c, d, x)
    # obliczanie pochodnej by wyznaczyć kolejne przybliżenia pierwiastka równania
    derivative = calculate_derivative(a, b, c, d, x)

    iterations = 0  # iteration counter

    while abs(x_value) >= epsilon:
        if derivative == 0:  # If derivative is zero, Newton's method diverges, jesli nie jest zbieżna
            print("Derivative is zero, method diverges")
            return None
        elif iterations > max_iterations:  # iteration limit
            print("Exceeded maximum iterations, method may not converge")
            return None

        # new x value based on Newton pattern
        x = x - x_value / derivative
        x_value = calculate_polynomial(a, b, c, d, x)
        derivative = calculate_derivative(a, b, c, d, x)

        # check if function value is close to zero
        if abs(x_value) < epsilon:
            # root of multiplicity
            degree = 1
            while abs(calculate_polynomial(a, b, c, d, x + epsilon)) < epsilon:
                degree += 1
                x += epsilon
            print(f"Found a root of multiplicity {degree} at x = {x}")
            return x

        iterations += 1

    return x


def method_wrapper(method_name, epsilon, a, b, c, d, max_iterations):
    method_name = "Bisection" if method_name == bisection_method else "Newton"
    print(f"\n==================== {method_name} method ========================")

    if method_name == bisection_method:
        solution = bisection_method(a, b, c, d, epsilon, max_iterations)
    else:
        solution = newton_method(epsilon, a, b, c, d, max_iterations)

    if solution is not None:
        abs_error = abs(calculate_polynomial(a, b, c, d, solution))
        print(f"The approximate root is: {solution} ")
        print(f"The error is: {abs_error:.10f}")
    else:
        print("No solution was found")


precision = choose_precision()
a, b, c, d = parameters_input()
iteration_limit = set_iteration_limit()
# Równanie z jednym pierwiastkiem rzeczywistym
#     a = 1, b = -3, c = 3, d = -1

# Równanie z dwoma pierwiastkami rzeczywistymi
#     a = 1, b = -5, c = 6, d = 0

# Równanie bez pierwiastków rzeczywistych
#     a = 1, b = 0, c = 4, d = 5
# 1, -6, 4, -27
# pierwiastki wielokrotne: 1, -3, 3, -1
# błędy numeryczne: 1, -6, 12, -8
# przekroczenie limitu iteracji: 1, -1e6, 1e6, -1


time_taken = time_measurement(lambda: method_wrapper(bisection_method, precision, a, b, c, d, iteration_limit))
print(f"The time taken for calculation (bisection method) is: {time_taken: .5f} seconds")

time_taken = time_measurement(lambda: method_wrapper(newton_method, precision, a, b, c, d, iteration_limit))
print(f"The time taken for calculation (Newton's method) is: {time_taken: .5f} seconds")
