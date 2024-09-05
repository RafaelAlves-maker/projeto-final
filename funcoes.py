import os

tarefas = []

def mostrar_tarefas(): 
    """Exibe a lista de tarefas."""
    if len(tarefas) == 0: 
        print("Nenhuma tarefa na lista.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, 1): 
            print(f"{i}. {tarefa}")

def adicionar_tarefa(): 
    """Adiciona uma nova tarefa à lista."""
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa():
    """Remove uma tarefa da lista."""
    mostrar_tarefas()
    if len(tarefas) > 0:
        try:
            indice = int(input("Digite o número da tarefa que deseja remover: "))
            if 1 <= indice <= len(tarefas):
                tarefa_removida = tarefas.pop(indice - 1)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Por favor, insira um número válido.")
    else:
        print("A lista está vazia. Nada para remover.")


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
