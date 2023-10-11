import networkx as nx
import matplotlib.pyplot as plt

zoo_graph = nx.Graph()

zoo_graph.add_node("Polar bear")
zoo_graph.add_node("Goat")
zoo_graph.add_node("Dolphin")
zoo_graph.add_node("Lion")
zoo_graph.add_node("Squirrel")
zoo_graph.add_node("Octopus")
zoo_graph.add_node("Pigeon")
zoo_graph.add_node("Giraffe")
zoo_graph.add_node("Snake")
zoo_graph.add_node("Crocodile")
zoo_graph.add_node("Monkey")
zoo_graph.add_node("Buffalo")
zoo_graph.add_node("Rabbits")

zoo_graph.add_edges_from([
    ("Polar bear", "Goat"),
    ("Polar bear", "Dolphin"),
    ("Polar bear", "Pigeon"),
    ("Pigeon", "Dolphin"),
    ("Pigeon", "Octopus"),
    ("Pigeon","Buffalo"),
    ("Buffalo", "Monkey"),
    ("Monkey", "Crocodile"),
    ("Monkey", "Rabbits"),
    ("Monkey", "Lion"),
    ("Lion", "Giraffe"),
    ("Lion", "Squirrel"),
    ("Squirrel", "Goat"),
    ("Giraffe", "Snake"),

])

def get_neighbors(animal):
    neighbors = list(zoo_graph.neighbors(animal))
    return neighbors



pos = nx.spring_layout(zoo_graph)
plt.figure(figsize=(10, 8))
nx.draw(zoo_graph, pos, with_labels=True, node_size=500, node_color='w', font_size=10, font_color='purple', font_weight='bold', edge_color='black')
plt.title("Структурный зоопарк")
plt.show()

input_animal = "Goat"

neighbors = get_neighbors(input_animal)
print(f"Neighbors у {input_animal}: {neighbors}")

