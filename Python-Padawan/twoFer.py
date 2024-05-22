def two_fer(name=None):
    if name:
        return f"Um para {name}, um para mim!"
    else:
        return "Um para você, um para mim!"

def main():
    name = input("Digite um nome (ou pressione Enter para nenhum): ").strip()
    print(two_fer(name))

if __name__ == "__main__":
    main()
