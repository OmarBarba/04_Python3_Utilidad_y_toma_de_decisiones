#El Proceso de Decisión de Markov (MDP) es un marco formal para 
#modelar problemas de decisión secuencial bajo incertidumbre. 
#Aquí tienes un ejemplo simplificado de cómo aplicar MDP en un 
#problema de búsqueda en un grafo:

import numpy as np

class MDP:
    def __init__(self, graph):
        self.graph = graph
        self.states = list(graph.keys())
        self.actions = self.calculate_actions()
        self.transitions = self.calculate_transitions()
        self.rewards = self.calculate_rewards()

    def calculate_actions(self):
        actions = []
        for state in self.states:
            for neighbor, cost in self.graph[state].items():
                actions.append((state, neighbor, cost))
        return actions

    def calculate_transitions(self):
        n_states = len(self.states)
        n_actions = len(self.actions)
        transitions = np.zeros((n_states, n_actions, n_states))

        for i, state in enumerate(self.states):
            for j, action in enumerate(self.actions):
                next_state = action[1]
                transitions[i, j, self.states.index(next_state)] = 1

        return transitions

    def calculate_rewards(self):
        rewards = np.zeros((len(self.states), len(self.actions)))

        for i, state in enumerate(self.states):
            for j, action in enumerate(self.actions):
                reward = action[2]
                rewards[i, j] = reward

        return rewards

def value_iteration(mdp, gamma, epsilon):
    n_states = len(mdp.states)
    n_actions = len(mdp.actions)
    values = np.zeros(n_states)

    while True:
        delta = 0
        for s in range(n_states):
            v = values[s]
            max_q = float('-inf')
            for a in range(n_actions):
                q = mdp.rewards[s, a] + gamma * np.sum(mdp.transitions[s, a, :] * values)
                max_q = max(max_q, q)
            values[s] = max_q
            delta = max(delta, abs(v - values[s]))
        if delta < epsilon:
            break

    return values

# Ejemplo de uso:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 5, 'F': 4},
    'D': {'B': 3},
    'E': {'B': 1, 'F': 6},
    'F': {'C': 4, 'E': 6}
}

mdp = MDP(graph)
gamma = 0.9
epsilon = 0.01

optimal_values = value_iteration(mdp, gamma, epsilon)
print("Valores óptimos por estado:")
for i, state in enumerate(mdp.states):
    print(f"Estado {state}: {optimal_values[i]}")
