from teste_de_primo import e_primo
from random import randint

# Utiliza o Pequeno Teorema de Fermat para garantir que o número gerado é primo.

def gerador_de_primo(n):
    while True:
        p = randint(2**(n-1), 2**n)
        if e_primo(p):
            return p