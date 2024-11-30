"""Contains my custom Python functions and exercises."""


def addition():
    """Return the sum of two numbers."""
    a = (input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    print("Your result is", c)
    return None


def new_addition(a, b):
    """Return the sum of two numbers."""
    c = a + b
    print("Your result is", c)
    return None


def square():
    """Return the square of the argument."""
    a = int(input("enter number: "))
    b = a**2
    print("your result is", b)
    return b


def find_min(my_list):
    """Find the min."""

    minimum = min(my_list)
    # maximum = max("number")

    print("The minimum value is", minimum)
    return minimum


def computepay(hours: int, rate: float):
    """Compute daily gross pay given the number of hours worked and 
    pay per hour"""
    
    try:
        # Calculating daily gross pay
        daily_gross_pay = hours * rate
        print(f"Your daily gross pay is: ${daily_gross_pay:.2f}")

    except:
        print("an error occurred")

    return daily_gross_pay


# new_addition(2, 5)
# addition()
# square()
# find_min([5, 4, 33, 41, 30, 23, 3, 44])
