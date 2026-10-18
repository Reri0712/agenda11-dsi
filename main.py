from colorama import init, Fore, Style

# Inicializa o colorama para garantir o funcionamento correto das cores no terminal
init(autoreset=True)

def definir_cor_nivel(nivel):
    """
    Função responsável por associar cada nível do reservatório à sua respectiva 
    mensagem de alerta, situação e cor utilizando a biblioteca colorama.
    """
    if nivel == 1:
        return f"{Fore.RED}[NÍVEL 1] Muito baixo (crítico) - Alerta de seca no reservatório!"
    elif nivel == 2:
        return f"{Fore.YELLOW}[NÍVEL 2] Baixo - Atenção para o consumo moderado."
    elif nivel == 3:
        return f"{Fore.GREEN}[NÍVEL 3] Médio - Reservatório dentro da faixa ideal."
    elif nivel == 4:
        return f"{Fore.CYAN}[NÍVEL 4] Alto - Nível elevado, monitorando volume."
    elif nivel == 5:
        return f"{Fore.BLUE}[NÍVEL 5] Muito alto (alerta) - Risco de transbordo!"
    else:
        return f"{Style.RESET_ALL}Nível desconhecido."

def simular_monitoramento():
    """
    Função principal que armazena os níveis em uma lista e realiza a 
    simulação exibindo as mensagens formatadas no terminal.
    """
    # Lista contendo os 5 níveis do reservatório
    niveis_reservatorio = [1, 2, 3, 4, 5]
    
    print("=== SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ===")
    print("Iniciando varredura dos níveis de água...\n")
    
    for n in niveis_reservatorio:
        mensagem = definir_cor_nivel(n)
        print(mensagem)
    
    print("\nVarredura concluída. Sistema operando normalmente.")

if __name__ == "__main__":
    simular_monitoramento()