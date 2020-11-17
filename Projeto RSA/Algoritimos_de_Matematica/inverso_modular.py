
# Encontra o valor do inverso modular de dois números utilizando força bruta,

# O correto em RSA é utilizar o Algoritmo de Euclides estendido para para encontrar o vaor do inverso modular de uma forma muito mais eficiente.


def inversoModular(a, b):
    a = a % b
    for i in range(1, b): 
        if ((a * i) % b == 1): 
            return i