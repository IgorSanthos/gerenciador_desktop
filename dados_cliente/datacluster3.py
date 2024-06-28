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
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\dener_brito_nutricionista_ltda_794343\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\fernandes_lucena__lopes_consultoria_i_794349\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\fernandes_lucena_empreendimentos_imobi_780747\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\fn_patrimonial_e_condominios_ltda_780794\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\llrm_restaurante_e_comercio_de_bebidas_ltda_780809\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\manxiang_gui_comercio_de_iluminacao_780775\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\nlb_comercio_de_maquin.e_peas_eireli_780779\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\nlb_industria_de_maquinas_e_equipament_780758\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\sisaltech_eventos_e_administrao_ltda_1153240\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\sjr_imoves_ltda_780812\notas',
        rf'W:\Shared With Me\Clientes\Jettax\{dtCliente_Atual}\NFS 03\NOTAS\JETTAX\teknovation_equipamentos_e_servios_ltda_972056\notas'
    ],

    'Destino': [
        r'W:\Shared With Me\Clientes\Dener Nutricionista\2024\Fiscal',
        r'W:\Shared With Me\Clientes\FL Lopes (barueri)\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Fernandes Lucena Matriz\2024\Fiscal',
        r'W:\Shared With Me\Clientes\FN Patrimonial (fl gestao)\2024\Fiscal',
        r'W:\Shared With Me\Clientes\LLRM (Jovina)\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Manxiang Gui - Terminal Luz\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Nlb Comércio\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Nlb Indústria\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Sisaltech\2024\Fiscal',
        r'W:\Shared With Me\Clientes\SJR Imoveis - Monica Imoveis\2024\Fiscal',
        r'W:\Shared With Me\Clientes\Teknovation\2024\Fiscal'

    ]
}

