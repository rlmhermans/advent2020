import re

with open('input') as f:
    input = f.readlines()

def evaluate(expression, operator): 
    while operator in expression:
        subs = re.findall(f'(\d+ [\{operator}] \d+)', expression)
        for sub in subs:
            expression = expression.replace(sub, str(eval(sub)), 1)

    return expression

def solve(expression):
    while '(' in expression:
        subs = re.findall('(\([\+\* \d]+\))', expression)
        for sub in subs:
            expression = expression.replace(sub, solve(sub[1:-1]), 1)

    expression = evaluate(expression, '+')
    expression = evaluate(expression, '*')

    return expression

print('Sum of all results: ', sum(int(solve(expr)) for expr in input))