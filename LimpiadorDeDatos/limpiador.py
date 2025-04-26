import pandas as pd

# Cargar datos
data = {
    'Nombre': ['Ana', 'Juan', 'Ana', None, 'Carlos'],
    'Email': ['ana@gmail.com', 'juan@gmail.com', 'ana@gmail.com', 'lucas@gmail.com', None]
}
df = pd.DataFrame(data)

print("Datos originales:")
print(df)

# Eliminar filas duplicadas
df = df.drop_duplicates()

# Eliminar filas con datos faltantes
df = df.dropna()

print("\nDatos limpios:")
print(df)
