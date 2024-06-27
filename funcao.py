import pandas as pd
import shutil
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog

# Instância do QApplication
app = QApplication([])

# Caminho do arquivo Excel
caminho_excel = Path(r'W:\Shared With Me\Clientes\Fenix Assessoria\Planilhas\RELAÇÃO JETTAX2.xlsx')

# Exibir caixa de diálogo de entrada
text, ok = QInputDialog.getText(None, "CLUSTER", "Insira a data do Cluster:")

# Verificar se o usuário pressionou "OK"
if ok:
    # Definir o caminho para salvar o arquivo de log na área de trabalho
    caminho_area_trabalho = Path.home() / 'Desktop'
    caminho_arquivo_log = caminho_area_trabalho / 'log_erros.txt'

    erros_ocorridos = False

    # Abrir o arquivo de log para escrita
    with open(caminho_arquivo_log, 'w') as arquivo_log:
        try:
            # Ler a planilha Excel
            df = pd.read_excel(caminho_excel, sheet_name=f'Cluster_{text}')

            # Iterar sobre as linhas da planilha
            for index, row in df.iterrows():
                caminho_origem = Path(row['ORIGEM'])   # Coluna F: Caminho de origem
                caminho_destino = Path(row['DESTINO'])  # Coluna I: Caminho de destino
                caminho_nfts = Path(row['NFTS'])    # Coluna G: Caminho de origem
                caminho_guias = Path(row['GUIA'])  # Coluna H: Caminho de origem
                caminho_destino2 = Path(row['DESTINO2']) # Coluna J: Caminho de destino

                # Movimentar arquivos de guias
                try:
                    if caminho_guias.is_dir():
                        for arquivo in caminho_guias.glob('*'):
                            caminho_destino_arquivo = caminho_destino2 / arquivo.name
                            shutil.move(arquivo, caminho_destino_arquivo)
                            arquivo_log.write(f"Arquivo {arquivo.name} movido de {caminho_guias} para {caminho_destino_arquivo}\n")
                    else:
                        erros_ocorridos = True
                        arquivo_log.write(f"ERRO: Diretório de origem {caminho_guias} não encontrado. Movimento não realizado.\n")
                except Exception as error:
                    erros_ocorridos = True
                    arquivo_log.write(f"ERRO: Ocorreu um erro ao mover os arquivos de guias: {error}\n")

                # Movimentar arquivos de notas fiscais NFTS
                try:
                    if caminho_nfts.is_dir():
                        for arquivo in caminho_nfts.glob('*'):
                            if 'nfs' in arquivo.name:
                                caminho_destino_arquivo = caminho_destino / 'Serviços Tomados' / arquivo.name
                                shutil.move(arquivo, caminho_destino_arquivo)
                                arquivo_log.write(f"Arquivo {arquivo.name} movido de {caminho_nfts} para {caminho_destino_arquivo}\n")
                    else:
                        erros_ocorridos = True
                        arquivo_log.write(f"ERRO: Diretório de origem {caminho_nfts} não encontrado. Movimento não realizado.\n")
                except Exception as error:
                    erros_ocorridos = True
                    arquivo_log.write(f"ERRO: Ocorreu um erro ao mover os arquivos de notas fiscais: {error}\n")

                # Movimentar arquivos de Prestados Tomados
                try:
                    if caminho_origem.is_dir():
                        for arquivo in caminho_origem.glob('*'):
                            if 'enviadas' in arquivo.name:
                                caminho_destino_arquivo = caminho_destino / 'Serviços Prestados' / arquivo.name
                            elif 'recebidas' in arquivo.name:
                                caminho_destino_arquivo = caminho_destino / 'Serviços Tomados' / arquivo.name
                            else:
                                continue
                            shutil.move(arquivo, caminho_destino_arquivo)
                            arquivo_log.write(f"Arquivo {arquivo.name} movido de {caminho_origem} para {caminho_destino_arquivo}\n")
                    else:
                        erros_ocorridos = True
                        arquivo_log.write(f"ERRO: Diretório de origem {caminho_origem} não encontrado. Movimento não realizado.\n")
                except Exception as error:
                    erros_ocorridos = True
                    arquivo_log.write(f"ERRO: Ocorreu um erro ao mover os arquivos de origem: {error}\n")

            # Exibir mensagem informando que os arquivos foram movidos com sucesso
            if erros_ocorridos:
                QMessageBox.warning(None, "Erros Ocorridos", "Alguns erros ocorreram. Verifique o arquivo de log na área de trabalho.")
            else:
                QMessageBox.information(None, "Sucesso", "Fim da execução!")

        except Exception as error:
            QMessageBox.critical(None, "ERRO", f"Ocorreu um erro: {error}")
            arquivo_log.write(f"ERRO: Ocorreu um erro: {error}\n")
            erros_ocorridos = True

    if erros_ocorridos:
        QMessageBox.warning(None, "Erros Ocorridos", "Alguns erros ocorreram. Verifique o arquivo de log na área de trabalho.")

# Executar o loop de eventos do PyQt
app.exec_()
