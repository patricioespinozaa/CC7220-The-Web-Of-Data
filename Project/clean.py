import pandas as pd
import os

path = os.path.dirname(__file__)

# Función para procesar y limpiar cada archivo
def process_file(file_path, platform_name):
    df = pd.read_csv(file_path)
    rows_wanted = ["title", "type", "genres", "releaseYear", "availableCountries"]
    df_selected = df[rows_wanted].dropna().copy()  # Crear una copia explícita
    df_selected['releaseYear'] = df_selected['releaseYear'].astype(int)
    df_selected['plataform'] = platform_name
    return df_selected

# Procesar cada archivo
hbo_clean = process_file(path+"/data/hbo.csv", "HBO")
netflix_clean = process_file(path+"/data/netflix.csv", "Netflix")
amazon_clean = process_file(path+"/data/amazon.csv", "Amazon")

# Combinar los datos en un único DataFrame
combined_df = pd.concat([hbo_clean, netflix_clean, amazon_clean], ignore_index=True)

# Guardar el resultado en un archivo CSV
combined_df.to_csv(path+"/clean_data.csv", index=False)

