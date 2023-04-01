import unittest
import networkx as nx
import networkx.algorithms.isomorphism as iso

from main import *


def setup(self):
    exGraph = pg.PopGraph()
    exGraph.add_pop(44, 13)


# finds the greatest difference in population between graphs
def compare(g1, g2):
    lst1 = list(g1.nodes)
    lst2 = list(g2.nodes)

    popDif = 0

    for i in range(len(lst1)):
        temp1 = abs(lst1[i].pop1 - lst2[i].pop1)
        temp2 = abs(lst1[i].pop2 - lst2[i].pop2)
        if temp1 > popDif:
            popDif = temp1
        if temp2 > popDif:
            popDif = temp2

    return popDif


class TestPopGraph(unittest.TestCase):

    # test the auto_populate method
    def test_auto_populate(self):
        G1 = pg.PopGraph(nx.petersen_graph())
        G2 = G1.auto_populate()
        # The populated graph should be isomorphic to the passed graph
        self.assertTrue(iso.is_isomorphic(G1, G2))
        # Each node in the populated graph is a PopNode where both attributes are ints.
        for node in G2.nodes:
            self.assertTrue(isinstance(node, pg.PopNode))
            self.assertTrue(isinstance(node.pop1, int) and isinstance(node.pop2, int))

    """def test_simulate(self):
    populationList = [pg.PopNode(1, 2), pg.PopNode(3, 4), pg.PopNode(5, 6), pg.PopNode(7, 8), pg.PopNode(9, 10),
                      pg.PopNode(11, 12), pg.PopNode(13, 14), pg.PopNode(15, 16), pg.PopNode(17, 18), pg.PopNode(19, 20)]

    g1 = populate(nx.petersen_graph(), populationList)
    display(g1)
    g2 = simulate(g1, 1, 0.5)
    display(g2)
    self.assertTrue(nx.is_isomorphic(g1, g2))
    print(compare(g1, g2))
    """


if __name__ == '__main__':
    unittest.main()
