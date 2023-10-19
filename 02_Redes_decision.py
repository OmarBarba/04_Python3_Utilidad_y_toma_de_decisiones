class Node:
    def __init__(self, name, parents, values, utility_function=None):
        self.name = name
        self.parents = parents
        self.values = values
        self.utility_function = utility_function

class DecisionNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_node_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

def calculate_utility(node, assignment):
    if node.utility_function:
        return node.utility_function(assignment)
    return 0

def decision_network_search(network, decision_sequence, evidence):
    utility = 0
    assignment = {}

    for decision in decision_sequence:
        node = network.get_node_by_name(decision)
        if node:
            options = node.values
            best_option = None
            max_utility = float('-inf')

            for option in options:
                assignment[decision] = option
                utility_for_option = calculate_utility(node, assignment)
                if utility_for_option > max_utility:
                    max_utility = utility_for_option
                    best_option = option

            assignment[decision] = best_option
            utility += max_utility

    for evidence_node, evidence_value in evidence.items():
        node = network.get_node_by_name(evidence_node)
        if node:
            assignment[evidence_node] = evidence_value
            utility += calculate_utility(node, assignment)

    return utility, assignment

# Ejemplo de uso:
def utility_function(assignment):
    if assignment['Decision'] == 'A':
        return 10
    elif assignment['Decision'] == 'B':
        return 8
    return 0

network = DecisionNetwork()
network.add_node(Node('Decision', [], ['A', 'B'], utility_function))
network.add_node(Node('Event', ['Decision'], ['Good', 'Bad']))

decision_sequence = ['Decision']
evidence = {'Event': 'Good'}

utility, assignment = decision_network_search(network, decision_sequence, evidence)
print("Utilidad total:", utility)
print("Asignación:", assignment)
