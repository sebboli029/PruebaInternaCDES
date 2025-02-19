import pandas as pd
from tabulate import tabulate

# Cargar el archivo CSV
file_path = 'C:/Users/sebbo/Downloads/players.csv'
df = pd.read_csv(file_path)

# Convertir la columna 'height' a centímetros
def height_to_cm(height):
    feet, inches = height.split('-')
    total_inches = int(feet) * 12 + int(inches)
    return total_inches * 2.54

df['height'] = df['height'].apply(height_to_cm)

# Calcular el IMC
df['IMC'] = df['weight'] / (df['height'] / 100) ** 2

# Seleccionar las columnas deseadas y renombrarlas a español
selected_columns = df[['position', 'height', 'weight', 'IMC']]
selected_columns.columns = ['posición', 'altura (cm)', 'peso (kg)', 'IMC']

# Calcular el promedio de altura, peso e IMC por cada posición
average_columns = selected_columns.groupby('posición').mean().reset_index()

# Guardar los datos promediados en un archivo JSON
output_file_path = 'C:/Users/sebbo/Documents/prueba interna/promedios_posiciones.json'
average_columns.to_json(output_file_path, orient='records', lines=True)

# Mostrar los datos promediados usando tabulate con líneas continuas
print(tabulate(average_columns, headers='keys', tablefmt='fancy_grid'))