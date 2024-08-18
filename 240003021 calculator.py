#Atharva Chavan 240003021
#Basic Caluclator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result


def sin_t(x, terms=50):
    sin_x = 0
    for n in range(terms):
        sign = (-1) ** n
        exponent = 2 * n + 1
        term = sign * power(x, exponent) / factorial(exponent)
        sin_x += term
    return sin_x


def cos_t(x, terms=10):
    cos_x = 0
    for n in range(terms):
        sign = (-1) ** n
        exponent = 2 * n
        term = sign * power(x, exponent) / factorial(exponent)
        cos_x += term
    return cos_x


def linear_2_var(a1, b1, c1, a2, b2, c2):
    D = (a1 * b2) - (a2 * b1)
    if D == 0:
        return "The system has no unique solution (D=0)."

    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    x = Dx / D
    y = Dy / D
    return x, y


def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "No real solution"

    sqrt_d = d ** 0.5
    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)
    return root1, root2

def calc():
    while True:
        print("\nSelect operation to perform")
        operation = int(input("\nPress a key to perform operation\n"
                              "1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE\n5. Solve a linear equation\n6. Solve a quadratic equation\n7. Logarithmic Function\n8. Trigonometric Functions\n9. Exit\n\n"))

        if operation == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            ans = num1 + num2
            print("The sum is " + str(ans))

        elif operation == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            ans = num1 - num2
            print("The difference is " + str(ans))

        elif operation == 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            ans = num1 * num2
            print("The product is " + str(ans))

        elif operation == 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 != 0:
                ans = num1 / num2
                print("The quotient is " + str(ans))
            else:
                print("Error: Division by zero ")

        elif operation == 5:
            opt = int(input("\n1. Linear Eqn in 2 variables\n2. Linear Eqn in 3 variables\n"))
            if opt == 1:
                print("Arrange the equation in the format shown below and enter the values ")
                print("a1x + b1y = c1")
                print("a2x + b2y = c2")
                a1 = float(input("\na1= "))
                b1 = float(input("\nb1= "))
                c1 = float(input("\nc1= "))
                a2 = float(input("\na2= "))
                b2 = float(input("\nb2= "))
                c2 = float(input("\nc2= "))
                result = linear_2_var(a1, b1, c1, a2, b2, c2)
                if isinstance(result, tuple):
                    print(f"The solution is (x, y) = ({result[0]}, {result[1]})")
                else:
                    print(result)

            elif opt == 2:
                print("Solving linear equations in 3 variables is not yet implemented.")

        elif operation == 6:
            print("Please arrange the quadratic equation in the format shown below and enter the values")
            print("ax^2 + bx + c = 0")
            a = float(input("\na= "))
            b = float(input("\nb= "))
            c = float(input("\nc= "))
            result = quadratic(a, b, c)
            if isinstance(result, tuple):
                print(f"The solutions are: {result[0]} and {result[1]}")
            else:
                print(result)

        elif operation == 7:
            def exp_taylor(x, terms=50):
                result = 1.0  # e^0 = 1
                term = 1.0
                for n in range(1, terms):
                    term *= x / n
                    result += term
                return result

            def ln_newton(y, tolerance=1e-10, max_iterations=1000):
                if y <= 0:
                    raise ValueError("Logarithm undefined")

                x = y  # Initial guess
                iteration = 0

                while iteration < max_iterations:
                    exp_x = exp_taylor(x)  # Compute e^x using Taylor series
                    f_x = exp_x - y
                    f_prime_x = exp_x

                    x_next = x - f_x / f_prime_x

                    if abs(x_next - x) < tolerance:
                        return x_next

                    x = x_next
                    iteration += 1

                raise ValueError("error.")

            y = float(input("entr number"))

            ln_y = ln_newton(y)
            log10 = ln_y / 2.303
            print(f"Natural logarithm of {y} is approximately {ln_y}\n And the value for log to base 10 is {log10}")

        elif operation == 8:
            function = int(input("1. Sin\n2. Cosine\n3. Tangent\n4. Sec\n5. Cosec\n6. Cot\n"))
            x = float(input("Enter angle in radians: "))

            if function == 1:
                print(f"Result: {sin_t(x)}")
            elif function == 2:
                print(f"Result: {cos_t(x)}")
            elif function == 3:
                cos_x = cos_t(x)
                if cos_x != 0:
                    tan_x = sin_t(x) / cos_x
                    print(f"Result: {tan_x}")
                else:
                    print("Error Division by zero in tangent calculation.")
            elif function == 4:
                cos_x = cos_t(x)
                if cos_x != 0:
                    sec_x = 1 / cos_x
                    print(f"Result: {sec_x}")
                else:
                    print("Error Division by zero in secant calculation.")
            elif function == 5:
                cos_x = cos_t(x)
                if cos_x != 0:
                    cosec_x = 1 / cos_x
                    print(f"Result: {cosec_x}")
                else:
                    print("Error Division by zero in cosecant calculation.")
            elif function == 6:
                sin_x = sin_t(x)
                if sin_x != 0:
                    cot_x = cos_t(x) / sin_x
                    print(f"Result: {cot_x}")
                else:
                    print("Error: Division by zero")
            else:
                print("Invalid entry")

        elif operation == 9:
            print("Exiting the calculator.")
            break

        else:
            print("\n\nINVALID entry\n\n")

        continue_choice = input("\nDo you want to continue? (yes/no): ")
        if continue_choice != 'yes':
            print("Exiting the calculator.")
            break

if __name__ == "__main__":
    calc()

