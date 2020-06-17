'''
Homework 6 - Problem 1:
Create a Graph class and test
See HW6 PDF for specifications
'''

# Checked homework with Matt Pozsgai

from collections import defaultdict, deque

class Graph():
    """The Graph class stores nodes and edges of an undirected graph in a dictionary, where each key is a node and the values of keys are the adjacent nodes to the key node."""
    def __init__(self, edges=None):
        self.edges = edges
        self.nodes_edges = defaultdict(set)
        try:
            for e in self.edges:
                self.nodes_edges[e[0]].add(e[1])
                self.nodes_edges[e[1]].add(e[0])
        except TypeError: # allows us to intialize if no edges given
            pass
        
    def add_node(self, u):
        """The add_node method accepts a single argument of an immutable type representing a node to the instantiated, undirected graph if the node is not already present."""
        if u not in self.nodes_edges:
            self.nodes_edges[u] = set()

    def add_edge(self, u, v):
        """The add_edge method accepts two arguments representing two nodes of immutable type connected via an edge to the instantiated, undirected graph if the edge is not already present."""
        self.nodes_edges[u].add(v) 
        self.nodes_edges[v].add(u)
                
    def __iter__(self):
        self.n = 0
        return self 

    def __next__(self):
        temp = [node for node in self.nodes_edges]
        if self.n < len(temp):
            result = temp[self.n]
            self.n += 1
            return result
        raise StopIteration

    def __getitem__(self, u):
        if u in self.nodes_edges.keys():
            return self.nodes_edges[u]
        else:
            raise IndexError

    def __contains__(self, u):
        return True if u in self.nodes_edges.keys() else False

    def bfs(self, u):
        """The bfs method produces an iterable of 2-tuples that are of the form (node, distance) where the node is a node in the graph and the distance is determined with the breadth-first search. 
        
        The bfs method takes one argument that represents the node that you want to find the distance from for all other nodes in the graph.
        The breadth-first search starts at that source node, marks its distance as 0 and adds it as (node, 0) to the return list, and then moves to the next level (which are includes all adjacent nodes to the source node.
        The nodes in this next level are added to the queue and then traversed, while the source node is removed from the queue.
        Traversing, in this implementation, means that the node is removed from the queue, the (node, level) is added to the queue, and its adjacent nodes are added to a temporary queue as long as they have not previously been traversed.
        Once all nodes in a level are traversed, the temporary queue becomes the actual queue and the traversing process continues with this new level.
        Traversing continues until there are no nodes left in the queue.
        """
        if u in self: # we only want to do this if u is in the graph -- if it is not, then return a message that says this node is not in the graph -- this will return None distance in distance() method
            nd = [(u, 0)]
            queue = deque([u])
            temp = [] # we want to explore all nodes in one level before moving on to the next, so save next level nodes in a temp file to be added to the queue after all nodes in a given level have been marked and popped. 
            dist = 1
            while queue:
                v = queue.popleft()
                for neighbor in self.nodes_edges[v]:
                    if neighbor not in [x[0] for x in nd]:
                        nd.append((neighbor, dist))
                        temp.append(neighbor)
                if len(queue) == 0:
                    queue.extend(temp)
                    temp = []
                    dist += 1
            # logic for unconnected nodes - infinity distance
            for node in self.nodes_edges:
                if node not in [x[0] for x in nd]:
                    nd.append((node, float('inf')))
        else:
            nd = "{} not in graph - no distance to any other node".format(u)
        return nd
    
    def distance(self, u, v):
        """The distance method takes two arguments that are nodes and returns the length of the shortest path between them utilizing the bfs method.

        run Graph.bfs__doc__() to see how distance is calculated using bfs.
        """
        for i in self.bfs(u):
            if i[0] == v:
                return i[1]

    def __repr__(self):
        return "{}".format(self.nodes_edges)

