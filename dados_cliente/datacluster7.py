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
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\hmf_sistemas_de_energia_comercio_e_imp_780804\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\r2_empreendimentos_1193371\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\roth_sociedade_individual_de_advocacia_794377\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\verardi__mesquita_794395\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\yabiku_filial_l3_780759\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\yabiku_filial_l6_780787\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\yabiku_filial_l2_780833\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\yabiku_filial_l8_780832\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 07\NOTAS\JETTAX\yabiku_matriz_780727\notas'
    ],
    
    'Destino': [
        r'W:\Shared With Me\Clientes\Hmf Sistemas de Energia\2024\Fiscal',
        r'W:\Shared With Me\Clientes\R2 Empreendimentos\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Roth\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Verardi & Mesquita\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Yabiku Materiais (filial 01) L3\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Yabiku Materiais (filial 02) L6\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Yabiku Materiais (filial 04) L2\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Yabiku Materiais (filial 05) L8\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Yabiku Materiais (matriz) L1\2024\Fiscal'
    ]
}

