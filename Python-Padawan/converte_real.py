

def conversao_real():
    cotacao_dolar = float(input("Digite a cotação do Dolar: ").replace(',', '.'))
    quantidade_dolares = float(input("Digite a quantidade em dolares: ").replace(',', '.'))
    valor_conversao = quantidade_dolares * cotacao_dolar
    print(f"O valor da conversão em reais é: R${valor_conversao:.2f}")

conversao_real()
