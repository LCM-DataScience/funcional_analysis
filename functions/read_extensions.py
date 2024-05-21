import pandas as pd
from . import process_data


def read_json(file):
    # Lê o arquivo específico
    df = pd.read_json(file)
    # Chama a função process_data do módulo process_data
    return process_data.process_data(df)


def read_csv(file):
    # Lê o arquivo específico
    df = pd.read_csv(file)
    # Chama a função process_data do módulo process_data
    return process_data.process_data(df)


def read_excel(file):
    # Lê o arquivo Excel
    df = pd.read_excel(file)
    return process_data.process_data(df)


def read_xml(file_path):
    # Adicione aqui o código para ler arquivos XML
    # Exemplo:
    with open(file_path, 'r') as file:
        data = file.read()
        # Processar o conteúdo do arquivo XML conforme necessário
        # Aqui você pode usar bibliotecas como lxml ou xml.etree.ElementTree para analisar o XML
    return data


def read_html(file_path):
    # Adicione aqui o código para ler arquivos HTML
    # Exemplo:
    with open(file_path, 'r') as file:
        data = file.read()
        # Processar o conteúdo do arquivo HTML conforme necessário
    return data


def read_txt(file):
    # Lê o arquivo de texto
    df = pd.read_csv(file, delimiter='\t')
    return process_data.process_data(df)
