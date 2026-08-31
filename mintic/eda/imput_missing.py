#Recibe un DataFrame y una lista opcional de nombres de columnas, y debe imputar los valores faltantes según corresponda.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def impute_missing(df, columns = None):
    vacios = []
    columnas = list(df.keys())
    for c in columnas:
        if df[c].isnull().any():
            vacios.append(c)

        if len(vacios) == 0:
            return df
        #else: pendiente
