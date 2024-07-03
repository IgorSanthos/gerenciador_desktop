import shutil
import tkinter as tk
import os
from pathlib import Path
from datetime import datetime, timedelta
from tkinter import Tk, Label, Frame, TOP, messagebox
from tkinter.ttk import Progressbar
from tqdm import tqdm  # Importa tqdm para a barra de progresso
import pandas as pd
from pandasgui import show

def move_files(df_filtrado):
    data_atual = datetime.now()

    # Calcular o último mês em relação à data atual
    primeiro_dia_mes_atual = data_atual.replace(day=1)
    ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    mes_anterior = ultimo_dia_mes_anterior.month

    # Obter o nome do mês em português
    meses_em_portugues = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    nome_mes = meses_em_portugues[mes_anterior - 1]  # Ajustando o índice para começar em 0

    # Formatando para o estilo desejado (exemplo: '5_Maio')
    dtCliente = f"{mes_anterior}_{nome_mes}"

    messages_list = []  # Inicializa a lista vazia para armazenar as mensagens
    df = df_filtrado

    # Configuração da janela Tkinter
    root = Tk()
    root.title("Progresso de Movimentação de Arquivos")
    root.geometry("400x150")

    # Garante que a janela fique sempre no topo
    root.lift()
    root.attributes('-topmost', True)

    # Frame para conter os elementos
    frame = Frame(root)
    frame.pack(pady=20)

    # Label informativa
    lbl_info = Label(frame, text="Movendo arquivos...", font=("Arial", 12))
    lbl_info.pack(side=TOP)

    # Barra de progresso
    progress = Progressbar(frame, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=10)

    # Função para atualizar a barra de progresso
    def update_progress(count, total):
        progress['value'] = (count / total) * 100
        root.update_idletasks()

    # Função para fechar a janela Tkinter
    def close_window():
        root.destroy()

    # Inicia a barra de progresso com o total de iterações
    total_files = len(df)
    with tqdm(total=total_files) as pbar:
        for index, row in df.iterrows():
            # Caminho Origem
            clienteJettax = Path(row['Origem'])

            # Verificar se o caminho de origem existe
            if not clienteJettax.exists():
                # Separando as barras para que seja retirado do endereço o nome do cliente
                clienteJettax=str(clienteJettax)
                terceira_barra_cliente = clienteJettax.find('\\', clienteJettax.find('\\', clienteJettax.find('\\') + 1) + 1)
                quarta_barra_cliente = clienteJettax.find('\\', terceira_barra_cliente + 1)
                clienteJettax_name = clienteJettax[terceira_barra_cliente + 1:quarta_barra_cliente]               
                messages_list.append(f"Caminho de origem não encontrado: {clienteJettax_name}")
                # barra de progresso
                pbar.update(1)  # Atualiza a barra de progresso
                update_progress(pbar.n, total_files)
                continue  # Continua para o próximo arquivo

            # Caminho Destino
            clienteDest = Path(row['Destino']) / dtCliente
            arquivos = {
                'enviada': list((clienteJettax/'notas').glob('enviadas*')),
                'recebida': list((clienteJettax/'notas').glob('recebidas*')),
                'nfts': list((clienteJettax/'nfts').glob('nfs*')),
                'guias': list((clienteJettax/'guias').glob('guias*')),
                'resumo_guias': list((clienteJettax/'guias').glob('resumo_guias_guias*'))
            }
            destinos = {
                'nfs': [clienteDest / 'Arquivos XML/Serviços Prestados', clienteDest / 'Arquivos XML/Serviços Tomados'],
                'iss': clienteDest / 'Tributos'
            }
            # Envio para Movimentação de Arquivos
            try:
                for arquivo in arquivos['enviada']:
                    shutil.copy(arquivo, destinos['nfs'][0])
                
                for arquivo in arquivos['recebida']:
                    shutil.copy(arquivo, destinos['nfs'][1])

                for arquivo in arquivos['guias']:
                    shutil.copy(arquivo, destinos['iss'])
                
                for arquivo in arquivos['resumo_guias']:
                    shutil.copy(arquivo, destinos['iss'])

                for arquivo in arquivos['nfts']:
                    shutil.copy(arquivo, destinos['nfs'][1])
                    
                # Separando as barras para que seja retirado do endereço o nome do cliente
                clienteDest=str(clienteDest)
                terceira_barra = clienteDest.find('\\', clienteDest.find('\\', clienteDest.find('\\') + 1) + 1)
                quarta_barra = clienteDest.find('\\', terceira_barra + 1)
                client_name = clienteDest[terceira_barra + 1:quarta_barra]
                messages_list.append(f"Arquivos do ( {client_name} ) copiados com sucesso !")
            # tratamento de Erros
            except (FileNotFoundError, PermissionError) as e:
                messages_list.append(f"Erro ao copiar arquivo: {e}")
                # barra de progresso
                pbar.update(1)  # Atualiza a barra de progresso
                update_progress(pbar.n, total_files)
                continue  # Continua para o próximo arquivo
            except Exception as e:
                messages_list.append(f"Erro inesperado ao copiar arquivo: {e}")
                # barra de progresso
                pbar.update(1)  # Atualiza a barra de progresso
                update_progress(pbar.n, total_files)
                continue  # Continua para o próximo arquivo

            pbar.update(1)  # Atualiza a barra de progresso após o processamento de cada arquivo
            update_progress(pbar.n, total_files)

    # Salva todas as mensagens ao final do processamento
    save_messages_list_to_desktop(messages_list)
    messagebox.showinfo("Aviso","Arquivos do dia enviados com sucesso")
    # Fecha a janela Tkinter após o término do processamento
    root.after(1000, close_window)  # Espera 1 segundo antes de fechar a janela

    root.mainloop()

    return messages_list


def save_messages_list_to_desktop(messages_list):
    # Cria uma janela tkinter
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    root.title("Erros")
    root.geometry('1200x600')

    # Monta as mensagens em uma string para exibir na messagebox
    message_text = "\n".join(messages_list)

    # Exibe a messagebox com as mensagens
    messagebox.showinfo("Mensagens", message_text)

    # Fecha a janela tkinter
    root.destroy()


if __name__ == "__main__":
    pass
