import itertools
from ex03_boolean_evaluation import boolean_eval


def sat(formula: str) -> bool:
    variables = sorted(set(c for c in formula if c.isupper()))
    
    for values in itertools.product([False, True], repeat=len(variables)):
        env = dict(zip(variables, values))
        
        rpn_eval = ''
        for c in formula:
            if c.isupper():
                rpn_eval += '1' if env[c] else '0'
            else:
                rpn_eval += c
        
        
        if boolean_eval(rpn_eval):
            return True
    return False



tests = ["AB|", "AB&", "AA!&", "AA^"]
for t in tests:
    print(f"{t} -> {sat(t)}")