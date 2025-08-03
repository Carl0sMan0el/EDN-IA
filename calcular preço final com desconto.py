def calcular_desconto():
    valor = float(input("Digite o valor original do produto: R$ "))
    desconto = float(input("Digite a porcentagem de desconto: "))

    valor_desconto = valor * (desconto / 100)
    preco_final = valor - valor_desconto

    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")
calcular_desconto()
