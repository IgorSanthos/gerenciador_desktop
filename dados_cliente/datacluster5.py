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
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\atma_pictures_ltda_1193380',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\clinica_oftalmologica_arruda_ltda_-_me_794338',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\engpoint_servicos_de_engenharia_ltda_780819',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\evoluir_instituto_terapeutico_eireli_780734',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\jf_oliveira_eventos_ltda_973387',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\r1_audiovisual_locao_de_equipamentos_780793',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\r1_solutions_eventos_eireli_epp_780746',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\telma_lima_sociedade_individual_de_adv_780789',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 05\NOTAS\JETTAX\vcg_01_empreendimento_imobiliario_spe_794394'
    ],
    
    'Destino': [
        r'W:\Shared With Me\Clientes\Atma Pictures\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Clinica Arruda\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Engpoint Serviços\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Evoluir Instituto\2024\Fiscal',
        r'W:\Shared With Me\Clientes\JF Oliveira\2024\Fiscal',
        r'W:\Shared With Me\Clientes\R1 Audiovisual (letsee)\2024\Fiscal',
        r'W:\Shared With Me\Clientes\R1 Eventos\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Telma Lima Adv\2024\Fiscal',
        r'W:\Shared With Me\Clientes\VCG01\2024\Fiscal'
    ]
}

