def inertia(kmeans):
    #Construir los clusters como ya lo habíamos hecho en la otra función
    clusters = [[] for _ in range(kmeans["N_clusters"])]
        
    for p in kmeans["Puntos"]:
        dist = [0] * kmeans["N_clusters"] #aquí iremos almacenando la distancia del punto p a cada centroide
        for c in range(len(kmeans["Centroides"])):
            dist[c] = euclidean_distance(p, kmeans["Centroides"][c]) #la distancia de p a c

        mas_cercano = dist.index(min(dist))
        clusters[mas_cercano].append(p)

    inercia_por_cluster = []
    for cluster in range(len(clusters)):
        suma = 0
        for punto in clusters[cluster]:
            suma += ((euclidean_distance(punto, kmeans["Centroides"][cluster]))**2)

        inercia_por_cluster.append(suma)

    inercia_total = sum(inercia_por_cluster)

    return inercia_total
