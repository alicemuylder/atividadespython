def main():
    while True:
        try:
            entrada = input("Digite uma fração (X/Y): ")
            X, Y = map(int, entrada.split('/'))

            if X > Y or Y == 0:
                print("Entrada inválida. X deve ser menor ou igual a Y, e Y não pode ser zero.")
            else:
                porcentagem = (X / Y) * 100
                porcentagem_arredondada = round(porcentagem)

                if porcentagem_arredondada <= 1:
                    print("E (tanque vazio)")
                elif porcentagem_arredondada >= 99:
                    print("F (tanque cheio)")
                else:
                    print(f"{porcentagem_arredondada}%")
                break
        except (ValueError, ZeroDivisionError):
            print("Entrada inválida. Certifique-se de digitar uma fração no formato X/Y e evitar divisão por zero.")

if __name__ == "__main__":
    main()