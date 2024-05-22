def calcular_media_e_status():
    print("CÁLCULO DA MÉDIA DO ALUNO")

    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("A média do aluno é:", media)

    if media >= 5:
        print("Aprovado")
    else:
        print("Reprovado")

calcular_media_e_status()
