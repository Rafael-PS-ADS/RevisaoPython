notas = []

for x in range(5):
    codigo_aluno = input("Digite o código do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("quantidade de notas: ", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O aluno de código:", codigo_aluno, " obteve a nota:", nota)