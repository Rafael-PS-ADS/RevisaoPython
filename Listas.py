numeros = [5, 8, 13, 30, 2, 1, 4, 9, 6]

print("Total: ", len(numeros))
print("Menor número: ", min(numeros))
print("Maior número: ", max(numeros))
print("Soma dos números: ", sum(numeros))
print("Números pares: ", [nume for nume in numeros if nume % 2 == 0])
print("Números ímpares: ", [nume for nume in numeros if nume % 2 != 0])
print("Números ordenados: ", sorted(numeros))