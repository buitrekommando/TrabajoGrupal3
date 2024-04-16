import pandas as pd

df = pd.read_csv("datos.csv")
df.head(3)
print(df.info())