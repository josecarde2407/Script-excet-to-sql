import pandas as pd
import mysql.connector

# Configuración de la conexión a la base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password':'Asul270220.',
    'database':'Bd_Datos'
}

# Conexión a la base de datos
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Ruta al archivo Excel
excel_file = 'INSERT_BD_CLI_ART.xlsx'

# Leer el archivo Excel
df = pd.read_excel(excel_file)

# Nombre de la tabla en la base de datos
table_name = 'cli_art'


# Generar la sentencia SQL para insertar datos en la tabla
columns = ', '.join(df.columns)
values = ', '.join(['%s'] * len(df.columns))
insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

# Insertar datos en la base de datos
for row in df.itertuples(index=False):
    # Verificar si el artículo ya existe en la base de datos
    exist_query = f"SELECT COUNT(*) FROM {table_name} WHERE n_articulo = %s"
    cursor.execute(exist_query, (row.n_articulo,))
    result = cursor.fetchone()
    if result[0] == 0:  # Si el artículo no existe, insertarlo
        cursor.execute(insert_query, tuple(row))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Los datos se han insertado correctamente en la base de datos.")
