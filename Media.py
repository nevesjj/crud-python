alunos = {}

for i in range(20):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = []
    
    for j in range(3):
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas.append(nota)
    
    alunos[nome] = notas

maior_media = 0
aluno_maior_media = ""

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    if media > maior_media:
        maior_media = media
        aluno_maior_media = aluno

print(f"\nO aluno com a maior média é {aluno_maior_media} com média {maior_media:.2f}")