import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0

        while True:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    print("Correto!")
                    score += 1
                    break
                else:
                    attempts += 1
                    if attempts < 3:
                        print("EEE")
                    else:
                        print(f"Resposta correta: {correct_answer}")
                        break
            except ValueError:
                print("EE")
    
    print(f"Pontuação: {score} de 10")

def get_level():
    while True:
        try:
            level = int(input("Escolha o nível (1, 2, ou 3): "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        print("Por favor, escolha um nível válido.")

def generate_integer(level):
    min_value = 10 ** (level - 1)
    max_value = 10 ** level - 1
    return random.randint(min_value, max_value)

if __name__ == "__main__":
    main()
