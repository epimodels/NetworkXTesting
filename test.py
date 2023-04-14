import unittest
import networkx as nx
import networkx.algorithms.isomorphism as iso

from main import *


def setUp(self):
    pass


# finds the greatest difference in population between graphs
def difference(g1, g2):
    lst1 = list(g1.nodes)
    lst2 = list(g2.nodes)

    max_dif = 0

    for i in range(len(lst1)):
        dif1 = abs(lst1[i].pop1 - lst2[i].pop1)
        dif2 = abs(lst1[i].pop2 - lst2[i].pop2)
        if dif1 > max_dif:
            max_dif = dif1
        if dif2 > max_dif:
            max_dif = dif2

    return max_dif


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

    def test_example_graph(self):
        exGraph = pg.PopGraph()
        exGraph.add_pops_from(
            [(44, 13), (36, 46), (39, 25), (0, 34), (65, 93), (82, 68), (68, 92), (52, 77), (67, 25), (88, 19)]
        )

        edgeArray = [((44, 13), (36, 46), (68, 92), (88, 19)), ((36, 46), (44, 13), (65, 93), (39, 25)),
                     ((39, 25), (36, 46), (67, 25), (0, 34)), ((0, 34), (39, 25), (68, 92), (52, 77)),
                     ((65, 93), (82, 68), (52, 77), (36, 46)), ((82, 68), (67, 25), (68, 92), (65, 93)),
                     ((68, 92), (82, 68), (44, 13), (0, 34)), ((52, 77), (88, 19), (65, 93), (0, 34)),
                     ((67, 25), (82, 68), (88, 19), (39, 25)), ((88, 19), (44, 13), (52, 77), (67, 25))]

        exGraph.add_pop_edges_from(edgeArray)
        exGraph.display()

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
