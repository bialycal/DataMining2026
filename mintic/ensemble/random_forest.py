def bootstrap_sample(X, y, random_state = None):
    X_sample =  []
    Y_sample = []
    N =[] 
    for x in range(len(X) // 5):
        n = random.randint(1, len(X))
        X_sample.append(X.iloc[n])
        Y_sample.append(y.iloc[n].iloc[0])

    return tuple(X_sample), tuple(Y_sample)
