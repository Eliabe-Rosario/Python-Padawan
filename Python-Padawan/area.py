import math

def calcular_area_circunferencia(raio):
    pi = 3.14159265
    area = pi * raio ** 2
    return area

def main():
    raio = float(input("Digite o valor do raio da circunferência: "))

    area = calcular_area_circunferencia(raio)

    print("A área da circunferência é:", area)

if __name__ == "__main__":
    main()
