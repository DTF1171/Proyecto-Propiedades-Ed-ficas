import pandas as pd
from sodapy import Socrata


def consultar_datos_suelos(departamento, municipio, cultivo, limite):
    # Cliente de la API
    client = Socrata("www.datos.gov.co","UaVtYT7HfXCF0ja7Vb7hLyuMo")

    # Filtro por departamento, municipio y cultivo
    query = f"departamento='{departamento}' AND municipio='{municipio}' AND cultivo='{cultivo}'"

    # Consulta a la API con un límite de registros
    resultados = client.get("ch4u-f3i5", where=query, limit=limite)

    # Convertir los resultados en un DataFrame de pandas
    if resultados:
        df_resultados = pd.DataFrame.from_records(resultados)
        return df_resultados
    else:
        return pd.DataFrame()


def calcular_mediana(df, columnas):
    # Asegurarse de que las columnas existan
    columnas_existentes = [col for col in columnas if col in df.columns]

    if len(columnas_existentes) > 0:
        # Convertir las columnas a valores numéricos, reemplazando valores no numéricos con NaN
        df[columnas_existentes] = df[columnas_existentes].apply(pd.to_numeric, errors='coerce')

        # Calcular la mediana, ignorando los NaN
        medianas = df[columnas_existentes].median()
        return medianas
    else:
        print(f"Las siguientes columnas no están disponibles en los datos: {columnas}")
        return None

