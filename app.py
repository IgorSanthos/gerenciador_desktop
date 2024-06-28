import pandas as pd
import tkinter as tk
from tkinter import messagebox, Button, font
from funcao import move_files, save_messages_list_to_desktop
from PIL import Image, ImageTk

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
            messagebox.showinfo("Erros", "Caso haja Erros serao salvos no desktop")
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
def funcao4():
    try:
        from dados_cliente.datacluster4 import dados as dados_cluster3
        return processar_dados_cluster(dados_cluster3)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]
def funcao5():
    try:
        from dados_cliente.datacluster5 import dados as dados_cluster3
        return processar_dados_cluster(dados_cluster3)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]
def funcao6():
    try:
        from dados_cliente.datacluster6 import dados as dados_cluster3
        return processar_dados_cluster(dados_cluster3)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]
def funcao7():
    try:
        from dados_cliente.datacluster7 import dados as dados_cluster3
        return processar_dados_cluster(dados_cluster3)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]
def funcao8():
    try:
        from dados_cliente.datacluster8 import dados as dados_cluster3
        return processar_dados_cluster(dados_cluster3)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]
def funcao11():
    try:
        from dados_cliente.datacluster11 import dados as dados_cluster3
        return processar_dados_cluster(dados_cluster3)
    except ModuleNotFoundError:
        return ["Erro: Módulo não encontrado"]



# Variável global para armazenar a função selecionada
select_funcao = None

# Função para mostrar a opção selecionada e definir select_funcao
def mostrar_selecao(opcao):
    global select_funcao  # Declarar como global para modificá-la
    messagebox.showinfo("Opção Selecionada", f"Arquivos do dia {opcao[42:49]} enviados:")
    if opcao == "Cluster Prefeitura Geral | Agendado para o dia 01":
        select_funcao = funcao1
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 02":
        select_funcao = funcao2
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 03":
        select_funcao = funcao3
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 04":
        select_funcao = funcao4
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 05":
        select_funcao = funcao5
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 06":
        select_funcao = funcao6
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 07":
        select_funcao = funcao7
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 08":
        select_funcao = funcao8
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 11":
        select_funcao = funcao11
    else:
        select_funcao = None  # Defina um padrão caso necessário


# Configuração da janela principal
root = tk.Tk()
root.title("Projeto com Tkinter")
root.geometry('1000x600')
root.configure(background='white')


# Criando os botões e associando-os às funções
botao1 = Button(root, text="Mover arquivos", command=executar_e_mostrar,
                foreground="white", background="#ECA521", font=("Helvetica", 14))

botao1.pack(pady=8)
botao1.place(x=750, y=350) # Posiciona o botão

# Lista de opções
opcoes = [
    "Cluster Prefeitura Geral | Agendado para o dia 01",
    "Cluster Prefeitura Geral | Agendado para o dia 02",
    "Cluster Prefeitura Geral | Agendado para o dia 03",
    "Cluster Prefeitura Geral | Agendado para o dia 04",
    "Cluster Prefeitura Geral | Agendado para o dia 05",
    "Cluster Prefeitura Geral | Agendado para o dia 06",
    "Cluster Prefeitura Geral | Agendado para o dia 07",
    "Cluster Prefeitura Geral | Agendado para o dia 08",
    "Cluster Prefeitura Geral | Agendado para o dia 11"
]

# Variável para armazenar a opção selecionada
selecao = tk.StringVar(root)
selecao.set(opcoes[0])  # Define a opção padrão

# Criando o OptionMenu
menu_selecao = tk.OptionMenu(root, selecao, *opcoes)
menu_selecao.config(bg="#F2E8DE", fg='#EE3D25', font=('Helvetica', 10))
menu_selecao.place(x=665, y=400)


imagem = Image.open("img/aside.png")  
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(root, image=imagem_tk)
label_imagem.pack()
label_imagem.place(x=50, y=70)

textoh1 = "TransferEasy"
label_texto = tk.Label(root, text=textoh1, background="white", font=("Helvetica", 20, "bold"))
label_texto.place(x=730, y=200)

textoh2 = "Gerenciador de Arquivos"
label_texto = tk.Label(root, text=textoh2, background="white", font=("Helvetica", 16))
label_texto.place(x=700, y=240)

textoh2 = "Mova os arquivos do Jettax para o seu repositório"
label_texto = tk.Label(root, text=textoh2, background="white", font=("Helvetica", 10))
label_texto.place(x=680, y=270)

# Iniciando o loop principal da interface gráfica
root.mainloop()
