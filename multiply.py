#Title:-
def multiply(num1, num2):
    """this function takes two positive integers as parameters and returns the product of those two numbers """
    if num2 == 0:
        return 0
    else:
        return num1 + multiply(num1, num2 - 1)

#first = int(input("Enter a positive integer: "))
#second = int(input("Enter another positive integer: "))
#print("Product of", first, "and", second, "is =", multiply(first, second))


