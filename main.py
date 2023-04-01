import networkx as nx

import PopGraph as pg


if __name__ == '__main__':
    exGraph = pg.PopGraph()
    exGraph.add_pops_from(
        [(44, 13), (36, 46), (39, 25), (0, 34), (65, 93), (82, 68), (68, 92), (52, 77), (67, 25), (88, 19)]
    )
    print(exGraph.find((39, 25)))

    exGraph.display()
