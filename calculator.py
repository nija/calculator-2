"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
#import arithmetic
# Given a slist of tokens, process them and call the appropriate math function
def process_tokens(tokens):
    result = None
    if len(tokens) not in [2,3]:
        print "I don't understand"
    #if length is valid proceed:
    else:
        # It might be legit
        operation = tokens[0].lower()
        if operation == "+":
            result = add(int(tokens[1]), int(tokens[2]))
        elif operation == "-":
            result = subtract(int(tokens[1], int[2]))
        elif operation == "*":
            result = multiply(int(tokens[1], int[2]))
        elif operation == "/":
            result = divide(tokens[1], tokens[2])
        elif operation == "square":
            result = square(tokens[1])
        elif operation == "cube":
            result = cube(tokens[1])
        elif operation == "pow":
            result = power(float(tokens[1]), float(tokens[2]))
        elif operation == "mod":
            result = mod(int(tokens[1]), int(tokens[2]))
        # second exit condition   
        else:
            print "I will mock your mother with a limp fish"
    print "{}".format(result)


# Your code goes here
while True:
    # Get the input
    input = raw_input("> ")
    # Tokenize this baby
    tokens = input.split()
    
    process_tokens(tokens)