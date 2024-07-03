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
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 06\NOTAS\JETTAX\dixmedical_produtos_para_a_saude_ltda_837401\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 06\NOTAS\JETTAX\r1_solutions_informatica_eireli_epp_780743\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 06\NOTAS\JETTAX\r2c_eventos_ltda_780834\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 06\NOTAS\JETTAX\sisnac_filial_sc_794403\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 06\NOTAS\JETTAX\tes_design_locacao_e_instalacao_de_equ_780776\notas'
    ],

    'Destino': [
        r'W:\Shared With Me\Clientes\Dixmedical Produtos\2024\Fiscal',
        r'W:\Shared With Me\Clientes\R1 Audiovisual (letsee)\2024\Fiscal',
        r'W:\Shared With Me\Clientes\R2C Eventos\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Sisnac filial\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Tes Design\2024\Fiscal'
    ]
}

