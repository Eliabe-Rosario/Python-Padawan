def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número para calcular seu fatorial: "))

if numero < 0:
    print("Erro: O fatorial é definido apenas para números não negativos.")
else:
    resultado = calcular_fatorial(numero)
    print("O fatorial de {} é: {}".format(numero, resultado))
