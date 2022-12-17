# Write your test here
import pytest
from challenge01 import Graph

def test_BFS():
    graph1=Graph()
    arr=['A','B','C','E','D','F','G','H','I','K']
    for i in arr:
        graph1.addNode(i)

    graph1.addEdge('A','C')
    graph1.addEdge('A','E')
    graph1.addEdge('A','B')
    graph1.addEdge('E','G')
    graph1.addEdge('E','F')
    graph1.addEdge('E','D')
    graph1.addEdge('B','D')
    graph1.addEdge('C','F')
    graph1.addEdge('F','I')
    graph1.addEdge('F','H')
    graph1.addEdge('H','G')
    graph1.addEdge('H','K')
    graph1.addEdge('I','K')
    expected=['A', 'C', 'E', 'B', 'F', 'G', 'D', 'I', 'H', 'K']
    actual= graph1.BFS('A')
    assert expected==actual
def test_BFS2():
        graph2=Graph()
        expected="empty graph"
        actual= graph2.BFS('A')
        assert expected==actual
