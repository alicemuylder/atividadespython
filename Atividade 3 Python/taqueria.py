menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    pedido = []
    custo_total = 0.00

    print("Bem-vindo à Taqueria do Felipe! Faça seu pedido:")

    while True:
        try:
            item = input().title()
            if item in menu:
                custo_total += menu[item]
                pedido.append(item)
            else:
                print("Item não encontrado no menu. Por favor, escolha um item válido.")
        except EOFError:
            break

    if pedido:
        print("Seu pedido:")
        for item in pedido:
            print(f"- {item}")
        print(f"Custo total: ${custo_total:.2f}")
    else:
        print("Você não fez nenhum pedido.")

if __name__ == "__main__":
    main()