import networkx as nx
import random
import matplotlib.pyplot as plt


# Stores two populations (each population stores an integer)
class PopNode:
    def __init__(self, pop1, pop2):
        self.pop1 = pop1
        self.pop2 = pop2


class PopGraph(nx.Graph):

    # overrides the __init__ method from nx.Graph
    # if a graph is passed for G, then the nodes and edges of G will be added to self
    def __init__(self, G=None):
        super().__init__()
        if G is not None:
            self.add_nodes_from(G.nodes())
            self.add_edges_from(G.edges())

    # simple function to cleanly add new population objects
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

    # for each node, there is a chance of the population migrating
    def simulate(self, ticks, weight):
        for i in range(ticks):
            for node in self:
                for neighbor in iter(self[node]):
                    if random.random() <= weight:
                        neighbor.pop1 += 1
                        node.pop1 -= 1
                    if random.random() <= weight:
                        neighbor.pop2 += 1
                        node.pop2 -= 1
        return self

    # Displays a graph of PopNodes graphically, with each PopNode shown as a tuple
    def display(self):
        # make a list with a tuple for each node in g1
        tupleList = []
        for i in self.nodes():
            tupleList.append((i.pop1, i.pop2))

        # draw a graph with the PopNodes replaced with tuples
        mapping = dict(zip(self.nodes, tupleList))
        g2 = nx.relabel_nodes(self, mapping)
        nx.draw(g2, with_labels=True, font_weight='bold')
        plt.show()
