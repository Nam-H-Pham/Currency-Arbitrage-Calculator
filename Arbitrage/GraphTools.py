def floyd_warshall_with_cycles(graph):
    num_vertices = len(graph)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    next_node = [[None] * num_vertices for _ in range(num_vertices)]

    # Initialize distance and next_node matrices
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 1
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
                next_node[i][j] = j

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] * dist[k][j]:
                    dist[i][j] = dist[i][k] * dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Detect cycles
    cycles = []
    for i in range(num_vertices):
        if dist[i][i] < 1:
            cycle = []
            v = i
            while True:
                cycle.append(v)
                v = next_node[v][i]
                if v == i or v in cycle:
                    cycle.append(i)
                    break
            cycles.append(cycle)

    return dist, cycles


# A utility function to print the solution
def printGraph(dist, labels=None):
    import tabulate
    print(tabulate.tabulate(dist, tablefmt='grid', showindex=labels, headers=labels))

def get_product_of_path(graph, path):
    product = 1
    for i in range(len(path) - 1):
        product *= graph[path[i]][path[i + 1]]
    return product


if __name__ == "__main__":
    graph = [
                [1, 0.1, float('inf')],
                [float('inf'), 1, 0.1],
                [0.1, float('inf'), 1]
            ]
    
    solution, negative_cycles = floyd_warshall_with_cycles(graph)
    
    print("Distance matrix:")
    printGraph(solution)

    print("Negative cycles:", len(negative_cycles))
    for cycle in negative_cycles:
        print("Negative cycle:", cycle, get_product_of_path(graph, cycle))
