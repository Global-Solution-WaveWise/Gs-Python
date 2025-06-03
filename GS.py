import random

usuarios = {
    "funcionario": "12345",
    "cliente": "54321"
}

semana = {
    "domingo": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "segunda": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "terca": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "quarta": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "quinta": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "sexta": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "sabado": {"chanceDeChuva": None, "chanceDeEnchente": None}
}

def verUser(usuarios):
    print("Bem-vindo ao nosso sistema!")
    userValidacao = input("Você é um funcionário ou cliente? ")

    while userValidacao not in usuarios:
        userValidacao = input("Digite uma opção válida: \n-> funcionario ou cliente\n-> ")

    tentativas = 3
    while tentativas > 0:
        senha = input(f"Digite a senha para {userValidacao}: ")
        if senha == usuarios[userValidacao]:
            print(f"Acesso concedido como {userValidacao}.")
            return userValidacao
        else:
            tentativas -= 1
            print(f"Senha incorreta. Tentativas restantes: {tentativas}")

    print("Você não sabe a senha ou excedeu o número de tentativas.")
    return None

def gerar_dados_aleatorios():
    for dia in semana:
        chance_chuva = random.randint(0, 100)
        # chance de enchente depende da chuva
        if chance_chuva < 30:
            chance_enchente = random.randint(0, 20)
        elif chance_chuva < 70:
            chance_enchente = random.randint(20, 60)
        else:
            chance_enchente = random.randint(60, 100)

        semana[dia]["chanceDeChuva"] = f"{chance_chuva}%"
        semana[dia]["chanceDeEnchente"] = f"{chance_enchente}%"

def inserir_dados_manualmente():
    print("\n--- Inserção de Dados Meteorológicos ---")
    for dia in semana:
        print(f"\n{dia.capitalize()}:")
        chuva = input("Chance de chuva (%): ")
        enchente = input("Chance de enchente (%): ")
        semana[dia]["chanceDeChuva"] = f"{chuva}%"
        semana[dia]["chanceDeEnchente"] = f"{enchente}%"
    print("\nTodos os dados foram inseridos com sucesso!\n")

def mostrar_dados():
    print("\n--- Previsão da Semana ---")
    for dia, dados in semana.items():
        chuva = dados["chanceDeChuva"] if dados["chanceDeChuva"] else "N/D"
        enchente = dados["chanceDeEnchente"] if dados["chanceDeEnchente"] else "N/D"
        print(f"{dia.capitalize()}: Chuva: {chuva} | Enchente: {enchente}")
    print()

# Execução principal
usuario_validado = verUser(usuarios)

if usuario_validado:
    # Se não houver dados preenchidos, gera aleatórios
    if any(dados["chanceDeChuva"] is None for dados in semana.values()):
        gerar_dados_aleatorios()

    if usuario_validado == "funcionario":
        print("\nVocê deseja inserir os dados manualmente ou usar os dados aleatórios gerados?")
        opcao = input("Digite 'manual' para inserir manualmente ou 'auto' para manter aleatórios: ").lower()
        if opcao == "manual":
            inserir_dados_manualmente()
        mostrar_dados()
    elif usuario_validado == "cliente":
        mostrar_dados()
else:
    print("Acesso negado.")
