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
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\castilho_servios_administrativos_e_financeiros_ltda_1060939\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\dinamica_service_manuteno_de_maquinas_e_equipamentos_ltda_940353\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\imperial_empreendimentos_imobiliarios_794355\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\leila_aparecida_de_oliveira_silva_794360\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\ptm_planejamento_financeiro_ltda_794374\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\sfx_administradora_de_bens_proprios_ltda_1061007\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\sfx_administradora_de_bens_proprios_ltda_1061007\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\sonho_da_sorte_promocoes_e_vendas_ltda_794387\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\vision_constantly_growing_ltda_794397\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 02\NOTAS\JETTAX\vision_constantly_growing_ltda_794397\notas'
    ],
    'Destino': [
        r'W:\Shared With Me\Clientes\Castilho Serviços\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Dinamica Service\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Imperial Empreendimentoss Imob\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Leila Aparecida (Historias Visuais - HV)\2024\Fiscal',
        r'W:\Shared With Me\Clientes\PTM Assessoria\2024\Fiscal',
        r'W:\Shared With Me\Clientes\SFX Administradora\2024\Fiscal',
        r'W:\Shared With Me\Clientes\SFX Administradora\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Sonho da Sorte\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Vision Constantly\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Vision Constantly\2024\Fiscal'

    ]
}

