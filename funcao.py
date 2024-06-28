import shutil
import os
from pathlib import Path
from datetime import datetime, timedelta

def move_files(df_filtrado):
    data_atual = datetime.now()

    # Calcular o último mês em relação à data atual
    primeiro_dia_mes_atual = data_atual.replace(day=1)
    ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    mes_anterior = ultimo_dia_mes_anterior.month
    ano_atual = ultimo_dia_mes_anterior.year

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
    try:
        for index, row in df.iterrows():
            #caminho Origem
            clienteJettax = Path(row['Origem'])
            #verificar se tem algum erro de Origem
            if not clienteJettax.exists():
                messages_list.append (f"Caminho de origem não encontrado: {clienteJettax}")
                save_messages_list_to_desktop(messages_list)

            #caminho DEstino
            clienteDest = Path(row['Destino']) / dtCliente
            arquivos = {
                'enviada': list(clienteJettax.glob('enviada*')),
                'recebida': list(clienteJettax.glob('recebido*')),
                'nfts': list((clienteJettax / 'nfts').glob('nft*')),
                'guia': list((clienteJettax / 'guia').glob('guia*'))
            }
            destinos = {
                'nfs': [clienteDest /'Arquivos XML/Serviços Prestados', clienteDest / 'Arquivos XML/Serviços Tomados'],
                'iss': clienteDest /'Tributos'
            }

            # Envio para Movimentação de Arquivos
            for arquivo in arquivos['enviada']:
                shutil.copy(arquivo, destinos['nfs'][0])
                
            for arquivo in arquivos['recebida']:
                shutil.copy(arquivo, destinos['nfs'][1])

            for arquivo in arquivos['guia']:
                shutil.copy(arquivo, destinos['iss'])

            for arquivo in arquivos['nfts']:
                shutil.copy(arquivo, destinos['nfs'][1])

        print(f"Arquivos copiados com sucesso{clienteDest}")
    
    except FileNotFoundError as e:
        messages_list.append(f"Erro: Arquivo não encontrado - {e}")
        save_messages_list_to_desktop(messages_list)
    
    except PermissionError as e:
        messages_list.append(f"Erro: Permissão negada - {e}")
        save_messages_list_to_desktop(messages_list)
    
    except Exception as e:
        messages_list.append(f"Erro inesperado: {e}")
        save_messages_list_to_desktop(messages_list)

    
    
    return messages_list


def save_messages_list_to_desktop(messages_list):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, 'messages_list.txt')

    with open(file_path, 'w') as file:
        for message in messages_list:
            file.write(f"{message}\n")

    print(f"Mensagens salvas com sucesso em {file_path}")

