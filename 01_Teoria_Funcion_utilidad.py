#La teoría de la utilidad se utiliza comúnmente en la toma de 
#decisiones para asignar un valor a las diferentes opciones 
#y elegir la que maximice la utilidad. Puedes utilizar la 
#teoría de la utilidad en la búsqueda de grafos cuando necesitas
#elegir entre diferentes rutas o soluciones en función de un valor
# de utilidad. Aquí tienes un ejemplo de cómo podrías aplicar la 
#teoría de la utilidad a un problema de búsqueda de rutas:

import random

# Definición del grafo como diccionario de adyacencia
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1, 'D': 4},
    'C': {'A': 2, 'B': 1, 'E': 5},
    'D': {'B': 4, 'E': 2},
    'E': {'C': 5, 'D': 2}
}

# Función para calcular la utilidad de una ruta (puede ser la distancia, el tiempo, etc.)
def calculate_utility(route, graph):
    total_utility = 0
    for i in range(len(route) - 1):
        node1, node2 = route[i], route[i + 1]
        if node2 in graph[node1]:
            total_utility += graph[node1][node2]
        else:
            return float('inf')  # Ruta inválida
    return total_utility

# Algoritmo de búsqueda para encontrar la ruta de máxima utilidad
def find_best_route(graph, start, goal):
    best_route = None
    best_utility = float('-inf')

    # Realizar una búsqueda exhaustiva (esto puede ser costoso para grafos grandes)
    for _ in range(1000):  # Número de iteraciones
        current_route = [start]
        while current_route[-1] != goal:
            neighbors = list(graph[current_route[-1]].keys())
            next_node = random.choice(neighbors)
            current_route.append(next_node)
        current_utility = calculate_utility(current_route, graph)
        if current_utility > best_utility:
            best_route = current_route
            best_utility = current_utility

    return best_route, best_utility

# Ejemplo de uso
start_node = 'A'
goal_node = 'E'
best_route, best_utility = find_best_route(graph, start_node, goal_node)

if best_route:
    print(f"Mejor ruta de {start_node} a {goal_node}: {best_route}")
    print(f"Utilidad máxima: {best_utility}")
else:
    print(f"No se encontró una ruta válida de {start_node} a {goal_node}.")


############################################################
####################Funcion utilidad########################

# Función de utilidad que asigna valores a las opciones en función de la preferencia del usuario.
def calculate_utility(option):
    # Podrías tener una lógica más compleja para calcular la utilidad.
    if option == 'A':
        return 10
    elif option == 'B':
        return 8
    else:
        return 0

# Opciones disponibles para el usuario.
options = ['A', 'B']

# Simulación de la toma de decisiones.
print("Toma de decisiones:")
print("Opción A: Hacer algo beneficioso")
print("Opción B: Hacer algo menos beneficioso")

# El usuario elige una opción.
user_choice = input("Elige una opción (A o B): ")

if user_choice in options:
    utility = calculate_utility(user_choice)
    print(f"Has elegido la opción {user_choice}. La utilidad de esta elección es {utility}.")
else:
    print("Opción no válida. Debes elegir entre A o B.")
