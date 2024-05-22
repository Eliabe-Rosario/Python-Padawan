def solicitar_numeros():
    numeros = []
    for i in range(12):
        numero = int(input("Digite o {}º número inteiro: ".format(i + 1)))
        numeros.append(numero)
    return numeros

def ordenar_decrescente(numeros):
    numeros.sort(reverse=True)
    return numeros

def exibir_ordem_decrescente(numeros):
    print("Elementos ordenados em ordem decrescente:")
    for numero in numeros:
        print(numero, end=" ")

def main():
    numeros = solicitar_numeros()
    numeros_ordenados = ordenar_decrescente(numeros)
    exibir_ordem_decrescente(numeros_ordenados)

if __name__ == "__main__":
    main()
