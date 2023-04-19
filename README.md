# PopulationX

## Usage

### Creating a PopGraph

A PopGraph is like a nx.Graph, except that it has several other features for handling PopNode objects. 
When instantiating a PopGraph you can pass in any nx.Graph. The PopGraph will have the same structure
as the passed nx.Graph. For example:

```py
import PopGraph as px
import networkx as nx
G = px.PopGraph(nx.petersen_graph())
```
This will create "G", a PopGraph with the same structure as a peterson graph. The parameter can be omitted,
in which case it will just be an empty graph.

#### Display

Any graph where every node is a PopNode can be displayed using the display() method. This will use matplotlib
to display the graph with each node visually represented as a tuple of population values.

#### Autopopulate

The peterson PopGraph created earlier does not yet hold any populations. To add populations to the graph we 
can use the populate() and auto_populate() methods.

Using the auto_populate() method, we can choose to pass in a lower bound and/or an upper bound. Lower bound
will default to 0 and upper bound will default to 99 if no parameter is passed. It will then return a graph
where each node is a PopNode with each population value being randomized between the lower and upper bounds.
```py
import PopGraph as px
import networkx as nx
G = px.PopGraph(nx.petersen_graph())
G = G.auto_populate(20, 30)
```

#### Populate

Using the populate() method, we pass in a list of PopNode objects equal to the size of
the graph. The nx.peterson_graph() defaults to ten nodes, so we will need a list of ten PopNodes as such:
```py
import PopGraph as px
import networkx as nx
G = px.PopGraph(nx.petersen_graph())

PopList = [px.PopNode(12, 32), px.PopNode(74, 21), px.PopNode(58, 23), px.PopNode(93, 10), px.PopNode(50, 84),
           px.PopNode(93, 79), px.PopNode(82, 10), px.PopNode(73, 9), px.PopNode(0, 21), px.PopNode(87, 5)]

G = G.populate(PopList)
```

#### Adding Single PopNode

Creating a new node can be done using add_node() inherited from nx.Graph, or add_pop(). Example:
```py
import PopGraph as px
import networkx as nx
G = px.PopGraph()
G.add_node(px.PopNode(1, 2)) #Creates PopNode object and adds it to the graph
G.add_pop(3, 4) #Also creates PopNode object but wrapped in method
```

#### Adding Single Edge

To create a single edge, we use the same method as NetworkX, add_edge(). We can access nodes using the find() method.
This method finds the first node with population values that match the passed parameters.
find() might not return the intended value if there are nodes with equal population values. A more secure method is to
use actual references.

```py
import PopGraph as px
import networkx as nx
G = px.PopGraph()

G.add_pop(1, 2)
G.add_pop(3, 4)

G.add_edge(G.find((1, 2)), G.find((3, 4)))
```

#### Adding Multiple PopNodes

The add_pops_from() method adds a list of PopNodes passed as an array of tuples.
```py
import PopGraph as px
import networkx as nx
G = px.PopGraph()
G.add_pops_from(
            [(44, 13), (36, 46), (39, 25), (0, 34), (65, 93), 
             (82, 68), (68, 92), (52, 77), (67, 25), (88, 19)]
        )
```

#### Adding Multiple Edges

The add_pop_edges_from() method takes in a list in a very specific format. The list comprises tuples.
Each tuple in the list is itself comprised of tuples, where each tuple represents a PopNode.
The first node in each tuple is the one to be connected to each other node. For example if we want to connect the
node (0, 3) to the nodes (2, 4), (3, 5), and (7, 6) we would denote this as ((0, 3), (2, 4), (3, 5), (7, 6)).
We then pass this as a list to add_pop_edges_from().
```py
import PopGraph as px
import networkx as nx
G = px.PopGraph()
G.add_pops_from([(0, 3), (2, 4), (3, 5), (7, 6)])
G.add_pop_edges_from([((0, 3), (2, 4), (3, 5), (7, 6))])
```

The add_pop_edges_from() method will not apply self loops opr double edges. 

We can do operations to more than one node by including more tuples. Here is a more complex example:

```py
import PopGraph as px

G = px.PopGraph()
G.add_pops_from(
    [(44, 13), (36, 46), (39, 25), (0, 34), (65, 93), 
     (82, 68), (68, 92), (52, 77), (67, 25), (88, 19)]
)

edgeArray = [
    #nodes to connect to (44, 13):
    ((44, 13), (36, 46), (68, 92), (88, 19)), ((36, 46), (44, 13), (65, 93), (39, 25)),
    #nodes to connect to (39, 25):
    ((39, 25), (36, 46), (67, 25), (0, 34)), ((0, 34), (39, 25), (68, 92), (52, 77)),
    #nodes to connect to (65, 93):
    ((65, 93), (82, 68), (52, 77), (36, 46)), ((82, 68), (67, 25), (68, 92), (65, 93)),
    #nodes to connect to (68, 92):
    ((68, 92), (82, 68), (44, 13), (0, 34)), ((52, 77), (88, 19), (65, 93), (0, 34)),
    #nodes to connect to (67, 25):
    ((67, 25), (82, 68), (88, 19), (39, 25)), ((88, 19), (44, 13), (52, 77), (67, 25))
]

G.add_pop_edges_from(edgeArray)
G.display()
```

### Simulating Population Change

We can simulate changes in the population using the simulate() method. The method takes in the number of steps to run,
and the weight (0 to 1) for a population to migrate. Both parameters default to 1. Note that even with a weight of 1,
which guarantees that a population will migrate when a node is visited, doesn't guarantee that populations won't
migrate back. So some nodes may have the same population values even if migration is guaranteed.

We can do a simple simulation that displays the graph before and after as follows:

```py
import PopGraph as px
import networkx as nx
G = px.PopGraph(nx.petersen_graph())
G = G.auto_populate()
G.display()
G.simulate(3, 0.5)
G.display()
```

This will create a peterson graph with pop values between 0 and 99. It will then run 3 simulation steps on the graph,
with there being a 50% chance of population migration whenever a node is visited.
