"""
Gunnar Bachmann
9/4/2019
roots.py
Write a function that computes the real roots of a quadratic equation,
prints the equation and the number of roots.
"""
import math


def quadratic_roots(a, b, c):
    """
    quadratic_roots is a function that computes real roots of a
    quadratic equation, prints the equation and the number of roots.

    Using an if statement, the function will run by first checking the
    number of roots using the num_of_roots variable (b**2 - 4*a*c).
    Then, depending on whether the answer is positive, negative, or
    equal to zero... the function will find the values of the
    roots, and print the equation, number of roots, and the value
    of the roots.

    Positive = Two roots
    Equal to zero = One root
    Negative = No roots

    :param a:
    :param b:
    :param c:
    :return:
    """
    num_of_roots = (b**2)-(4*a*c)
    #quad_add = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
    #quad_sub = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)

    if num_of_roots > 0:
        x1 = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
        print(str(a), "x^2 + ", str(b), "x + ", str(c), " = 0", sep="")
        print("Two roots.")
        print("x = ", str(x1))
        print("x = ", str(x2))
    elif num_of_roots == 0:
        x1 = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
        print("Equation: ",str(a), "x^2 + ", str(b), "x + ", str(c), " = 0", sep="")
        print("One root.")
        print("x = ", str(x1))
    elif num_of_roots < 0:
        print("Equation: ", str(a), "x^2 + ", str(b), "x + ", str(c), " = 0", sep="")
        print("No roots.")


def test():
    """
    This function runs 10 tests that try different combinations
    of categories of a, b, and c and produce different kinds of
    results.
    In the comments at the end of the function is an bonus test case
    just in case, to test and show that the quadratic_roots function
    does not work when a=0.
    :return:
    """
    print("1:")
    quadratic_roots(1, -3, 4) #1 - No roots (a and c are positive. b is negative)
    print("\n")
    print("2:")
    quadratic_roots(5, 50, 1000) #2 - No roots (a < b < c)
    print("\n")
    print("3:")
    quadratic_roots(15, 0, 10) #3 - No roots (a and c are positive. b is negative)
    print("\n")
    print("4:")
    quadratic_roots(-4, 12, -9) #4 - One root (a and c are negative)
    print("\n")
    print("5:")
    quadratic_roots(2, 4, 2) #5 - One root (a and c are the same number)
    print("\n")
    print("6:")
    quadratic_roots(-5, -10, -5) #6 - One root (a, b, and c are negative)
    print("\n")
    print("7:")
    quadratic_roots(2, -11, 5) #7 - Two roots (b is a negative. a and c are positive)
    print("\n")
    print("8:")
    quadratic_roots(130, 50, 2) #8 - Two roots (a is the largest number)
    print("\n")
    print("9:")
    quadratic_roots(15, 0, -10) #9 - Two roots (a is a positive, b is zero, c is a negative)
    print("\n")
    print("10:")
    quadratic_roots(5, 5, 5) #10 - No roots (all same number)
    """
    print("\n")
    print("Bonus:")
    quadratic_roots(0, 10, 15) #bonus - crashes because a=0 and it gives a ZeroDivisionError. Told to ignore this issue.
    """


if __name__ == '__main__':
    """
    Main function: Let's the user know by using a print statement that
    we are running 10 tests to test the quadratic_roots function. Then
    it will print the 10 tests to the user. Following that, the user will
    be asked to input a value for a, b, and c. After that, quadratic_roots
    is run with the numbers inputted by the user.
    """
    print("Running 10 tests...")
    test()
    print("--------------------------------------")
    a = int(input("Enter a number for a: "))
    b = int(input("Enter a number for b: "))
    c = int(input("Enter a number for c: "))
    print("\n")
    quadratic_roots(a, b, c)