'''
# tests for my own sanity
if __name__ == "__main__":
    edges= [(1,2), (1,5), (2,3), (2,5), (3,4), (4,5), (4,6)]
    g = Graph(edges)
    for u,v in edges:
        g.add_edge(u,v)

    print("index tests")
    print(g[5])
    print(g[6])
    #print(g[99]) - raises appropriate index error
    
    print("\nin tests")
    print(4 in g)
    print(20 in g)
    print("foo" in g)
    
    print("\niter/next tests")
    for node in g:
        print(node)
    print(g)
    for node in g:
        print(node)
    print(g)
    
    print("\nadding node and edge test")
    g.add_node(7)
    g.add_edge(7,6)
    g.add_edge(("foo",6),"hello")
    g.add_edge(("foo",6),7)
    g.add_edge(("foo",6),6)
    print(g)
    
    print("\nbfs tests")
    for node,distance in g.bfs(1):
        print("{}, d={}".format(node, distance))
    print("\n")
    for node,distance in g.bfs(3):
        print("{}, d={}".format(node, distance))
    
    print("\ndistance tests")
    print(g.distance(2,4))
    print(g.distance(6,5))
    
    print("\nunconnected graph tests")
    g.add_node(20) 
    for node,distance in g.bfs(20):
        print("{}, d={}".format(node, distance))
    print("\n")
    for node,distance in g.bfs(1):
        print("{}, d={}".format(node, distance))
    print("\n")
    print(g.distance(1,20))
    print(g.distance(20,3))
    g.add_edge(20, 17)
    print("\n")
    for node,distance in g.bfs(20):
        print("{}, d={}".format(node, distance))
    print("\n")
    for node,distance in g.bfs(17):
        print("{}, d={}".format(node, distance))
    print("\n")
    for node,distance in g.bfs(1):
        print("{}, d={}".format(node, distance))
    print("\n")
    print(g.distance(3,17))
    print(g.distance(20,3))
    print(g.distance(20,17))

    print("\ntest bfs and distance when node arguments not in the graph")
    print(g.bfs(89))
    print(g.distance(89,1))
    print(g.distance(89,1))
    print(g.distance(89,76))
    
    print("\ntest docstrings")
    print(Graph.__doc__)
    print(Graph.add_node.__doc__)
    print(Graph.add_edge.__doc__)
    print(Graph.bfs.__doc__)
    print(Graph.distance.__doc__)

    print("\nprint graph")
    print(g)
'''

import unittest
class TestGraphMethods(unittest.TestCase):

    def setUp(self):
        edges= [(1,2), (1,5), (2,3), (2,5), (3,4), (4,5), (4,6)]
        self.g = Graph(edges)

    def tearDown(self):
        del self.g

    # note: for add_node I test both that I can add a node and that adding an already present node will not change my data structure
    def test_add_nodes(self):
        self.g.add_node(7)
        self.assertIn(7, self.g)
        
        self.g.add_node(6)
        self.assertListEqual([1,2,3,4,5,6,7], [x for x in self.g.nodes_edges])

    # note: for add_edge I test both that I can add an edge and that adding an already present edge will not change my data structure
    def test_add_edge(self):
        self.g.add_edge(7, 6)
        self.assertTrue(6 in self.g[7])
        self.assertTrue(7 in self.g[6])
        self.g.add_edge(20, 14)
        self.assertTrue(20 in self.g[14])
        self.assertTrue(14 in self.g[20])
        
        self.g.add_edge(2, 5)
        self.assertSetEqual({1,3,5}, self.g[2])
        self.assertSetEqual({1,2,4}, self.g[5])
        self.assertSetEqual({1,5,3}, self.g[2])
        
    def test_in(self):
        self.assertTrue(1 in self.g)
        self.assertTrue(77 not in self.g)
        self.assertTrue(7 not in self.g)

    # note: I am expecting a failure when tring to index 99 because that will raise an index error
    @unittest.expectedFailure
    def test_indexed(self):
        self.assertTrue(self.g[99] == set())
        
    def test_indexed2(self):
        self.assertSetEqual(self.g[4], {3, 5, 6})
        self.assertSetEqual(self.g[4], {5, 6, 3})
        self.assertFalse(self.g[1] == set())
        
    # note: this bfs test tests whether the bfs does not repeat nodes and that I get the output I am expecting
    def test_bfs(self):
        self.assertTrue(len(self.g.bfs(3)) == len(self.g.nodes_edges))
        
        self.g.add_node(20)
        self.assertListEqual(self.g.bfs(3), [(3,0), (2,1), (4,1), (1,2), (5,2), (6,2), (20, float('inf'))])
        self.assertListEqual(self.g.bfs(20), [(20,0), (1, float('inf')), (2, float('inf')), (3, float('inf')), (4, float('inf')), (5, float('inf')), (6, float('inf'))])
        self.assertEqual(self.g.bfs(89), "89 not in graph - no distance to any other node")
        
    def test_distance(self):
        self.assertEqual(self.g.distance(2, 4), 2)
        self.assertEqual(self.g.distance(1, 6), 3)
        self.g.add_node(20)
        self.assertEqual(self.g.distance(20, 1), float('inf'))
        self.g.add_node(17)
        self.assertEqual(self.g.distance(20, 17), float('inf'))
        self.assertEqual(self.g.distance(17, 20), float('inf'))
        self.g.add_edge(17,20)
        self.assertEqual(self.g.distance(20, 17), 1)
        self.assertEqual(self.g.distance(20, 1), float('inf'))
        self.assertEqual(self.g.distance(20, 1), float('inf'))
        self.assertEqual(self.g.distance(4, 17), float('inf'))
        self.assertEqual(self.g.distance(4, 89), None)
        self.assertEqual(self.g.distance(89, 17), None)
        self.assertEqual(self.g.distance(89, 104), None)

    
