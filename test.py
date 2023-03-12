import unittest
import networkx as nx
import networkx.algorithms.isomorphism as iso

from main import *


class PopGraphTest(unittest.TestCase):

    def test_simulate(self):
        populationList = [PopNode(1, 2), PopNode(3, 4), PopNode(5, 6), PopNode(7, 8), PopNode(9, 10),
                          PopNode(11, 12), PopNode(13, 14), PopNode(15, 16), PopNode(17, 18), PopNode(19, 20)]

        g1 = populate(nx.petersen_graph(), populationList)
        g2 = simulate(g1, 1, 1)
        self.assertTrue(nx.is_isomorphic(g1, g2))
