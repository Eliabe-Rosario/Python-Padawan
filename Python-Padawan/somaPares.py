def soma_pares_intervalo(inicio, fim):
    soma = 0
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            soma += num
    return soma

def main():
    inicio = int(input("Digite o primeiro valor: "))
    fim = int(input("Digite o segundo valor: "))

    soma_pares = soma_pares_intervalo(inicio, fim)

    print("A soma dos números pares no intervalo é:", soma_pares)

if __name__ == "__main__":
    main()
