def main():
    lista_de_compras = []
    print("Crie sua lista de compras. Digite um item por linha e pressione Ctrl+D para finalizar:")

    while True:
        try:
            item = input()
            lista_de_compras.append(item)
        except EOFError:
            break

    lista_de_compras = [item.strip().upper() for item in lista_de_compras]
    lista_de_compras.sort()

    for item in lista_de_compras:
        print(item)

if __name__ == "__main__":
    main()