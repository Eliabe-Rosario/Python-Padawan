def calcular_novo_salario(salario, percentual_reajuste):
    novo_salario = salario * (1 + percentual_reajuste / 100)
    return novo_salario

def main():
    
    salario = float(input("Digite o salário atual do trabalhador: "))
    percentual_reajuste = float(input("Digite o percentual de reajuste a ser aplicado: "))

 
    novo_salario = calcular_novo_salario(salario, percentual_reajuste)


    print("O novo salário após o reajuste é:", novo_salario)

if __name__ == "__main__":
    main()
