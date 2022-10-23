# Write here the code challenge solution
class Node :
    """
    this class for create node
    """
    def __init__(self,value):
        self.value=value
        self.next=None


class Linked_list:
   
    def __init__(self):
        self.head=None
        self. counter=0
        
    def append(self,value):
        """
        this function for appending new nodes 
        """
        new_node=Node(value)
        if self.counter==0:
            self.head=new_node
        # if Linked_list.counter==1:
        #     pass
            
        else: 
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new_node
        Linked_list.counter+=1
    def get_node(self,value):
        """
        this function for getting a nodes 
        """
        current=self.head
        while current.value!=value:
            current=current.next
        return current
    def transfer_to_list(self):
        """
        this function is appending node.value to an array
        """
        array=[]
        current=self.head
        while current.next!=None:
            array.append(current.value)
            current=current.next
        array.append(current.value)
        return array
    # def delete_node(self,node):
    #     """
    #     this function for deleting a node 
    #     """
    #     node.value=node.next.value
    #     node.next=node.next.next
    


        
def delete_node(node):
        """
        this function for deleting a node 
        """
        node.value=node.next.value
        node.next=node.next.next
# first_node=Linked_list()
# first_node.append("12")
# first_node.append("13")
# first_node.append("14")
# first_node.append("15")
# first_node.append("16")
# node=first_node.get_node("13")
# list_of_nodes_values=first_node.transfer_to_list()
# print(list_of_nodes_values)
# first_node.delete_node(node)
# print(first_node.transfer_to_list())


if __name__=="__main__":
    pass
