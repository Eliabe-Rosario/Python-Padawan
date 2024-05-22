

def conversao_dolar():
    cotacao_dolar = float(input("Digite a cotação do Dolar: ").replace(',', '.'))
    quantidade_reais = float(input("Digite a quantidade em reais: ").replace(',', '.'))
    valor_conversao = quantidade_reais / cotacao_dolar
    print(f"O valor da conversão em dolar é: US$ {valor_conversao:.2f}")

conversao_dolar()
