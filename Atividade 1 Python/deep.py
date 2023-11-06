def verificar_resposta(resposta):
    resposta_lower = resposta.lower()
    return resposta_lower == "42" or resposta_lower == "forty-two" or resposta_lower == "forty two"

resposta = input("Qual é a resposta para a Grande Questão da Vida, do Universo e Tudo o Mais? ")

if verificar_resposta(resposta):
    print("Yes")
else:
    print("No")
