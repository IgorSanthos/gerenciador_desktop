import tkinter as tk
from tkinter import messagebox, Button

# Funções que serão executadas pelos botões
def funcao1():
    messagebox.showinfo("Função 1", "A função 1 foi executada")

def funcao2():
    messagebox.showinfo("Função 2", "A função 2 foi executada")

def funcao3():
    messagebox.showinfo("Função 3", "A função 3 foi executada")

def funcao4():
    messagebox.showinfo("Função 4", "A função 4 foi executada")

def funcao5():
    messagebox.showinfo("Função 5", "A função 5 foi executada")

def funcao6():
    messagebox.showinfo("Função 6", "A função 6 foi executada")

def funcao7():
    messagebox.showinfo("Função 7", "A função 7 foi executada")

def funcao8():
    messagebox.showinfo("Função 8", "A função 8 foi executada")

def funcao9():
    messagebox.showinfo("Função 9", "A função 9 foi executada")

def funcao10():
    messagebox.showinfo("Função 10", "A função 10 foi executada")

def funcao11():
    messagebox.showinfo("Função 11", "A função 11 foi executada")

# Função para mostrar a opção selecionada
def mostrar_selecao(opcao):
    messagebox.showinfo("Opção Selecionada", f"Você selecionou: {opcao}")
    if opcao == "Cluster Prefeitura Geral | Agendado para o dia 1":
        funcao1()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 2":
        funcao2()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 3":
        funcao3()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 4":
        funcao4()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 5":
        funcao5()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 6":
        funcao6()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 7":
        funcao7()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 8":
        funcao8()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 9":
        funcao9()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 10":
        funcao10()
    elif opcao == "Cluster Prefeitura Geral | Agendado para o dia 11":
        funcao11()

# Configuração da janela principal
root = tk.Tk()
root.title("Projeto com Tkinter")
root.geometry('1000x700')
root.configure(background='white')

# Criando os botões e associando-os às funções
botao1 = Button(root, text="Mover arquivos", command=funcao1, foreground="white",  background="#ECA521", font=("Helvetica", 14))
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
menu_selecao = tk.OptionMenu(root, selecao, *opcoes, command=mostrar_selecao,)
menu_selecao.config(bg="#F2E8DE",fg='#EE3D25', font=('Helvetica', 10))
menu_selecao.place(x=665, y=400)











# Iniciando o loop principal da interface gráfica
root.mainloop()
