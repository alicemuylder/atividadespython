meses = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():
    while True:
        data = input("Digite uma data (mês-dia-ano ou nome do mês dia, ano): ")

        try:
            partes = data.split()
            if len(partes) == 3:
                mes, dia, ano = partes
                mes = mes if len(mes) == 2 else meses[mes]
            else:
                dia, mes, ano = partes
                mes = mes if len(mes) == 2 else meses[mes]

            data_iso8601 = f"{ano}-{mes}-{dia}"
            print(data_iso8601)
            break
        except (ValueError, KeyError):
            print("Data em formato inválido. Tente novamente.")

if __name__ == "__main__":
    main()