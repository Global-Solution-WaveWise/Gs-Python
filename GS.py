import random # Importa o módulo 'random' para gerar números aleatórios.

# Dicionário 'usuarios' armazena os tipos de usuário e suas respectivas senhas.
# As chaves são os tipos de usuário (ex: "funcionario"), e os valores são as senhas.
usuarios = {
    "funcionario": "12345",
    "cliente": "54321"
}

# Dicionário 'semana' armazena a previsão do tempo para cada dia da semana.
# Cada dia é uma chave, e seu valor é outro dicionário com 'chanceDeChuva' e 'chanceDeEnchente'.
# Inicialmente, essas chances são 'None', indicando que os dados ainda não foram preenchidos.
semana = {
    "domingo": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "segunda": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "terca": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "quarta": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "quinta": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "sexta": {"chanceDeChuva": None, "chanceDeEnchente": None},
    "sabado": {"chanceDeChuva": None, "chanceDeEnchente": None}
}

# --- Nova Função para Validação de Entrada (Numérica e de Opção) ---

def obter_resposta_valida(mensagem, opcoes_validas=None):
    """
    Obriga o usuário a digitar uma resposta que esteja entre as 'opcoes_validas' (se fornecidas)
    ou que seja um número inteiro entre 0 e 100 (se 'opcoes_validas' for None).
    Esta função entra em um loop contínuo até que uma entrada válida seja fornecida.

    Args:
        mensagem (str): A string a ser exibida ao usuário como prompt de entrada.
        opcoes_validas (list, optional): Uma lista de strings contendo as opções aceitáveis.
                                         Se None, a função espera um número inteiro entre 0 e 100.

    Returns:
        str or int: A resposta válida do usuário. Se for uma opção, em minúsculas.
                    Se for um número, como um inteiro.
    """
    while True:
        resposta_raw = input(mensagem) # Obtém a entrada bruta do usuário.

        if opcoes_validas is not None:
            # Lógica para validação de opções de texto
            resposta = resposta_raw.lower() # Converte para minúsculas para comparação.
            if resposta in opcoes_validas:
                return resposta
            else:
                print(f"Opção inválida. Por favor, digite uma das seguintes opções: {', '.join(opcoes_validas)}")
        else:
            # Lógica para validação de entrada numérica (chance de chuva/enchente)
            try:
                numero = int(resposta_raw) # Tenta converter a entrada para um inteiro.
                if 0 <= numero <= 100: # Verifica se o número está no intervalo de 0 a 100.
                    return numero
                else:
                    print("Por favor, digite um número entre 0 e 100.")
            except ValueError:
                # Captura o erro se a conversão para int falhar (ou seja, não é um número).
                print("Entrada inválida. Por favor, digite apenas números.")

# --- Funções do Sistema ---

def verUser(usuarios):
    """
    Função responsável pela autenticação do usuário (funcionário ou cliente) e verificação de senha.

    Args:
        usuarios (dict): O dicionário contendo os tipos de usuário e suas senhas.

    Returns:
        str or None: O tipo de usuário validado ("funcionario" ou "cliente") se o acesso for concedido,
                     caso contrário, retorna None.
    """
    print("Bem-vindo ao nosso sistema!")
    
    # Usa a função 'obter_resposta_valida' para garantir que o tipo de usuário seja válido.
    userValidacao = obter_resposta_valida(
        "Você é um funcionário ou cliente? \n-> funcionario ou cliente\n-> ",
        list(usuarios.keys()) # Passa as chaves do dicionário 'usuarios' como opções válidas.
    )

    tentativas = 3 # Define o número de tentativas permitidas para a senha.
    while tentativas > 0: # Loop de verificação de senha com limite de tentativas.
        senha = input(f"Digite a senha para {userValidacao}: ") # Solicita a senha.
        if senha == usuarios[userValidacao]: # Compara a senha digitada com a senha armazenada.
            print(f"Acesso concedido como {userValidacao}.") # Mensagem de sucesso.
            return userValidacao # Retorna o tipo de usuário validado.
        else:
            tentativas -= 1 # Decrementa o contador de tentativas.
            print(f"Senha incorreta. Tentativas restantes: {tentativas}") # Mensagem de erro.

    # Se as tentativas acabarem, o acesso é negado.
    print("Você não sabe a senha ou excedeu o número de tentativas.")
    return None # Retorna None indicando falha na autenticação.

