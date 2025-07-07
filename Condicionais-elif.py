# Verifica o salário e informa a faixa de imposto

salario = float(input("Digite o seu salário: "))

if salario <= 1000:
    print("Você está na faixa de isenção.")
elif salario > 1000 and salario <= 2000:
    print("Você paga 10% de imposto.")
elif salario > 2000 and salario <= 3000:
    print("Você paga 20% de imposto.")
else:
    print("Você paga 30% de imposto.")