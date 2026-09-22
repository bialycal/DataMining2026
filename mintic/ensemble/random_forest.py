def bootstrap_sample(X, y, random_state = None):
    X_sample =  []
    Y_sample = []
    N =[] 
    for x in range(len(X) // 5):
        n = random.randint(1, len(X))
        X_sample.append(X.iloc[n])
        Y_sample.append(y.iloc[n].iloc[0])

    return tuple(X_sample), tuple(Y_sample)


#-------------------------------------------------------------------------

def entropia(y):
    labels, conteos = np.unique(y, return_counts=True)
    probabilidades = conteos / len(y)

    return -np.sum(probabilidades * np.log2(probabilidades))


def ganancia_informacion(X_col, y):
    entropia_inicial = entropia(y)
    valores = np.unique(X_col)
    entropia_condicional = 0

    for valor in valores:
        mascara = X_col == valor
        y_sub = y[mascara]
        peso = len(y_sub) / len(y)
        entropia_condicional += peso * entropia(y_sub)

    return entropia_inicial - entropia_condicional

def entropia(y):
    clases, conteos = np.unique(y, return_counts=True)
    probabilidades = conteos / len(y)

    return -np.sum(probabilidades * np.log2(probabilidades))


def ganancia_informacion(X_col, y):
    entropia_inicial = entropia(y)
    valores = np.unique(X_col)
    entropia_condicional = 0

    for valor in valores:
        mascara = X_col == valor
        y_sub = y[mascara]
        peso = len(y_sub) / len(y)
        entropia_condicional += peso * entropia(y_sub)

    return entropia_inicial - entropia_condicional


def build_id3_tree(X, y):
    X = np.asarray(X)
    y = np.asarray(y)
    clases = np.unique(y)
    
    #Caso 1 cuando todas las muestras tienen la misma clase
    if len(clases) == 1:
        return {
            "tipo": "hoja", "clase": clases[0]}

    #Caso 2 cuando ya no se puede dividir más
    if X.shape[1] == 0:
        valores, conteos = np.unique(y, return_counts=True)
        clase_mayoritaria = valores[np.argmax(conteos)]

        return {"tipo": "hoja", "clase": clase_mayoritaria}

    #Ganancia de información
    ganancias = np.array([ganancia_informacion(X[:, j], y) for j in range(X.shape[1])])
    mejor_caracteristica = np.argmax(ganancias)

    #Si ninguna característica es especialmente mejor que las demás, usamos la clase mayoritaria
    if ganancias[mejor_caracteristica] == 0:
        valores, conteos = np.unique(y, return_counts=True)
        clase_mayoritaria = valores[np.argmax(conteos)]

        return {
            "tipo": "hoja",
            "clase": clase_mayoritaria
        }

    #Crear nodo
    arbol = {
        "tipo": "nodo",
        "caracteristica": mejor_caracteristica,
        "ganancia": ganancias[mejor_caracteristica],
        "ramas": {}
    }

    valores = np.unique(X[:, mejor_caracteristica])

    for valor in valores:
        mascara = X[:, mejor_caracteristica] == valor
        X_sub = X[mascara]
        y_sub = y[mascara]
        X_sub = np.delete(X_sub, mejor_caracteristica, axis=1)
        arbol["ramas"][valor] = build_id3_tree(X_sub, y_sub)

    return arbol

#----------------------------------------------------------------------------------------------

def build_random_forest(X, y, n_trees = 10, random_state = None):
    arboles_entrenados = []
    for n in range(n_trees):
        arboles_entrenados.append(build_id3_tree(X, y))
   
    return arboles_entrenados

#------------------------------------------------------------------------------

def predict_ensemble(trees, x):
    predicciones_finales = []
    for muestra in x:
        votos = []
        for tree in trees:
            nodo = tree
            muestra_actual = muestra.copy()
            while nodo["tipo"] != "hoja":
                caracteristica = nodo["caracteristica"]
                valor = muestra_actual[caracteristica]
                nodo = nodo["ramas"][valor]
                muestra_actual = np.delete(muestra_actual, caracteristica)
            votos.append(nodo["clase"])

        clases, conteos = np.unique(votos, return_counts=True)
        max_votos = np.max(conteos)
        empatadas = clases[conteos == max_votos]
        clase_final = sorted(empatadas, key=str)[0] #escoger alfabéticamente si dos o más empataron
        predicciones_finales.append(clase_final)

    return np.array(predicciones_finales)
