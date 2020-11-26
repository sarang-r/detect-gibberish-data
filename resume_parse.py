def func1(x):
    

    return x + 1

def func2(x):

    return x+ 3


def operator_func(func, x):

    result = func(x)
    return result

print(operator_func(func2,3))
