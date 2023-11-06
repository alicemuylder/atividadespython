def converter_emoticons(texto):
    texto = texto.replace(":)", "🙂")
    texto = texto.replace(":(", "🙁")
    return texto
entrada = input("Digite uma string, sendo :) ou :( : ")
resultado = converter_emoticons(entrada)
print("Texto convertido:", resultado)