from test_framework import generic_test

# prefix notation, polish notation, +12
# infix expression, 1+2
# postfix notation, reverse polish notation, 12-
# where prefix and postfix expressions can be evaluated by stack
# the following algo is for postfix expression
# for prefix expression, read tokens from right to left
# then follow the operand, operand, operator pattern

# from book, simple
def second(expression):
    result = []
    OPERATORS = {
        '+': lambda v1, v2: v1 + v2,
        '-': lambda v1, v2: v2 - v1,
        '*': lambda v1, v2: v1 * v2,
        '/': lambda v1, v2: v2 // v1,
    }

    for token in expression.split(','):
        if token in OPERATORS:
            result.append(OPERATORS[token](result.pop(), result.pop()))
        else:
            result.append(int(token))

    return result[-1]

def first(expression):
    class Calculator:
        def __init__(self):
            self.stack = []

        def input(self, op):
            if op == '+':
                v1 = self.stack.pop()
                v2 = self.stack.pop()
                self.stack.append(v1 + v2)
            elif op == '-':
                v1 = self.stack.pop()
                v2 = self.stack.pop()
                self.stack.append(v2 - v1)
            elif op == '*':
                v1 = self.stack.pop()
                v2 = self.stack.pop()
                self.stack.append(v1 * v2)
            elif op == '/':
                v1 = self.stack.pop()
                v2 = self.stack.pop()
                self.stack.append(v2 // v1)
            else:
                self.stack.append(int(op))

        def get_value(self):
            return self.stack.pop()

    calculator = Calculator()
    while expression:
        p = expression.partition(',')
        calculator.input(p[0])
        expression = p[2]
    
    return calculator.get_value()
    

def evaluate(expression):
    # return first(expression)
    return second(expression)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
