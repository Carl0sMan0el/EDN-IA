def classificar_numeros():
    print("=== Classificador de Números ===")
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            print("Entrada inválida, digite apenas números inteiros ou 'sair'.")

    return f"Total de pares: {pares}\nTotal de ímpares: {impares}"

print(classificar_numeros())
