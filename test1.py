import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("datos.csv")

# Limpiar Data:
df.dropna(inplace=True)

df[df < 0] = 0
df = df[df > 0]

print(df.describe())

# Maximos y minimos
maximo = df["public_transportation_pct"].max()
print(f"Los valores maximos de la columna public_transportation_pct son: \n{maximo}")

valores_minimos_positivos = df[df["public_transportation_pct"] > 0]["public_transportation_pct"].min()
print(f"Los valores mínimos positivos de la columna public_transportation_pct son: \n{valores_minimos_positivos}")

# Fila con maximos
maximo = df[df["public_transportation_pct"] == df["public_transportation_pct"].max()]
print(f"Las fila con maximos es: \n{maximo}")
# Filas con minimos
valores_minimos_positivos = df[df["public_transportation_pct"] > 0]
print(f"Las filas con valores mínimos positivos de la columna public_transportation_pct son: \n{valores_minimos_positivos}")

# Crear nuevas columnas
df["minimo"] = df.min(axis=1)
df["maximo"] = df.max(axis=1)

# Reemplazar valores menores que cero por cero
df[df < 0] = 0

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv("datos_modificados.csv", index=False)

# Leer el archivo CSV modificado
df_modificado = pd.read_csv("datos_modificados.csv")

# Filtrar clientes en zonas de alto transporte público
alto_transporte = df_modificado[df_modificado["public_transportation_pct"] > 10]

# Calcular ventas potenciales promedio para clientes en zonas de alto transporte público
ventas_potenciales_alto = alto_transporte.groupby("zip_code")["maximo"].mean()

# Filtrar clientes en zonas de bajo transporte público
bajo_transporte = df_modificado[df_modificado["public_transportation_pct"] <= 10]

# Calcular ventas potenciales promedio para clientes en zonas de bajo transporte público
ventas_potenciales_bajo = bajo_transporte.groupby("zip_code")["maximo"].mean()

# Imprimir resultados
print("Ventas potenciales promedio para clientes en zonas de alto transporte público:")
print(ventas_potenciales_alto)

print("Ventas potenciales promedio para clientes en zonas de bajo transporte público:")
print(ventas_potenciales_bajo)

# Leer los datos en Pandas
df = pd.read_csv("datos.csv")

# Graficar histograma de la distribución
plt.hist(df["public_transportation_pct"], bins=10)
plt.xlabel("Porcentaje de transporte público")
plt.ylabel("Frecuencia")
plt.title("Distribución del porcentaje de transporte público")
plt.show()


# Agrupar potenciales clientes por zip_code y calcular el número promedio de ventas
ventas_promedio = df_modificado.groupby("zip_code")["maximo"].mean()

# Crear diagrama de dispersión para visualizar la relación entre el uso del transporte público y las potenciales ventas
plt.scatter(df_modificado["public_transportation_pct"], df_modificado["maximo"])
plt.xlabel("Porcentaje de transporte público")
plt.ylabel("Ventas potenciales")
plt.title("Relación entre el uso del transporte público y las potenciales ventas")
plt.show()

# Exportar los datos a un archivo Excel
df_modificado.to_excel("datos_modificados.xlsx", index=False)
