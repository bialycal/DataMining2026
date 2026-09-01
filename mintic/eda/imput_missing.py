#Recibe un DataFrame y una lista opcional de nombres de columnas, y debe imputar los valores faltantes según corresponda.

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
                df2[v] = df2[v].fillna(df2[v].mean())
            elif strategy == "median":
                df2[v] = df2[v].fillna(df2[v].median())
            elif strategy == "mode":
                df2[v] = df2[v].fillna(df2[v].mode()[0])
        return df2
