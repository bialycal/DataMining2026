#Identifica la presencia de valores atípicos en el DataFrame basándose en un método estadístico y un umbral especificado.

def detect_outliers(df, method = 'iqr', umbral = 1.5):
    df2 = df.copy()
    
    num = []
    for c in list(df2.keys()):
        if pd.api.types.is_numeric_dtype(df2[c]):
            num.append(c)

    for n in num:
        quart = df2[n].quantile([0.25, 0.75])
        iqr = quart[0.75] - quart[0.25]
        lim_inf = quart[0.25] - umbral * iqr
        lim_sup = quart[0.75] + umbral * iqr
        
        for m in df2[n]:
            if (m < lim_inf) or (m > lim_sup):
                #m = True
            else:
                #m = False
    return df2
