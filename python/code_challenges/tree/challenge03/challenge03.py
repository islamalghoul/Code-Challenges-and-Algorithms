# Write here the code challenge solution
class Node:
    def __init__(self,value):
       self.right=None
       self.left=None
       self.value=value



class Tree:
    def  __init__(self):
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
    def lookup(self,value):
        """
        this function for searching in the tree
        """
        if self.root==None:
            return "empty Tree"
        if value ==self.root.value:
            return self.root
        current= self.root
        while current!=None:
            if current.value>value:
                current=current.left
            elif current.value<value:
                current=current.right
            elif current.value==value:
                return current
        return "we dont have node matching the value"
    def pre_order(self,current,list=[]):
        """
        return list that have the values of the tree in preorder way
        """
        list.append(current.value)
        if current.left!=None:
            self.pre_order(current.left,list)
        if current.right!=None:
            self.pre_order(current.right,list)
        return list
    def sortedArrayToBST(self, nums):
        """
        this function is taking an array and return  root of the tree
        
        """
        if not nums: return None

        # getting the mid
        mid = len(nums)//2
        node = Node(nums[mid])

        # left node is given the responsibility till mid, 
        # but not including mid
        node.left = self.sortedArrayToBST(nums[:mid])
        # right node is given the responsibility from mid+1 
        # till the end
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
        
