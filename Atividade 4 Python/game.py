import random

def main():
    while True:
        try:
            nivel = int(input("Digite o nível de dificuldade (um número entre 1 e 100): "))
            if 1 <= nivel <= 100:
                break
            else:
                print("Por favor, insira um número entre 1 e 100.")
        except ValueError:
            print("Por favor, insira um número válido.")
    numero_secreto = random.randint(1, nivel)

    while True:
        try:
            palpite = int(input("Adivinhe o número: "))
            if palpite < 1:
                print("Por favor, insira um número positivo.")
            elif palpite < numero_secreto:
                print("Pequeno demais!")
            elif palpite > numero_secreto:
                print("Grande demais!")
            else:
                print("Correto!")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()