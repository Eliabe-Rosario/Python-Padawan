def verificar_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

entrada = input("Digite uma palavra, frase ou número para verificar se é um palíndromo: ")


if verificar_palindromo(entrada):
    print(f"A entrada '{entrada}' é um palíndromo.")
else:
    print(f"A entrada '{entrada}' não é um palíndromo.")
