def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Teste do código
numero = int(input("Digite um número: "))
if is_prime(numero):
    print(numero, "é um número primo")
else:
    print(numero, "não é um número primo")
