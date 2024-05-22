def calcular_velocidade():
    print("CALCULAR VELOCIDADE")
    distancia = float(input("Digite a distâcia em kms: "))
    tempo = float(input("Digite o tempo em minutos: "))

    distancia_metros = distancia * 1000
    
    tempo_segundos = tempo * 60

    velocidade = distancia_metros / tempo_segundos
    
    print("A velocidade é de:", velocidade, "m/s")

calcular_velocidade()
