import math
import random

fact_dict = dict()
mod_dict = dict()
ans_dict = dict()

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    # v = math.pow(x, y)
    # v = math.factorial(v)
    # v //= (x + y)
    # v %= 982451653
    
    # create dicts to store all of the possible values
    # - factorials
    # - modulo
    # - answer value of v
    global fact_dict, mod_dict, ans_dict

    # if the x,y pair exists in the dict, return the value
    if ans_dict.get(str(x) + ',' + str(y)):
        return ans_dict[str(x) + ',' + str(y)]

    # otherwise, do the following sets of calculations:

    # 0
    # compute power of x, y
    v = math.pow(x,y)

    # 1
    # if v exists in the fact dict, return value of v
    if fact_dict.get(v):
        v = fact_dict(v)
    # else, do the calculation, store in the fact dict, then return v
    else:
        v = math.factorial(v)
        fact_dict[v] = v

    # 2
    v //= (x+y)

    # 3
    # if v exists in the mod dict, return value of v
    if mod_dict.get(v):
        v = mod_dict[v]
    # else, do the ccalculation, store in mod dict, then return v
    else:
        v %= 982451653 
        mod_dict[v] = v

    ans_dict[str(x) + ',' + str(y)] = v
    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
