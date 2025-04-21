import pandas as pd

# Cargar el archivo CSV
csv_file_path = 'C:/Users/sebbo/Documents/prueba interna/result.csv'
df = pd.read_csv(csv_file_path)

# Guardar los datos en un archivo Excel
excel_file_path = 'C:/Users/sebbo/Documents/prueba interna/result.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Archivo Excel guardado en: {excel_file_path}")