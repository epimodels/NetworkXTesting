import unittest
import networkx as nx
import networkx.algorithms.isomorphism as iso
import PopGraph as pg
from main import *


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


class PopGraphTest(unittest.TestCase):



    def test_simulate(self):
        populationList = [pg.PopNode(1, 2), pg.PopNode(3, 4), pg.PopNode(5, 6), pg.PopNode(7, 8), pg.PopNode(9, 10),
                          pg.PopNode(11, 12), pg.PopNode(13, 14), pg.PopNode(15, 16), pg.PopNode(17, 18), pg.PopNode(19, 20)]

        g1 = populate(nx.petersen_graph(), populationList)
        display(g1)
        g2 = simulate(g1, 1, 0.5)
        display(g2)
        self.assertTrue(nx.is_isomorphic(g1, g2))
        print(compare(g1, g2))