def gerar_dados_aleatorios():
    """
    Preenche os dados meteorológicos da semana com valores aleatórios.
    A chance de enchente é influenciada pela chance de chuva.
    """
    for dia in semana: # Itera sobre cada dia no dicionário 'semana'.
        chance_chuva = random.randint(0, 100) # Gera uma chance de chuva aleatória.
        
        # Define a chance de enchente baseada na chance de chuva.
        if chance_chuva < 30:
            chance_enchente = random.randint(0, 20)
        elif chance_chuva < 70:
            chance_enchente = random.randint(20, 60)
        else:
            chance_enchente = random.randint(60, 100)

        # Armazena as chances formatadas como strings percentuais.
        semana[dia]["chanceDeChuva"] = f"{chance_chuva}%"
        semana[dia]["chanceDeEnchente"] = f"{chance_enchente}%"

def inserir_dados_manualmente():
    """
    Permite que um funcionário insira manualmente os dados de chance de chuva e enchente para cada dia,
    validando que as entradas sejam números entre 0 e 100.
    """
    print("\n--- Inserção de Dados Meteorológicos ---")
    for dia in semana: # Itera sobre cada dia da semana.
        print(f"\n{dia.capitalize()}:") # Exibe o nome do dia.
        
        # Usa 'obter_resposta_valida' sem 'opcoes_validas' para forçar entrada numérica.
        chuva = obter_resposta_valida("Chance de chuva (%): ")
        enchente = obter_resposta_valida("Chance de enchente (%): ")
        
        # Armazena os dados inseridos no dicionário 'semana'.
        semana[dia]["chanceDeChuva"] = f"{chuva}%"
        semana[dia]["chanceDeEnchente"] = f"{enchente}%"
    print("\nTodos os dados foram inseridos com sucesso!\n")

def mostrar_dados():
    """
    Exibe a previsão meteorológica completa para a semana.
    """
    print("\n--- Previsão da Semana ---")
    for dia, dados in semana.items(): # Itera sobre cada dia e seus dados.
        # Recupera as chances de chuva e enchente.
        chuva = dados["chanceDeChuva"] if dados["chanceDeChuva"] else "N/D"
        enchente = dados["chanceDeEnchente"] if dados["chanceDeEnchente"] else "N/D"
        # Imprime a previsão para o dia.
        print(f"{dia.capitalize()}: Chuva: {chuva} | Enchente: {enchente}")
    print()

# --- Execução Principal do Programa ---

# Tenta validar o usuário.
usuario_validado = verUser(usuarios)

# Verifica se a autenticação foi bem-sucedida.
if usuario_validado:
    # Se não houver dados preenchidos, gera dados aleatórios.
    if any(dados["chanceDeChuva"] is None for dados in semana.values()):
        gerar_dados_aleatorios()

    # Lógica específica para funcionários.
    if usuario_validado == "funcionario":
        print("\nVocê deseja inserir os dados manualmente ou usar os dados aleatórios gerados?")
        # Usa 'obter_resposta_valida' para a opção de inserção de dados.
        opcao = obter_resposta_valida(
            "Digite 'manual' para inserir manualmente ou 'auto' para manter aleatórios: ",
            ["manual", "auto"]
        )
        if opcao == "manual":
            inserir_dados_manualmente() # Chama a função para inserção manual.
        mostrar_dados() # Exibe os dados.
    
    # Lógica específica para clientes.
    elif usuario_validado == "cliente":
        mostrar_dados() # Clientes apenas visualizam.
else:
    # Mensagem exibida se a autenticação falhar.
    print("Acesso negado.")