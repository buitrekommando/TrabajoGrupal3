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