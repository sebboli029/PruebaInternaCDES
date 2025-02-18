# NFL Player Data Analysis: Average Height, Weight, and BMI by Position

This repository contains a Python script (`main.py`) that analyzes NFL player data from a CSV file to calculate and display the average height, weight, and Body Mass Index (BMI) for each player position.

## Table of Contents

*   [Description](#description)
*   [Dependencies](#dependencies)
*   [Data Source](#data-source)
*   [Usage](#usage)
*   [Output](#output)
*   [Code Explanation](#code-explanation)
*   [License](#license)
*   [Author](#author)

## Description

The `main.py` script performs the following actions:

1.  **Loads Player Data:** Reads player information from a CSV file named `players.csv`.
2.  **Converts Height:** Converts player height from feet-inches format to centimeters.
3.  **Calculates BMI:** Calculates the Body Mass Index (BMI) for each player using their weight and height.
4.  **Selects and Renames Columns:** Selects the relevant columns (position, height, weight, BMI) and renames them to Spanish.
5.  **Calculates Averages by Position:** Groups the data by player position and calculates the average height, weight, and BMI for each position.
6.  **Prints Results:** Displays the calculated averages in a nicely formatted table using the `tabulate` library.

## Dependencies

Before running the script, make sure you have the following Python libraries installed:

*   `pandas`: For data manipulation and analysis.
*   `tabulate`: For creating formatted tables.

You can install these dependencies using pip:

```bash
pip install pandas tabulate
Use code with caution.
Markdown
Data Source
The script requires a CSV file named players.csv in the same directory. This file should contain at least the following columns:

position: Player position (e.g., QB, WR, RB).

height: Player height in feet-inches format (e.g., "6-2").

weight: Player weight in kilograms.

Example players.csv structure:

name,position,height,weight
Tom Brady,QB,6-4,102
Patrick Mahomes,QB,6-3,104
Derrick Henry,RB,6-3,112
Tyreek Hill,WR,5-10,84
Use code with caution.
Csv
Important: Ensure your players.csv file has headers in the first row. The script relies on these headers to access the correct data columns. If your data is in a different CSV file or has different column names, you will need to modify the file_path variable and the column selection in the script.

Usage
Clone the Repository: Clone this repository to your local machine.

git clone [repository_url]
cd [repository_directory]
Use code with caution.
Bash
Install Dependencies: Install the required Python libraries as described in the Dependencies section.

Place Data File: Make sure your players.csv file is in the same directory as the main.py script.

Run the Script: Execute the script using Python:

python main.py
Use code with caution.
Bash
Output
The script will print a table to the console showing the average height (in centimeters), weight (in kilograms), and BMI for each player position in the NFL. The table is formatted using the fancy_grid style of the tabulate library.

Example Output:

╒═══════════════╤═════════════╤═══════════════╤════════════════╕
│   posición    │   altura (cm) │   peso (kg)   │     IMC      │
╞═══════════════╪═════════════╪═══════════════╪════════════════╡
│ CB            │     182.88    │     90.7185   │     27.123   │
│ DE            │     190.5     │    120.202    │     33.123   │
│ DT            │     190.5     │    140.614    │     38.721   │
│ K             │     182.88    │     95.2544   │     28.4907  │
│ LB            │     187.96    │    108.862    │     30.7655  │
│ QB            │     190.5     │    102.058    │     28.1626  │
│ RB            │     177.8     │     95.2544   │     30.0515  │
│ TE            │     193.04    │    111.13    │     29.7986  │
│ WR            │     182.88    │     88.4504   │     26.445   │
╘═══════════════╧═════════════╧═══════════════╧════════════════╛
Use code with caution.
Code Explanation
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

# Seleccionar las columnas deseadas y renombrarlas a español
selected_columns = df[['position', 'height', 'weight', 'IMC']]
selected_columns.columns = ['posición', 'altura (cm)', 'peso (kg)', 'IMC']

# Calcular el promedio de altura, peso e IMC por cada posición
average_columns = selected_columns.groupby('posición').mean().reset_index()

# Mostrar los datos promediados usando tabulate con líneas continuas
print(tabulate(average_columns, headers='keys', tablefmt='fancy_grid'))
Use code with caution.
Python
import pandas as pd: Imports the pandas library for data manipulation.

from tabulate import tabulate: Imports the tabulate function for creating formatted tables.

file_path = 'players.csv': Defines the path to the CSV file containing player data.

df = pd.read_csv(file_path): Loads the data from the CSV file into a pandas DataFrame.

height_to_cm(height): A function that converts height from feet-inches format to centimeters.

df['height'] = df['height'].apply(height_to_cm): Applies the height_to_cm function to the 'height' column, converting all heights to centimeters.

df['IMC'] = df['weight'] / (df['height'] / 100) ** 2: Calculates the BMI for each player and stores it in a new 'IMC' column.

selected_columns = df[['position', 'height', 'weight', 'IMC']]: Selects the specified columns.

selected_columns.columns = ['posición', 'altura (cm)', 'peso (kg)', 'IMC']: Renames the selected columns to Spanish.

average_columns = selected_columns.groupby('posición').mean().reset_index(): Groups the data by position and calculates the mean of the height, weight, and IMC for each position.

print(tabulate(average_columns, headers='keys', tablefmt='fancy_grid')): Prints the calculated averages in a formatted table.
