def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    try:
        valor1 = int(input("Digite o primeiro número: "))
        valor2 = int(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Por favor, insira números válidos.")

resposta = minha_funcao(valor1, valor2)

print(valor1, "+", valor2, "=", resposta)