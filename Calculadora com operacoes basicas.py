def calculadora():
    print("=== Calculadora ===")
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: divisão por zero."
    else:
        return "Operação inválida."
    
    return f"Resultado: {resultado}"

print(calculadora())