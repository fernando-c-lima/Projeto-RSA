from algoritmo_de_euclides import mdc

# Utilizando o algoritmo de euclides, garantimos que dois números são primos entre si quando o MDC deles é = 1.

def e_primos_entre_si(a, b):
    x = mdc(a, b) == 1
    return x