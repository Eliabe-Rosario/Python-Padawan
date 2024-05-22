def scrabble_score(palavra):
    pontuacoes = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    palavra = palavra.upper()

    escore = 0
    for letra in palavra:
        if letra in pontuacoes:
            escore += pontuacoes[letra]

    return escore


palavra = input("Digite uma palavra para calcular o escore no Scrabble: ")


print("O score da palavra '{}' é: {}".format(palavra, scrabble_score(palavra)))
