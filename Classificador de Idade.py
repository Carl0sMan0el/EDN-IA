def classificar_idade():
    try:
        idade = int(input("Digite sua idade: "))
        
        if idade < 0:
            classificacao = "Idade inválida"
        elif idade <= 12:
            classificacao = "Criança"
        elif idade <= 17:
            classificacao = "Adolescente"
        elif idade <= 59:
            classificacao = "Adulto"
        else:
            classificacao = "Idoso"

        print("Classificação:", classificacao)
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

classificar_idade()
