def printRecrusive(num):
    if num <= 10:
        print(num)
        printRecrusive(num+1)

printRecrusive(1)

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print(fibonacci(10))  