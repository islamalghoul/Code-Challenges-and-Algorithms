# Write here the code challenge solution
class Graph:
    def __init__(self) :
        self.length=0
        self.adjacentlist={}
    def addNode(self,node):
        self.adjacentlist[node]=[]
        self.length+=1
    def addEdge(self,node1,node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)
    def BFS(self,s):
        if not self.adjacentlist.keys():
            return "empty graph"

        array=[]
        level={}
        visited={}
        parent={}
        queue=[]
        
        for i in self.adjacentlist.keys():
            visited[i]=False
            parent[i]=None
            level[i]=-1
        visited[s]=True
        level[s]=0
        queue.append(s)
        while queue:
            u=queue.pop(0)
            array.append(u)
            for i in self.adjacentlist[u]:
                if not visited[i]:
                    visited[i]=True
                    parent[i]=u
                    level[i]=level[u]+1
                    queue.append(i)
        return array

# graph1=Graph()
# arr=['A','B','C','E','D','F','G','H','I','K']
# for i in arr:
#     graph1.addNode(i)

# graph1.addEdge('A','C')
# graph1.addEdge('A','E')
# graph1.addEdge('A','B')
# graph1.addEdge('E','G')
# graph1.addEdge('E','F')
# graph1.addEdge('E','D')
# graph1.addEdge('B','D')
# graph1.addEdge('C','F')
# graph1.addEdge('F','I')
# graph1.addEdge('F','H')
# graph1.addEdge('H','G')
# graph1.addEdge('H','K')
# graph1.addEdge('I','K')
# print(graph1.BFS('A'))








