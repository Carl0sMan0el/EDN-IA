nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("\n=== Calculadora de Média Escolar ===")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média final: {media:.2f}")
print("Resultado:", "Aprovado" if media >= 7 else "Reprovado")