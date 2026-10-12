def kmeans_fit(kmeans, verbose = True):
    for rep in range(kmeans["Max_iter"]):
        clusters = [[] for _ in range(kmeans["N_clusters"])]
        
        for p in kmeans["Puntos"]:
            dist = [0] * kmeans["N_clusters"] #aquí iremos almacenando la distancia del punto p a cada centroide
            for c in range(len(kmeans["Centroides"])):
                dist[c] = euclidean_distance(p, kmeans["Centroides"][c]) #la distancia de p a c
    
            mas_cercano = dist.index(min(dist))
            clusters[mas_cercano].append(p)
    
        nuevos_centroides = []
        for i, cluster in enumerate(clusters):
            if len(cluster) > 0:
                nuevos_centroides.append(np.mean(cluster, axis=0))
            else:
                nuevos_centroides.append(kmeans["Centroides"][i])
        
        diferencia_centroides = []
        for anterior, nuevo in zip(kmeans["Centroides"], nuevos_centroides):
            diferencia_centroides.append(euclidean_distance(anterior, nuevo))

        kmeans["Centroides"] = nuevos_centroides
        
        if max(diferencia_centroides) < kmeans["Tolerancia"]:
            break
    
    return kmeans
