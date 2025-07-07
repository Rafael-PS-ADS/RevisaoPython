#Se tem mais de 18 anos, pode entrar
#Se tem menos de 18 anos, não pode entrar

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você pode entrar.")
else:
    print("Você não pode entrar.")