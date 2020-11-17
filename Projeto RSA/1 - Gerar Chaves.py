import sys
sys.path.append('C:/Projeto RSA/Algoritimos_de_Matematica')
from teoria_de_fermat import teste_de_fermat
from teste_de_primo import e_primo
from gerador_de_primos import gerador_de_primo
from algoritmo_de_euclides import mdc
from primos_entre_si import e_primos_entre_si
from inverso_modular import inversoModular



def main():
    n = 12 # Expoente do gerador de primos 2^12
    p = gerador_de_primo(n) # Primeiro número primo
    q = gerador_de_primo(n) # Segundo número primo
    N = p * q # Quociente de p e q
    phiN = (p - 1) * (q - 1) # Função Totiente de Euler's

    while True:
        e = gerador_de_primo(n) # Variavél "e" tem que ser co-primo com phiN
        if e_primos_entre_si(e, phiN):
            break
            return e

    d = inversoModular(e, phiN) # Variavél "d" é o valor do Inverso Modular de "e" e phiN

    Valor_N = open ('C:/Projeto RSA/Chaves Públicas/Valor de N.txt', 'w', encoding='utf-8')
    Valor_N.write(str(N))
    Valor_N.close


    Valor_e = open ('C:/Projeto RSA/Chaves Públicas/Valor de e.txt', 'w', encoding='utf-8')
    Valor_e.write(str(e))
    Valor_e.close


    Valor_d = open ('C:/Projeto RSA/Chaves Privadas/Valor de d.txt', 'w', encoding='utf-8')
    Valor_d.write(str(d))
    Valor_d.close




main()


