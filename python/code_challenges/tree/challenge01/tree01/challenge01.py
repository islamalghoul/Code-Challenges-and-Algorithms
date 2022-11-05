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
        list.append(current.value)
        if current.left!=None:
            self.pre_order(current.left,list)
        if current.right!=None:
            self.pre_order(current.right,list)
        return list
    def get_left_right(self,number,array):
        left_arr=[]
        right_arr=[]
        for i in range(len(array)):
          if array[i]==number:
             left_arr=array[0:i]
             right_arr=array[i+1:]
             break
        return [left_arr,right_arr]
    # def tree_construct_BT(self,preorder,inorder):
    #     self.root=None
    #     left_arr=[]
    #     right_arr=[]
    #     node=Node(preorder[0])
    #     self.root=node
    #     current=self.root
    #     left_arr=self.get_left_right(preorder[0],inorder)[0]
    #     right_arr=self.get_left_right(preorder[0],inorder)[1]
    #     i=1
    #     while True:
    #         node=Node(preorder[i])
    #         current.left=node
    #         current=current.left
    #         if len(left_arr)>1:
    #             left_arr=self.get_left_right(preorder[i],left_arr)[0]
    #         else:
    #             break
    #         i+=1
    def tree_construct_BT(self, preorder, inorder):
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = Node(inorder[INDEX])
            root.left = self.tree_construct_BT(preorder, inorder[:INDEX])
            root.right = self.tree_construct_BT(preorder, inorder[INDEX+1:])
            
            return root
    def BFS(self):
        tree=[]
        if not self.root:
            return 'Empty tree'
        node= self.root
        self.queue.append(node)
        while self.queue:
            node= self.queue.pop(0)
            tree.append(node.value)
            if node.left != None:
                self.queue.append(node.left)
            if node.right != None:
                self.queue.append(node.right)
        return tree
   
    

            
            

# tree1=Tree()
# tree1.root=tree1.tree_construct_BT([1,2,4,8,9,10,11,5,3,6,7],[8,4,10,9,11,2,5,1,6,3,7])
# print(tree1.BFS())






