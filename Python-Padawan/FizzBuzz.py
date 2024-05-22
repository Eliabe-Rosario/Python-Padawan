def fizz_buzz(inicio, fim):
    for num in range(inicio, fim + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def main():
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))

    if fim <= inicio:
        print("Erro: O número final deve ser maior que o número inicial.")
        return

    fizz_buzz(inicio, fim)

if __name__ == "__main__":
    main()
