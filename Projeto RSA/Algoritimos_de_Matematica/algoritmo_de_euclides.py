
# Encontra o minimo divisor comum de dois números.

def mdc(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x