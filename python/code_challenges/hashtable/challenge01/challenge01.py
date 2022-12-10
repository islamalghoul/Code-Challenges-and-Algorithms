# Write here the code challenge solution
class Node:
    def __init__(self,value):
       self.right=None
       self.left=None
       self.value=value



class Tree:
    def  __init__(self):
        self.root=None
        self.queue=[]
        self.root=None
    def insert(self,value):
        """
        this function for insert the nodes to make binary search tree
        """
        node= Node(value)
        if self.root==None:
            self.root=node
            return self.root
        current=self.root
        while True:
            if current.value>node.value:
                if current.left==None:
                  
                    current.left=node
                    return self.root
                current=current.left
            else:
                if current.right==None:
                    current.right=node
                 
                    return self.root
                current=current.right
    def findTarget(self, root, k) :
        
        obj={}
        current=root
        
        queue=[root]
        while queue:
            current=queue.pop(0)
            a=k-current.value
            if current.value in obj:
                return True
            else:
                obj[a]=a
                
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False




