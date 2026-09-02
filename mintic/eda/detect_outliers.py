#Identifica la presencia de valores atípicos en el DataFrame basándose en un método estadístico y un umbral especificado.

import pandas as pd
import numpy as np

def mean(lista):
    return sum(lista) / len(lista)

def sd(lista):
    suma = 0

    for x in lista:
        suma += (x - mean(lista)) ** 2

    return np.sqrt(suma / len(lista))

    
def detect_outliers(df, method = 'iqr', umbral = 1.5):
    df2 = df.copy()
    
    num = []
    for c in list(df2.keys()):
        if pd.api.types.is_numeric_dtype(df2[c]):
            num.append(c)

    if method == 'iqr':
        for n in num:
            quart = df2[n].quantile([0.25, 0.75])
            iqr = quart[0.75] - quart[0.25]
            lim_inf = quart[0.25] - umbral * iqr
            lim_sup = quart[0.75] + umbral * iqr

            outliers_abajo = df2[n] < lim_inf 
            outliers_arriba = df2[n] > lim_sup
            df2[n] = outliers_abajo | outliers_arriba

    elif method == 'zscore':
        for n in num:
            outliers_arriba = (df2[n] - mean(df2[n])) / sd(df2[n]) > 3
            outliers_abajo = (df2[n] - mean(df2[n])) / sd(df2[n]) < -3
            df2[n] = outliers_arriba | outliers_abajo
            
    return df2
