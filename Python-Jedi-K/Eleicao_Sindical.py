def calcular_percentuais(votos_a, votos_b, votos_c, nulos, em_branco, total):
    percentual_votos_validos = ((votos_a + votos_b + votos_c) / total) * 100
    percentual_a = (votos_a / total) * 100
    percentual_b = (votos_b / total) * 100
    percentual_c = (votos_c / total) * 100
    percentual_nulos = (nulos / total) * 100
    percentual_em_branco = (em_branco / total) * 100
    return percentual_votos_validos, percentual_a, percentual_b, percentual_c, percentual_nulos, percentual_em_branco

def apresentar_resultados(total, percentual_votos_validos, percentual_a, percentual_b, percentual_c, percentual_nulos, percentual_em_branco):
    print("\nRESULTADOS DA VOTAÇÃO:")
    print("Número total de eleitores:", total)
    print("Percentual de votos válidos em relação à quantidade de eleitores: {:.2f}%".format(percentual_votos_validos))
    print("Percentual de votos válidos para o candidato A em relação à quantidade de eleitores: {:.2f}%".format(percentual_a))
    print("Percentual de votos válidos para o candidato B em relação à quantidade de eleitores: {:.2f}%".format(percentual_b))
    print("Percentual de votos válidos para o candidato C em relação à quantidade de eleitores: {:.2f}%".format(percentual_c))
    print("Percentual de votos nulos em relação à quantidade de eleitores: {:.2f}%".format(percentual_nulos))
    print("Percentual de votos em branco em relação à quantidade de eleitores: {:.2f}%".format(percentual_em_branco))

def main():
    votos_a = int(input("Digite a quantidade de votos válidos para o candidato A: "))
    votos_b = int(input("Digite a quantidade de votos válidos para o candidato B: "))
    votos_c = int(input("Digite a quantidade de votos válidos para o candidato C: "))

    nulos = int(input("Digite a quantidade de votos nulos: "))
    em_branco = int(input("Digite a quantidade de votos em branco: "))

    total = votos_a + votos_b + votos_c + nulos + em_branco

    percentuais = calcular_percentuais(votos_a, votos_b, votos_c, nulos, em_branco, total)

    apresentar_resultados(total, *percentuais)

if __name__ == "__main__":
    main()
