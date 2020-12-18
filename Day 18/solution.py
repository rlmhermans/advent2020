import re

with open('input') as f:
    input = f.readlines()

def evaluate(expression, operator):
    complete = False    
    while not complete:
        subs = re.findall(f'(\d+ [\{operator}] \d+)', expression)
        if not subs:
            complete = True
        else:
            for sub in subs:
                expression = expression.replace(sub, str(eval(sub)), 1)

    return expression

def solve(expression):
    complete = False    
    while not complete:
        subs = re.findall('(\([\+\* \d]+\))', expression)
        if not subs:
            complete = True
        else:
            for sub in subs:
                expression = expression.replace(sub, solve(sub[1:-1]), 1)

    expression = evaluate(expression, '+')
    expression = evaluate(expression, '*')

    return expression

print('Sum of all results: ', sum(int(solve(expr)) for expr in input))