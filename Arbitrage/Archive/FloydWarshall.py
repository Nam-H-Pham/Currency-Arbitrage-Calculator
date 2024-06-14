# Python3 Program for Floyd Warshall Algorithm

V = 4

def floyd_warshall_with_cycles(graph):
    """
    Floyd-Warshall algorithm to find shortest paths and detect cycles in a graph.

    :param graph: 2D list representing the adjacency matrix of the graph, where graph[i][j] is the weight of the edge from vertex i to vertex j
    :return: tuple containing the distance matrix and a list of cycles detected in the graph
    """
    num_vertices = len(graph)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    next_node = [[None] * num_vertices for _ in range(num_vertices)]

    # Initialize distance and next_node matrices
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
                next_node[i][j] = j

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Detect cycles
    cycles = []
    for i in range(num_vertices):
        if dist[i][i] < 0:
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
def printGraph(dist):
    import tabulate
    print(tabulate.tabulate(dist, tablefmt='grid'))

def checkNegativeCycle(dist):
    for i in range(V):
        if dist[i][i] < 0:
            return True
    return False

def get_sum_of_path(graph, path):
    sum = 0
    for i in range(len(path) - 1):
        sum += graph[path[i]][path[i + 1]]
    return sum


if __name__ == "__main__":
    graph = [
                [0, -1, float('inf')],
                [float('inf'), 0, -1],
                [-1, float('inf'), 0]
            ]
    
    solution, negative_cycles = floyd_warshall_with_cycles(graph)
    print("Following matrix shows the shortest distances between every pair of vertices")
    
    print("Distance matrix:")
    printGraph(solution)

    for cycle in negative_cycles:
        print("Negative cycle:", cycle, get_sum_of_path(graph, cycle))
