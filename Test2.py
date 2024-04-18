import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


# Filtrar zonas de alto transporte público
altas_zonas_transporte = df[df["public_transportation_pct"] > 10]

# Calcular ventas potenciales promedio en zonas de alto transporte público
ventas_potenciales_promedio_altas = altas_zonas_transporte["public_transportation_population"].mean()

# Filtrar zonas de bajo transporte público
bajas_zonas_transporte = df[df["public_transportation_pct"] <= 10]

# Calcular ventas potenciales promedio en zonas de bajo transporte público
ventas_potenciales_promedio_bajas = bajas_zonas_transporte["public_transportation_population"].mean()

print(f"Ventas potenciales promedio en zonas de alto transporte público: {ventas_potenciales_promedio_altas}")
print(f"Ventas potenciales promedio en zonas de bajo transporte público: {ventas_potenciales_promedio_bajas}")


sns.histplot(data=df, x="public_transportation_pct", weights="public_transportation_population",bins=100, kde=False)
plt.savefig("imagenHistograma.png")
plt.show()

# Agrupar potenciales clientes por código postal y calcular el número promedio de ventas
ventas_promedio_por_codigo_postal = df.groupby("zip_code")["public_transportation_population"].mean()

# Crear un diagrama de dispersión para visualizar la relación entre el uso del transporte público y las potenciales ventas
plt.scatter(df["public_transportation_pct"], df["public_transportation_population"])
plt.xlabel("Uso del transporte público (%)")
plt.ylabel("Potenciales ventas")
plt.title("Relación entre el uso del transporte público y las potenciales ventas")
plt.savefig("imagenDispersion.png")
plt.show()


df.to_excel("datos_exportados.xlsx", index=False)



"""Basándome en el análisis proporcionado, aquí hay algunas recomendaciones para el equipo de marketing de la empresa de scooters:

1. Enfocarse en Zonas de Alto Uso de Transporte Público: Las zonas con un alto porcentaje de uso del transporte público podrían ser mercados clave para los scooters, ya que las personas pueden estar buscando opciones de transporte personal para complementar su viaje.
2. Promociones en Zonas de Bajo Uso de Transporte Público: Considerar promociones o descuentos en áreas con bajo uso de transporte público, donde las personas podrían estar más inclinadas a considerar alternativas de transporte personal como los scooters.
3. Publicidad Dirigida por Código Postal: Utilizar los datos de ventas promedio por código postal para dirigir la publicidad y las promociones a áreas con mayores ventas potenciales.
4. Análisis de Datos Continuo: Mantener un análisis continuo de los datos para identificar tendencias emergentes o cambios en los patrones de uso del transporte público que podrían influir en las oportunidades de ventas.
5. Optimización de la Cadena de Suministro: Asegurarse de que la cadena de suministro esté optimizada para satisfacer la demanda en las zonas identificadas con altas ventas potenciales.
6. Colaboraciones Estratégicas: Buscar colaboraciones con servicios de transporte público para ofertas conjuntas o programas de fidelidad que puedan incentivar la compra de scooters.
7. Educación del Consumidor: Desarrollar campañas educativas sobre los beneficios de los scooters, como la conveniencia y el ahorro de tiempo, especialmente en áreas con alta densidad de población y uso del transporte público.
8. Monitoreo de la Competencia: Vigilar las actividades de la competencia en las áreas objetivo para ajustar las estrategias de marketing y oferta de productos según sea necesario."""