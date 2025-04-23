import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def divide(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


should_repeat= True
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while should_repeat= True:

    n1 = float(input("What's the first number?: "))
    print(f"+\n-\n*\n/")
    op = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))

    print(n1, op, n2, "=", operations[op](n1, n2))
    if_continue = input(
        f'Type "y" to continue calculating with {operations[op](n1,n2)}, or type "n" to start a new calculation: '
    )
    while if_continue == "y":
        n1 = operations[op](n1, n2)
        print(f"+\n-\n*\n/")
        op = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        print(n1, op, n2, "=", operations[op](n1, n2))
        if_continue = input(
            f'Type "y" to continue calculating with {operations[op](n1,n2)}, or type "n" to start a new calculation: '
        )
