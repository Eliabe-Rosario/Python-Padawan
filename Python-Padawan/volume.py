def calcular_volume_caixa(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume

def main():
    comprimento = float(input("Qual o comprimento da caixa? "))
    largura = float(input("Qual a largura da caixa? "))
    altura = float(input("Qual a altura da caixa? "))

    volume = calcular_volume_caixa(comprimento, largura, altura)

    print("Esse é o volume da caixa:", volume)

if __name__ == "__main__":
    main()
