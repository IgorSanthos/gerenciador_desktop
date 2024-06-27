import pandas as pd
import tkinter as tk
from tkinter import messagebox, Button
from funcao import move_files, save_messages_list_to_desktop

# Função que processa todos os dados de verificação 
def processar_dados_cluster(dados):
    messages_list = []
    try:
        # Criando o DataFrame
        df = pd.DataFrame(dados)
        df_filtrado = df
        move_files(df_filtrado)
    except FileNotFoundError as e:
        messages_list.append(f"Erro: Arquivo não encontrado - {e}")
        save_messages_list_to_desktop(messages_list)
        messagebox.showinfo("Erro", f"Arquivo não encontrado: {e}")
    except PermissionError as e:
        messages_list.append(f"Erro: Permissão negada - {e}")
        save_messages_list_to_desktop(messages_list)
        messagebox.showinfo("Erro", f"Permissão negada: {e}")
    except Exception as e:
        messages_list.append(f"Erro inesperado: {e}")
        save_messages_list_to_desktop(messages_list)
        messagebox.showinfo("Erro", f"Erro inesperado: {e}")
    
    return messages_list

# Função para executar a função selecionada e mostrar mensagens
def executar_e_mostrar():
    opcao = selecao.get()
    mostrar_selecao(opcao)  # Atualizar select_funcao baseado na opção selecionada
    if select_funcao is not None:
        messages_list = select_funcao()
        if messages_list:
            messagebox.showinfo("Mensagens", "\n".join(messages_list))
        messagebox.showinfo("Opção Selecionada", f"Arquivos enviados: {opcao}")
    else:
        messagebox.showinfo("Erro", "Nenhuma função selecionada para essa opção.")

# Funções que serão executadas pelos botões
def funcao1():
    try:
        from dados_cliente.datacluster1 import dados as dados_cluster1
        return processar_dados_cluster(dados_cluster1)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]

def funcao2():
    try:
        from dados_cliente.datacluster2 import dados as dados_cluster2
        return processar_dados_cluster(dados_cluster2)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]

def funcao3():
    try:
        from dados_cliente.datacluster3 import dados as dados_cluster3
        return processar_dados_cluster(dados_cluster3)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]

# Variável global para armazenar a função selecionada
select_funcao = None

# Função para mostrar a opção selecionada e definir select_funcao
def mostrar_selecao(opcao):
    global select_funcao  # Declarar como global para modificá-la
    messagebox.showinfo("Opção Selecionada", f"Arquivos enviados: {opcao}")
    if opcao == "Cluster Prefeitura Geral | Agendado para o dia 1":
        select_funcao = funcao1
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 2":
        select_funcao = funcao2
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 3":
        select_funcao = funcao3
    else:
        select_funcao = None  # Defina um padrão caso necessário
    
# Configuração da janela principal
root = tk.Tk()
root.title("Projeto com Tkinter")
root.geometry('1000x700')
root.configure(background='white')

# Criando os botões e associando-os às funções
botao1 = Button(root, text="Mover arquivos", command=executar_e_mostrar,
                foreground="white", background="#ECA521", font=("Helvetica", 14))

botao1.pack(pady=8)
botao1.place(x=750, y=350) # Posiciona o botão

# Lista de opções
opcoes = [
    "Cluster Prefeitura Geral | Agendado para o dia 1",
    "Cluster Prefeitura Geral | Agendado para o dia 2",
    "Cluster Prefeitura Geral | Agendado para o dia 3",
    "Cluster Prefeitura Geral | Agendado para o dia 4",
    "Cluster Prefeitura Geral | Agendado para o dia 5",
    "Cluster Prefeitura Geral | Agendado para o dia 6",
    "Cluster Prefeitura Geral | Agendado para o dia 7",
    "Cluster Prefeitura Geral | Agendado para o dia 8",
    "Cluster Prefeitura Geral | Agendado para o dia 9",
    "Cluster Prefeitura Geral | Agendado para o dia 10",
    "Cluster Prefeitura Geral | Agendado para o dia 11"
]

# Variável para armazenar a opção selecionada
selecao = tk.StringVar(root)
selecao.set(opcoes[0])  # Define a opção padrão

# Criando o OptionMenu
menu_selecao = tk.OptionMenu(root, selecao, *opcoes)
menu_selecao.config(bg="#F2E8DE", fg='#EE3D25', font=('Helvetica', 10))
menu_selecao.place(x=665, y=400)

# Iniciando o loop principal da interface gráfica
root.mainloop()
