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
        rf'W:\Shared With Me\Clientes\Jettax\05 2024\NFS 11\NOTAS\JETTAX\8fs_corretora_de_beneficios_e_seguros_780815',
        rf'W:\Shared With Me\Clientes\Jettax\05 2024\NFS 11\NOTAS\JETTAX\gabriela_castro_fisioterapeuta_ltda_780828'
    ],

    'Destino': [
        r'W:\Shared With Me\Clientes\8FS\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Gabriela Castro\2024\Fiscal'
    ]
}
