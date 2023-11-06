expressao = input("Digite uma expressão aritmética (exemplo: x + y): ")

x, operacao, z = expressao.split()

x = int(x)
z = int(z)

if operacao == '+':
    resultado = x + z
elif operacao == '-':
    resultado = x - z
elif operacao == '*':
    resultado = x * z
elif operacao == '/':
    if z == 0:
        resultado = "Divisão por zero"
    else:
        resultado = x / z
else:
    resultado = "Operação inválida"

if isinstance(resultado, float):
    print(f"Resultado: {resultado:.1f}")
else:
    print(f"Resultado: {resultado}")