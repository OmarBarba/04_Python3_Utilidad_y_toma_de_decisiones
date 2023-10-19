import numpy as np

# Definición del grafo
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 3},
    'C': {'D': 2, 'E': 2},
    'D': {'E': 1, 'F': 3},
    'E': {'F': 1},
    'F': {},
}

# Estados ocultos (nodos del grafo)
hidden_states = list(graph.keys())

# Acciones posibles
actions = ['move']

# Observaciones posibles (simplificadas)
observations = ['obs_A', 'obs_B', 'obs_C', 'obs_D', 'obs_E', 'obs_F']

# Modelo de transición: Probabilidad de moverse de un estado a otro
def transition_model(state, action):
    if action == 'move':
        return graph[state]

# Modelo de observación: Probabilidad de observar una ubicación dada
def observation_model(state, observation):
    true_location = observation.split('_')[1]
    return 0.9 if state == true_location else 0.1 / (len(hidden_states) - 1)

# Función para actualizar el belief state
def update_belief(belief, action, observation):
    new_belief = np.zeros(len(hidden_states))
    for i, state in enumerate(hidden_states):
        sum_val = 0
        for j, old_state in enumerate(hidden_states):
            transition_prob = transition_model(old_state, action)
            if state in transition_prob:
                sum_val += belief[j] * transition_prob[state]
        new_belief[i] = observation_model(state, observation) * sum_val
    return new_belief / np.sum(new_belief)

# Inicialización del belief state
initial_belief = np.array([1 / len(hidden_states)] * len(hidden_states))

# Simulación de una serie de acciones y observaciones
actions_and_observations = [('move', 'obs_A'), ('move', 'obs_B'), ('move', 'obs_C')]

belief_state = initial_belief
for action, observation in actions_and_observations:
    belief_state = update_belief(belief_state, action, observation)

# Imprimir el belief state final
print("Belief state final:")
for state, belief in zip(hidden_states, belief_state):
    print(f"{state}: {belief:.2f}")

