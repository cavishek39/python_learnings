"""
    A simple finding factorial of a number program.
"""
def factroial(number):
    if (number == 0 or number == 1):
        return 1
    else:
       return number * factroial(number - 1)

print(factroial(5))

"""
    The famous Stack over flow problem
"""

# def stack_over_flow():
#     print("DEL")
#     stack_over_flow()

# stack_over_flow()