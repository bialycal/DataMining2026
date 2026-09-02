#Procesa los valores atípicos detectados en el DataFrame, permitiendo eliminarlos o recortarlos según la acción indicada.
import pandas as pd
import numpy as np
from detect_outliers.py import detect_outliers

def handle_outliers(df, method = 'iqr', action = 'trim', threshold = 1.5):
    df2 = df.copy()
    
    df2 = detect_outliers(df2)
    
    cols = []
    for c in list(df2.keys()):
        if pd.api.types.is_boolean_dtype(df2[c]):
            cols.append(c)

    if action == 'trim':
        #Eliminar filas
    elif action == 'cap':
        #Recortar valores a los límites
