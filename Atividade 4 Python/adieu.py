def main():
    nomes = []

    print("Digite os nomes, um por linha. Pressione Ctrl+D para finalizar.")

    while True:
        try:
            nome = input()
            nomes.append(nome)
        except EOFError:
            break

    for i, nome in enumerate(nomes, start=1):
        if i == 1:
            print(f"Adieu, adieu, to {nome}")
        else:
            adieu_line = f"Adieu, adieu, to {', '.join(nomes[:i - 1])}, and {nome}"
            print(adieu_line)

if __name__ == "__main__":
    main()