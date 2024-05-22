def jokenpo(jogada1, jogada2):
    if jogada1 == jogada2:
        return "Empate"
    elif (jogada1 == 1 and jogada2 == 3) or (jogada1 == 3 and jogada2 == 2) or (jogada1 == 2 and jogada2 == 1):
        return "Jogador 1 vence"
    else:
        return "Jogador 2 vence"

# Mapeamento de jogadas para números
opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

# Teste do código
print("Opções de jogadas:")
for numero, jogada in opcoes.items():
    print(f"{numero}: {jogada}")

jogador1 = int(input("Jogador 1, escolha o número correspondente à sua jogada: "))
jogador2 = int(input("Jogador 2, escolha o número correspondente à sua jogada: "))

print("Resultado:", jokenpo(jogador1, jogador2))

