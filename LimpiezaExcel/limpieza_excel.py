import pandas as pd

# Cargar el archivo Excel
archivo = "archivo_original.xlsx"  # ← Cambia esto por el nombre de tu archivo
df = pd.read_excel(archivo)

# Mostrar las primeras filas para ver cómo se ve
print("Datos originales:")
print(df.head())

# 1. Eliminar filas completamente vacías
df = df.dropna(how='all')

# 2. Eliminar espacios extra en los nombres de columnas
df.columns = df.columns.str.strip()

# 3. Eliminar espacios extra en los textos de todas las columnas tipo texto
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

# 4. Guardar el archivo limpio
archivo_salida = "archivo_limpio.xlsx"
df.to_excel(archivo_salida, index=False)

print(f"Archivo limpio guardado como {archivo_salida}")
