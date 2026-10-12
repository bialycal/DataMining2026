def create_kmeans(data, n_clusters = 9, max_iter = 100, tol = 0.0001, randomstate = None):
    np.random.seed(randomstate)
    data = data.to_numpy()
    centroides = [tuple(X.iloc[np.random.randint(len(X))]) for _ in range(n_clusters)]

    return {"Puntos": data, "Centroides": centroides, "N_clusters": n_clusters, "Max_iter": max_iter, "Tolerancia": tol}
