def adjacency_matrix(n):
    adjMat = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        u, v, w = map(int, input("Enter vertices and weight: ").split())
        adjMat[u][v] = w
        adjMat[v][u] = w
    
    return adjMat

nodes = int(input("Enter the number of vertices: "))
print(adjacency_matrix(nodes))