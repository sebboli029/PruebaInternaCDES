import pandas as pd
from tabulate import tabulate

# Cargar el archivo CSV
file_path = 'players.csv'
df = pd.read_csv(file_path)

# Convertir la columna 'height' a centímetros
def height_to_cm(height):
    feet, inches = height.split('-')
    total_inches = int(feet) * 12 + int(inches)
    return total_inches * 2.54

df['height'] = df['height'].apply(height_to_cm)

# Calcular el IMC
df['IMC'] = df['weight'] / (df['height'] / 100) ** 2

desired_positions = ['QB', 'WR', 'G', 'T']
df = df[df['position'].isin(desired_positions)]

# Seleccionar las columnas deseadas y renombrarlas a español
selected_columns = df[['position', 'height', 'weight', 'IMC']]
selected_columns.columns = ['posición', 'altura (cm)', 'peso (kg)', 'IMC']

# Calcular el promedio de altura, peso e IMC por cada posición
total_columns = selected_columns.reset_index()
averge_columns = total_columns.groupby('posición').mean().reset_index()

# Guardar los datos promediados  y totales en un archivo de Excel
output_file_path = 'C:/Users/sebbo/Documents/pruebaInterna/total_posiciones.xlsx'
total_columns.to_excel(output_file_path, index=False)

output_file_path = 'C:/Users/sebbo/Documents/pruebaInterna/media_posiciones.xlsx'
averge_columns.to_excel(output_file_path, index=False)

# Mostrar los datos promediados y totalesusando tabulate con líneas continuas
print(tabulate(total_columns, headers='keys', tablefmt='fancy_grid'))
print(tabulate(averge_columns, headers='keys', tablefmt='fancy_grid'))
