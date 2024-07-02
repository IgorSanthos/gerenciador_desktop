# Dados fornecido
from datetime import datetime, timedelta

data_atual = datetime.now()
primeiro_dia_mes_atual = data_atual.replace(day=1)
ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
mes_anterior = ultimo_dia_mes_anterior.strftime('%m')
ano_atual = ultimo_dia_mes_anterior.strftime('%Y')
dtCliente_Atual = f"{mes_anterior} {ano_atual}"


dados = {
    'Origem': [
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 08\NOTAS\JETTAX\leve_agora_comercio_e_distribuicao_de_780838',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 08\NOTAS\JETTAX\sisnac_matriz_780752'

    ],

    'Destino': [
        r'W:\Shared With Me\Clientes\Leve Agora\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Sisnac\2024\Fiscal'
    ]
}

