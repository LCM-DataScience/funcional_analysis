import pandas as pd
import matplotlib.pyplot as plt


def process_data(df):
    # Verifica se as colunas estão separadas por ponto e vírgula
    if ';' in df.columns[0]:
        df[['Date', 'Adj Close']] = df.iloc[:, 0].str.split(';', expand=True)
        df.drop(columns=[df.columns[0]], inplace=True)

    # Verifica se a coluna "Date" está presente no DataFrame
    if 'Date' not in df.columns:
        raise ValueError("Nenhuma coluna 'Date' encontrada no arquivo.")

    # Converte a coluna "Date" para datetime e usa como índice
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%Y-%m-%d')
    df.set_index('Date', inplace=True)

    # Remove NAs e NaNs
    df.dropna(inplace=True)

    # Ordena o DataFrame pelo índice (Data)
    df.sort_index(inplace=True)

    return df


#Neste caso, usamos o método 'ffill()', normalmente o mais usado em análise de dados financeiros
def handle_missing(df, method='ffill'):
    if method == 'ffill':
        return df.ffill()
    elif method == 'bfill':
        return df.bfill()
    elif method == 'mean':
        return df.fillna(df.mean())
    elif method == 'median':
        return df.fillna(df.median())
    else:
        return df


def visualize_data(df, column='Close'):
    df[column].plot(figsize=(12, 7))
    plt.show()


def filter_by_date(df, start_date=None, end_date=None, columns=None):
    """
    Filter DataFrame rows based on specified start and end dates.

    Parameters:
    - df (pd.DataFrame): DataFrame to filter.
    - start_date (str or datetime.date, optional): Start date for filtering.
    - end_date (str or datetime.date, optional): End date for filtering.
    - columns (list of str, optional): Columns to include in the filtered DataFrame.

    Returns:
    - pd.DataFrame: Filtered DataFrame.
    """
    if start_date is not None and end_date is not None:
        if isinstance(start_date, str):
            start_date = pd.to_datetime(start_date)
        if isinstance(end_date, str):
            end_date = pd.to_datetime(end_date)

        filtered_df = df.loc[start_date:end_date, columns]
    else:
        filtered_df = df

    return filtered_df


def filter_by_index(df, start_index=None, end_index=None, columns=None):
    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(df)
    if columns is None:
        filtered_df = df.iloc[start_index:end_index]
    else:
        filtered_df = df.iloc[start_index:end_index][columns]
    return filtered_df


# Método .shift
def shift_column(df, column, shift_periods):
    new_column_name = f"{column}_shifted_{shift_periods}"
    df[new_column_name] = df[column].shift(shift_periods)
    return df
