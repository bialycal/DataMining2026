import matplotlib.pyplot as plt

def elbow(data, min = 2, max = 8, max_iter = 1000, tol = 0.001, randomstate = None):
    inercias = []
    valores_k = list(range(min, max + 1))

    for k in valores_k:
        modelo = create_kmeans(data, k, max_iter, tol, randomstate)
        modelo = kmeans_fit(modelo, verbose=False)
        inercias.append(inertia(modelo))

    plt.plot(valores_k, inercias, marker='o')
    plt.xlabel("Número de clusters (k)")
    plt.ylabel("Inercia")
    plt.title("Método del codo")
    plt.xticks(valores_k)
    plt.grid(True)
    plt.show()
