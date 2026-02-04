# 1 - Soma os números
def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x,y):
    if y != 0:
        return x / y
    else:
        raise ValueError ("Não é Permitido divisão por zero!")