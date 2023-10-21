
#La iteración de políticas es otro enfoque para resolver problemas
# de decisión en grafos. En lugar de iterar sobre los valores de
#los estados como lo hacíamos en la iteración de valores, en la 
#iteración de políticas, iteramos directamente sobre las políticas,
# que son estrategias que determinan la acción a tomar en cada 
#estado. El objetivo es encontrar una política óptima que maximice 
#la recompensa esperada a lo largo del tiempo.

#A continuación, te proporciono un ejemplo simplificado de cómo 
#se podría aplicar la iteración de políticas en un problema de 
#decisión en un grafo:

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

def policy_iteration(graph, gamma, epsilon):
    # Inicialización de políticas
    policy = {node: None for node in graph.nodes}
    while True:
        values = value_evaluation(graph, policy, gamma, epsilon)
        policy_stable = True
        for node in graph.nodes:
            old_action = policy[node]
            best_action = None
            best_value = float('-inf')
            for edge in graph.edges.get(node, []):
                node2, action, reward = edge
                expected_value = reward + gamma * values[node2]
                if expected_value > best_value:
                    best_value = expected_value
                    best_action = action
            policy[node] = best_action
            if old_action != best_action:
                policy_stable = False
        if policy_stable:
            break
    return policy

def value_evaluation(graph, policy, gamma, epsilon):
    values = {node: 0 for node in graph.nodes}
    while True:
        delta = 0
        for node in graph.nodes:
            v = values[node]
            action = policy[node]
            expected_value = 0
            for edge in graph.edges.get(node, []):
                node2, edge_action, reward = edge
                if action == edge_action:
                    expected_value += reward + gamma * values[node2]
            values[node] = expected_value
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

optimal_policy = policy_iteration(graph, gamma, epsilon)
print("Política óptima:")
for node, action in optimal_policy.items():
    print(f"Nodo {node}: Acción {action}")
