import tkinter as tk
from tkinter import messagebox

# Funções que serão executadas pelos botões
def funcao1():
    messagebox.showinfo("Função 1", "A função 1 foi executada")

def funcao2():
    messagebox.showinfo("Função 2", "A função 2 foi executada")

def funcao3():
    messagebox.showinfo("Função 3", "A função 3 foi executada")

# Configuração da janela principal
root = tk.Tk()
root.title("Projeto com Tkinter")
root.geometry('400x400')
root.configure(background='blue')


# Criando os botões e associando-os às funções
botao1 = tk.Button(root, text="Executar Função 1", command=funcao1)
botao1.pack(pady=10)

botao2 = tk.Button(root, text="Executar Função 2", command=funcao2)
botao2.pack(pady=10)

botao3 = tk.Button(root, text="Executar Função 3", command=funcao3)
botao3.pack(pady=10)

# Iniciando o loop principal da interface gráfica
root.mainloop()
