import networkx as nx
import time
import random
import matplotlib.pyplot as plt


# Returns a graph from a graph of empty nodes, and a list of PopNodes
# Uses relabel_nodes function:
def populate(g, popList):
    nodeList = g.nodes  # gets a list of the node of the graph to be written over
    mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
    newGraph = nx.relabel_nodes(g, mapping, True)  # copies the population objects to the original graph
    return newGraph


# Returns a graph from a graph of empty nodes
def auto_populate(g):

    # generate list of popNodes
    popList = []
    for i in g:
        popNode = PopNode(random.randrange(0, 99), random.randrange(0, 99))
        popList.append(popNode)

    nodeList = g.nodes  # gets a list of the node of the graph to be written over
    mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
    newGraph = nx.relabel_nodes(g, mapping, True)  # copies the population objects to the original graph
    return newGraph


def simulate(graph, ticks, spt):
    success = 0
    for i in range(ticks):
        if random.random() <= 0.5:
            success += 1
    print(success)


# Function used to display a graph of PopNodes graphically, with each PopNode shown as a tuple
def display(g1):

    tupleList = []
    for i in g1.nodes():
        tupleList.append((i.pop1, i.pop2))

    mapping = dict(zip(g1.nodes, tupleList))
    g2 = nx.relabel_nodes(g1, mapping)
    nx.draw(g2, with_labels=True, font_weight='bold')
    plt.show()


# for each node, there is a chance of the population migrating
def update(graph, probability):
    pass


# Stores two populations (each population stores an integer)
class PopNode:
    def __init__(self, pop1, pop2):
        self.pop1 = pop1
        self.pop2 = pop2


if __name__ == '__main__':
    g = auto_populate(nx.petersen_graph())
    display(g)
