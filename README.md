Resumo das Funcionalidades do Código

O código implementa um projeto modular para análise de dados financeiros. Abaixo, estão suas principais funcionalidades, incluindo a nova integração com a biblioteca Yahoo Finance:

Arquivo main.py

![print_main](https://github.com/Luix78th/funcional_analysis/assets/141957237/2a198715-8ce0-4824-a765-adbd9a7b7506)

Realiza as seguintes funções:

    Importações Necessárias:
        pandas para manipulação de dados.
        yfinance para obter dados financeiros.
        Funções personalizadas dos módulos process_data e read_extensions.

    Função get_yahoo_finance_data:
        Obtém dados financeiros históricos do Yahoo Finance.
        Parâmetros:
            symbol: o símbolo do ativo financeiro (e.g., "^BVSP" para o índice Bovespa).
            start_date e end_date: intervalo de datas para os dados.
        Retorna um DataFrame com os dados ajustados automaticamente ou None em caso de erro.

    Função Principal main:
        Define a fonte de dados como "yahoo" ou "local", caso o usuário escolha obter dados de um arquivo local
        Especifica o intervalo de datas conforme a necessidade.
        Processa e trata dados ausentes utilizando o método ffill (conforme a imagem abaixo)
        Aplica filtros para selecionar dados por datas e índices.
        Demonstra o uso do método .shift() para deslocamento de coluna.

Arquivo process_data.py

![ffill](https://github.com/Luix78th/funcional_analysis/assets/141957237/021d151f-d663-4389-8ff6-267678078562)

Este módulo contém funções utilitárias para processar e visualizar dados:

    Função process_data:
        Verifica e ajusta o formato dos dados.
        Converte a coluna "Date" para datetime e define como índice.
        Remove valores ausentes e ordena os dados.

    Função handle_missing:
        Trata dados ausentes com métodos como ffill, bfill, mean e median.

    Função visualize_data:
        Plota dados da coluna especificada (default: 'Close').

    Funções de Filtragem:
        filter_by_date: Filtra dados com base em datas específicas.
        filter_by_index: Filtra dados com base em índices de linhas.

    Função shift_column:
        Desloca valores de uma coluna por um número especificado de períodos.

Arquivo read_extensions.py

Este módulo contém funções para leitura de diferentes formatos de arquivo:

    Funções de Leitura:
        read_json, read_csv, read_excel, read_xml, read_html, read_txt.
        Cada função lê um tipo específico de arquivo e processa os dados usando process_data.
