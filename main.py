import networkx as nx

import PopGraph as pg


if __name__ == '__main__':

    G = pg.PopGraph(nx.petersen_graph())

    G = G.auto_populate()

    G.display()
