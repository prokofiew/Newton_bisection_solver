import time
import tkinter as tk
from tkinter import messagebox


def calculate_polynomial(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def calculate_derivative(a, b, c, d, x):
    return 3 * a * x ** 2 + 2 * b * x + c


# Funkcja do wyświetlania wyników
def display_results(method_name_1, solution_1, error_1, method_name_2, solution_2, error_2):
    result_window = tk.Toplevel()
    result_window.title("Results")

    result_label_1 = tk.Label(result_window, text=f"{method_name_1} Method Result:\nApproximate root: {solution_1}\nError: {error_1:.10f}")
    result_label_1.pack()

    result_label_2 = tk.Label(result_window, text=f"{method_name_2} Method Result:\nApproximate root: {solution_2}\nError: {error_2:.10f}")
    result_label_2.pack()

    back_button = tk.Button(result_window, text="Back", command=result_window.destroy)
    back_button.pack()

    result_window.mainloop()


def run_methods():
    precision = float(precision_choice.get())
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    d = float(d_entry.get())

    # Obliczenie wyników dla obu metod
    solution_bisection = bisection_method(a, b, c, d, precision)
    error_bisection = 0  # Domyślna wartość błędu

    if solution_bisection is not None:
        error_bisection = abs(calculate_polynomial(a, b, c, d, solution_bisection))

    solution_newton = newton_method(precision, a, b, c, d)
    error_newton = abs(calculate_polynomial(a, b, c, d, solution_newton))

    # Wyświetlenie wyników w jednym oknie
    display_results("Bisection", solution_bisection, error_bisection, "Newton", solution_newton, error_newton)

def parameters_validation():
    parameters_window = tk.Toplevel()
    parameters_window.title("Parameters Validation")

    a_label = tk.Label(parameters_window, text="Enter 'a' value:")
    a_label.pack()
    global a_entry
    a_entry = tk.Entry(parameters_window)
    a_entry.pack()

    b_label = tk.Label(parameters_window, text="Enter 'b' value:")
    b_label.pack()
    global b_entry
    b_entry = tk.Entry(parameters_window)
    b_entry.pack()

    c_label = tk.Label(parameters_window, text="Enter 'c' value:")
    c_label.pack()
    global c_entry
    c_entry = tk.Entry(parameters_window)
    c_entry.pack()

    d_label = tk.Label(parameters_window, text="Enter 'd' value:")
    d_label.pack()
    global d_entry
    d_entry = tk.Entry(parameters_window)
    d_entry.pack()

    submit_button = tk.Button(parameters_window, text="Submit", command=parameters_window.withdraw)
    submit_button.pack()
    back_button = tk.Button(parameters_window, text="Back", command=parameters_window.destroy)
    back_button.pack()

    parameters_window.mainloop()


def choose_precision():
    global precision_choice
    precision_window = tk.Toplevel()
    precision_window.title("Choose Precision")

    precision_label = tk.Label(precision_window, text="Choose precision level:")
    precision_label.pack()

    precision_values = ["0.1", "0.01", "0.001", "0.0001", "0.00001", "0.000001"]
    precision_choice = tk.StringVar()

    precision_dropdown = tk.OptionMenu(precision_window, precision_choice, *precision_values)
    precision_dropdown.pack()

    submit_button = tk.Button(precision_window, text="Submit", command=precision_window.withdraw)
    submit_button.pack()
    back_button = tk.Button(precision_window, text="Back", command=precision_window.destroy)
    back_button.pack()

    precision_window.mainloop()


def calculate_derivative(a, b, c, d, x):
    return 3 * a * x ** 2 + 2 * b * x + c


def time_measurement(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return round(end_time - start_time, 5)


def bisection_method(a, b, c, d, eps):
    f_a = calculate_polynomial(a, b, c, d, a)
    f_b = calculate_polynomial(a, b, c, d, b)

    if f_a == 0:
        return a
    elif f_b == 0:
        return b
    elif (f_b > 0) == (f_a > 0):
        print("No solution exists")
        return None

    while (b - a) >= eps:
        c = (a + b) / 2
        f_c = calculate_polynomial(a, b, c, d, c)

        if f_c == 0:
            return c
        elif (f_c > 0) == (f_a > 0):
            a = c
        else:
            b = c
    return (a + b) / 2


def newton_method(epsilon, a, b, c, d):
    x = calculate_polynomial(a, b, c, d, -b / (2 * a))  # Start with a reasonable initial guess
    f_x = calculate_polynomial(a, b, c, d, x)
    derivative = calculate_derivative(a, b, c, d, x)

    while abs(f_x) >= epsilon:
        if derivative == 0:  # If derivative is zero, newton's method diverges
            print("Derivative is zero, method diverges")
            return None
        x = x - f_x / derivative
        f_x = calculate_polynomial(a, b, c, d, x)
        derivative = calculate_derivative(a, b, c, d, x)

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
        print("The approximate root is: ", solution)
        print(f"The error is: {abs_error:.10f}")
    else:
        print("No solution was found")


root = tk.Tk()
root.title("Polynomial Solver")

label = tk.Label(root, text="Welcome to Polynomial Solver!", font=("Arial", 16))
label.pack()

parameters_button = tk.Button(root, text="Enter Parameters", command=parameters_validation)
parameters_button.pack()

precision_button = tk.Button(root, text="Choose Precision", command=choose_precision)
precision_button.pack()

run_button = tk.Button(root, text="Run Methods", command=run_methods)
run_button.pack()

exit_button = tk.Button(root, text="Exit program", command=root.quit)
exit_button.pack()

root.mainloop()
