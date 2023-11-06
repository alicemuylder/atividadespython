frutas = {
    "apple": "52 calorias por porção",
    "banana": "89 calorias por porção",
    "orange": "62 calorias por porção",
    "grapes": "69 calorias por porção",
    "strawberries": "32 calorias por porção",

}

def main():
    fruta = input("Digite o nome de uma fruta: ").lower()

    if fruta in frutas:
        print(f"Informações nutricionais da {fruta}: {frutas[fruta]}")
    else:
        print("Desculpe, não temos informações nutricionais para essa fruta.")

if __name__ == "__main__":
    main()