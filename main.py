import networkx as nx
import matplotlib.pyplot as plt


# Function that takes a graph of empty nodes, and returns a populated graph.
# Uses relabel_nodes function:
def populate(graph, popList):
    nodeList = sorted(graph)  # gets a list of the node of the graph to be written over
    mapping = dict(zip(nodeList, popList))  # creates a dictionary of empty nodes and population objects
    newGraph = nx.relabel_nodes(graph, mapping, True)  # copies the population objects to the original graph
    return newGraph


# Stores two populations (each population stores an integer)
class PopNode:
    def __init__(self, pop1, pop2):
        self.pop1 = pop1
        self.pop2 = pop2


if __name__ == '__main__':

    # create empty graph
    fstG = nx.petersen_graph()

    # create list of PopNode objects
    lst = []
    for i in range(10):
        lst.append(PopNode(10, 15))

    # create new graph, with list of objects over shape of old graph
    sndG = populate(fstG, lst)

    nx.draw(sndG, with_labels=True, font_weight='bold')
    plt.show()

