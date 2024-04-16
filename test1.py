import pandas as pd

data_frame = pd.read_csv("datos.csv")
data_frame.head(3)

#print(data_frame) #imprime solo los 5 primeros y 5 ultimos
#print(frame_datos.to_string()) #imprime todo el Dataframe
#print(pd.options.display.max_rows) 

#Limpiar Data: 
data_frame.dropna(inplace = True)
print(data_frame.info())