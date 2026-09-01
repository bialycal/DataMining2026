#Recibe un DataFrame y una lista opcional de nombres de columnas, y debe imputar los valores faltantes según corresponda.

def mean(lista):
    return sum(lista) / len(lista)

def median(lista):
    lista.sort()
    if len(lista) %2 == 1:
        return lista[len(lista)//2]
    else:
        return (lista[len(lista)//2 - 1] + lista [len(lista)//2]) / 2

def mode(lista):
    moda  = pd.DataFrame(lista).value_counts()
    return moda.index[0][0]

def impute_missing(df, strategy = "mean", columns = None):
    df2= df.copy()
    vacios = []
    columnas = list(df2.keys())
    for c in columnas:
        if df2[c].isnull().any():
            vacios.append(c)
            
    if len(vacios) == 0:
        return df2

    else:
        for v in vacios:
            if strategy == "mean":
                df2[v] = df2[v].fillna(mean(df2[v]))
            elif strategy == "median":
                df2[v] = df2[v].fillna(median(df2[v]))
            elif strategy == "mode":
                df2[v] = df2[v].fillna(mode(df2[v]))
        return df2
