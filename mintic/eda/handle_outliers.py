#Procesa los valores atípicos detectados en el DataFrame, permitiendo eliminarlos o recortarlos según la acción indicada.
import pandas as pd
import numpy as np

def mean(lista):
    return sum(lista) / len(lista)

def sd(lista):
    suma = 0

    for x in lista:
        suma += (x - mean(lista)) ** 2

    return np.sqrt(suma / len(lista))

def handle_outliers(df, method = 'iqr', action = 'trim', threshold = 1.5):
    df2 = df.copy()
    
    cols = []
    for c in list(df2.keys()):
        if pd.api.types.is_numeric_dtype(df2[c]):
            cols.append(c)

    if action == 'trim':
        for col in cols:
            if method == 'iqr':
                quart = df2[col].quantile([0.25, 0.75])
                iqr = quart[0.75] - quart[0.25]
                lim_inf = quart[0.25] - threshold * iqr
                lim_sup = quart[0.75] + threshold * iqr
                dropear = (df2[col] < lim_inf) | (df2[col] > lim_sup)
                df2 = df2.drop(df2[dropear].index)
            elif method == 'zscore':
                outliers_arriba = (df2[col] - mean(df2[col])) / sd(df2[col]) > threshold
                outliers_abajo = (df2[col] - mean(df2[col])) / sd(df2[col]) < -threshold
                dropear = (outliers_arriba | outliers_abajo)
                df2 = df2.drop(df2[dropear].index)
    elif action == 'cap':
        for col in cols:
            if method == 'iqr':
                    quart = df2[col].quantile([0.25, 0.75])
                    iqr = quart[0.75] - quart[0.25]
                    lim_inf = quart[0.25] - threshold * iqr
                    lim_sup = quart[0.75] + threshold * iqr
                    df2.loc[df2[col] < lim_inf, col] = lim_inf
                    df2.loc[df2[col] > lim_sup, col] = lim_sup
            elif method == 'zscore':
                outliers_arriba = mean(df2[col]) + threshold * sd(df2[col])
                outliers_abajo = mean(df2[col]) - threshold * sd(df2[col])
                df2.loc[df2[col] < outliers_abajo, col] = outliers_abajo
                df2.loc[df2[col] > outliers_arriba, col] = outliers_arriba

    return df2
