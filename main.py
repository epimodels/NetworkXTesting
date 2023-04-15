import networkx as nx

import PopGraph as px


if __name__ == '__main__':
    G = px.PopGraph()

    G.add_pop(1, 2)
    G.add_pop(3, 4)
    G.add_pop(5, 6)
    G.add_pop(7, 8)

    G.add_edge(G.find((1, 2)), G.find((3, 4)))
    G.add_edge()
    print(G.find((5, 6)))
    print(G.find((7, 8)))
