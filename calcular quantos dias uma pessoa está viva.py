from datetime import datetime

def dias_vivo():
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    
    dias_vivo = (hoje - nascimento).days
    print(f"Você está vivo há {dias_vivo} dias.")
dias_vivo()
