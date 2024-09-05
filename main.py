import os
import funcoes



while True:
        print("---------- Gerenciador de Tarefas -----------------")
        print("\nMenu:")
        print("1. Mostrar tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")
        print("======================================================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            funcoes.mostrar_tarefas()
        elif escolha == '2':
            funcoes.adicionar_tarefa()
        elif escolha == '3':
            funcoes.remover_tarefa()
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")



input("Pressione Enter para limpar o terminal...")
funcoes.limpar_terminal()
