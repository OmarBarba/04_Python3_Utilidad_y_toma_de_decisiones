class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.utility = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, action, reward):
        if node1 not in self.edges:
            self.edges[node1] = []
        self.edges[node1].append((node2, action, reward))

def value_iteration(graph, gamma, epsilon):
    # Inicialización de valores
    values = {node: 0 for node in graph.nodes}
    while True:
        delta = 0
        for node in graph.nodes:
            v = values[node]
            best_value = float('-inf')
            for edge in graph.edges.get(node, []):
                node2, action, reward = edge
                expected_value = reward + gamma * values[node2]
                best_value = max(best_value, expected_value)
            values[node] = best_value
            delta = max(delta, abs(v - values[node]))
        if delta < epsilon:
            break
    return values

# Ejemplo de uso:
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_edge('A', 'B', 'Action1', 5)
graph.add_edge('A', 'B', 'Action2', 3)
graph.add_edge('B', 'C', 'Action3', 2)
graph.add_edge('B', 'C', 'Action4', 1)
graph.add_edge('C', 'A', 'Action5', 7)

gamma = 0.9
epsilon = 0.01

values = value_iteration(graph, gamma, epsilon)
print("Valores óptimos de los nodos:")
for node, value in values.items():
    print(f"Nodo {node}: {value:.2f}")
