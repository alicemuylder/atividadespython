def main():
 dollars = dollars_to_float(input("Quanto custou a refeição? "))
 percent = percent_to_float(input("Qual porcentagem você deseja dar de gorjeta? "))
 tip = dollars * percent
 print(f"Você deve pagar {dollars:.2f} x {percent:.2f} de gorgeta")
 print(f"Deixe uma gorjeta de ${tip:.2f}")
def dollars_to_float(dinheiro):
    string_sem_cifrao = dinheiro.replace("$", "")
    dinheiro_float = float(string_sem_cifrao)
    return float (dinheiro_float)

def percent_to_float(dinheiro):
    string_sem_porcentagem = dinheiro.replace("%","")
    dinheiro_float = float(string_sem_porcentagem)
    dinheiro_float = float(dinheiro_float) / 100
    return dinheiro_float

main()