def main():
    preco_coca_cola = 50 
    valor_inserido = 0 
    while valor_inserido < preco_coca_cola:
        moeda = int(input("Insira uma moeda (5, 10, ou 25 centavos): "))

        if moeda == 5 or moeda == 10 or moeda == 25:
            valor_inserido += moeda
            saldo_devido = preco_coca_cola - valor_inserido

            if saldo_devido > 0:
                print(f"Valor ainda devido: {saldo_devido} centavos")
            else:
                troco = valor_inserido - preco_coca_cola
                print(f"Você inseriu o valor correto. Troco: {troco} centavos.")
        else:
            print("Moeda não aceita. Por favor, insira apenas moedas de 5, 10, ou 25 centavos.")

if __name__ == "__main__":
    main()