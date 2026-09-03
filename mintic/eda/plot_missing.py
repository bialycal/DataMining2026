#Genera una representación visual que muestra la cantidad o proporción de valores faltantes por columna en el DataFrame.
import pandas as pd
import matplotlib.pyplot as plt

def plot_missing(df):
    nulls = df.isnull().sum()
    nulls2 = nulls[nulls > 0]

    plt.figure(figsize=(10, 5))
    plt.bar(nulls.index, nulls.values, color = "pink")
    plt.xlabel('Columnas')
    plt.ylabel('Cantidad valores faltantes')
    plt.title('Valores faltantes por columna')
    plt.xticks(rotation=45)
    
    plt.show()

plot_missing(df)
