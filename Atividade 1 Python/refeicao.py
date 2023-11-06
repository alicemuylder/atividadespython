def convert(time):
    horas, minutos = map(int, time.split(":"))
    return horas + minutos / 60

def main():
    horario = input("Digite um horário (HH:MM): ")
    hora = convert(horario)
    if 7.0 <= hora <= 8.0:
        print("Hora do café da manhã")
    elif 12.0 <= hora <= 13.0:
        print("Hora do almoço")
    elif 18.0 <= hora <= 19.0:
        print("Hora do jantar")

if __name__ == "__main__":
    main()