def remove_vogais(texto):
    texto_sem_vogais = ""
    for char in texto:
        if char.lower() not in "aeiou":
            texto_sem_vogais += char
    return texto_sem_vogais

def main():
    texto = input("Digite um texto: ")
    texto_sem_vogais = remove_vogais(texto)
    print(f"Texto sem vogais: {texto_sem_vogais}")

if __name__ == "__main__":
    main()