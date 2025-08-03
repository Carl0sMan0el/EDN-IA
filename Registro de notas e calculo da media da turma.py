def media_da_turma():
    print("=== Registro de Notas ===")
    qtd_alunos = int(input("Quantos alunos na turma? "))
    soma_notas = 0

    for i in range(qtd_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        soma_notas += nota

    media = soma_notas / qtd_alunos
    return f"Média da turma: {media:.2f}"

print(media_da_turma())