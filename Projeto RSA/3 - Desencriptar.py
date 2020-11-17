import sys

# A função "desencriptar", vai desencriptar cada letra encriptada pela função de RSA, e transforma-lo de volta em uma letra utilizando a função "chr"
# Para desencriptar vamos utilizar a seguinte função: chr(letra^d % N) 
# Que vai nos retornar uma letra ou espaço e adiciona-lo em uma lista para cada letra desencriptada e adicionar em um .txt

def desencriptar(d, N, cifrado):    
    texto_decifrado = []
    texto = cifrado.split()
    for letra in texto:
        caractere = int(letra)
        letra_descriptada = chr(pow(caractere, d, N))
        texto_decifrado.append(letra_descriptada)
    return texto_decifrado


def main():


    Valor_N = open('C:/Projeto RSA/Chaves Públicas/Valor de N.txt', encoding='utf-8')
    for valor in Valor_N:
        N = int(valor)
        Valor_N.close

    Valor_d = open('C:/Projeto RSA/Chaves Privadas/Valor de d.txt', encoding='utf-8')
    for valor in Valor_d:
        d = int(valor)
        Valor_d.close

    Texto_Cifrado = open('C:/Projeto RSA/Texto Encriptado/Texto Cifrado.txt', encoding='utf-8')
    for letra in Texto_Cifrado:
        cifrado = letra
        Texto_Cifrado.close

    Desencriptar = desencriptar(d, N, cifrado)

    sys.stdout = open("C:/Projeto RSA/Texto Descriptografado/Texto Descriptografado.txt", "w", encoding='utf-8')

    print(*Desencriptar, sep = "")

    sys.stdout.close()
    


main()

