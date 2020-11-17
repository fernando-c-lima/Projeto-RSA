
# Teste de primalidade de Fermat para achar números primos.

def teste_de_fermat(p):
    a = 10
    if pow(a, p-1, p) != 1:
        return False
    return True
    