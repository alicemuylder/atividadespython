emoji_dict = {
    ":thumbs_up:": "👍",
    ":thumbsup:": "👍",
    ":smile:": "😊",
    ":heart:": "❤️",
    ":pizza:": "🍕",
}

def emojize_string(texto):
    for code, emoji in emoji_dict.items():
        texto = texto.replace(code, emoji)
    return texto

def main():
    texto = input("Digite uma string em inglês: ")
    emojized_text = emojize_string(texto)
    print(emojized_text)

if __name__ == "__main__":
    main()