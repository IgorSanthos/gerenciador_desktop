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
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 04\NOTAS\JETTAX\chiarato_eventos_e_consultoria_ltda_973399\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 04\NOTAS\JETTAX\chie_assessoria_empresarial_ltda_780744\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 04\NOTAS\JETTAX\cinomatic_do_brasil_industria_e_comerc_780731\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 04\NOTAS\JETTAX\obah_produtos_e_servicos_analiticos_lt_780748\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 04\NOTAS\JETTAX\opticam_tecnologia_918439\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 04\NOTAS\JETTAX\swiss_revestimentos_ltda_-_epp_780795\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 04\NOTAS\JETTAX\zc_rubber_brazil_import_e_export_ltda_780769\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 04\NOTAS\JETTAX\dixmedical_produtos_para_a_saude_ltda_837401\notas'

    ],
    'Destino': [
        r'W:\Shared With Me\Clientes\Chiarato Eventos\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Chie Assessoria\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Cinomatic\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Obah Produtos\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Opticam Tecnologia\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Swiss Revestimentos\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Zc Rubber\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Dixmedical Produtos\2024\Fiscal'
    ]
}

