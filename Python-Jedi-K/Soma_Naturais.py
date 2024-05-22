def solicitar_numeros():
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))
    return inicio, fim

def calcular_soma_intervalo(inicio, fim):
    soma = sum(range(inicio, fim + 1))
    return soma

def exibir_resultado(inicio, fim, soma):
    print("Intervalo: de", inicio, "a", fim)
    print("Soma dos números no intervalo:", soma)

def main():
    inicio, fim = solicitar_numeros()
    soma = calcular_soma_intervalo(inicio, fim)
    exibir_resultado(inicio, fim, soma)

if __name__ == "__main__":
    main()
