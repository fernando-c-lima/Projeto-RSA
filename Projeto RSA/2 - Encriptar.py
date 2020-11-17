import sys

# A função "encriptar" vai encriptar cada letra de nossa mensagem, utilizando a função ord vamos converter cada letra da mensagem em um número,
# então aplicar a seguinte função de RSA: ord(letra)^e % N, 
# O progama vai rodar e adicionar cada letra ou espaço encriptado em uma lista e salva-lo em um .txt

def encriptar(N, e, texto):
    texto_cifrado = []
    for letra in texto:
        caractere = ord(letra)
        letra_encriptada = pow(caractere, e, N)
        texto_cifrado.append(letra_encriptada)
    return texto_cifrado


def main():

    texto = str(input("Mensagem secreta: "))
    
    Valor_N = open('C:/Projeto RSA/Chaves Públicas/Valor de N.txt', encoding='utf-8')
    for valor in Valor_N:
        N = int(valor)
        Valor_N.close
    
    Valor_e = open('C:/Projeto RSA/Chaves Públicas/Valor de e.txt', encoding='utf-8')
    for valor in Valor_e:
        e = int(valor)
        Valor_e.close

    texto_encriptado = encriptar(N, e, texto)

    sys.stdout = open("C:/Projeto RSA/Texto Encriptado/Texto Cifrado.txt", "w", encoding='utf-8') 

    print(*texto_encriptado, sep = " ")

    # Para o progama de desencriptação funcionar corretamente, nosso .txt não pode conter nenhuma formatação de uma lista como "" ou , então utiliza-mos a função sys.stdout para
    # formatar de uma forma que sejá válida.

    sys.stdout.close()




main()
