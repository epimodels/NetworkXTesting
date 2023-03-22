import networkx as nx
import random
import matplotlib.pyplot as plt


class PopNode:
    def __init__(self, pop1, pop2):
        self.pop1 = pop1
        self.pop2 = pop2


class PopGraph(nx.Graph):
    # def __init__(self):
    #    super().__init__()

    def add_pop(self, pop1, pop2):
        self.add_node(PopNode(pop1, pop2))

    # Returns a graph from a graph of empty nodes, and a list of PopNodes
    # Uses relabel_nodes function:
    def populate(self, popList):
        nodeList = self.nodes  # gets a list of the nodes of the graph to be written over
        mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
        newGraph = nx.relabel_nodes(self, mapping, True)  # copies the population objects to the original graph
        return newGraph

    # Returns a graph from a graph of empty nodes
    def auto_populate(self):
        # generate list of popNodes
        popList = []
        for i in self:
            popNode = PopNode(random.randrange(0, 99), random.randrange(0, 99))
            popList.append(popNode)

        nodeList = self.nodes  # gets a list of the node of the graph to be written over
        mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
        newGraph = nx.relabel_nodes(self, mapping, True)  # copies the population objects to the original graph
        return newGraph
