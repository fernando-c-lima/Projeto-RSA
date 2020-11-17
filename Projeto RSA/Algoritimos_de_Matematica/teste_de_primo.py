from teoria_de_fermat import teste_de_fermat

# O teste de primaidade de Fermat não é 100% efetivo pois existem números falsos primos que podem passar pelo teste, para ter certeza que o número é primo
# vamos testa-lo 20 vezes para reduzir muito as chances do número não ser primo e passar como verdadeiro.

def e_primo(p):
    for i in range(20):
        if not teste_de_fermat(p):
            return False
    return True