def expected_utility(decision, evidence, network):
    utility = 0

    for value in decision['values']:
        evidence[decision['name']] = value
        utility += decision['probability'][value] * decision['utility'][value]

    return utility

def value_of_information(decision, evidence, network):
    current_utility = expected_utility(decision, evidence, network)

    potential_utility = 0

    for value in decision['values']:
        evidence[decision['name']] = value
        future_decision = network['decision']
        potential_utility += expected_utility(future_decision, evidence, network)

    return potential_utility - current_utility

# Ejemplo de uso:
network = {
    'decision': {
        'name': 'Decision',
        'values': ['A', 'B'],
        'probability': {'A': 0.6, 'B': 0.4},
        'utility': {'A': 10, 'B': 8}
    }
}

evidence = {}

voi = value_of_information(network['decision'], evidence, network)
print("Valor de la Información:", voi)


##########################BUSQUEDA DE GRAFOS######################
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, cost):
        self.edges.append((node1, node2, cost))

def calculate_shortest_path(graph, start, goal):
    # Simulación de un algoritmo de búsqueda, como Dijkstra o A*
    # para calcular el camino más corto entre dos nodos.
    # En este ejemplo, simplemente devolvemos un valor arbitrario para simplificar.
    return 10

def calculate_voi(graph, current_node, decision, goal):
    best_path = calculate_shortest_path(graph, current_node, goal)

    # Supongamos que tenemos dos opciones, con y sin información adicional.
    with_information_path = calculate_shortest_path(graph, current_node, decision)
    without_information_path = calculate_shortest_path(graph, decision, goal)

    voi = best_path - min(with_information_path, without_information_path)
    return voi

# Ejemplo de uso:
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)
graph.add_edge('A', 'C', 8)

current_node = 'A'
decision = 'C'
goal = 'C'

voi = calculate_voi(graph, current_node, decision, goal)
print("Valor de la Información:", voi)
