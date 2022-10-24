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
        self.counter+=1
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
 

   
            
def find_middle_node(head):
        """
        this function is getting the nodes after the middle
        """
        current=head
        counter=1
        nod=current
        array=[]
        while nod.next!=None:
            nod=nod.next
            counter+=1
        mid=counter//2
        i=0
        
        
        while i<mid:
           
            current=current.next
            i+=1
        while current!=None:
            array.append(current.value)
            current=current.next
        return array
                       


def delete_node(node):
        """
        this function for deleting a node 
        """
        node.value=node.next.value
        node.next=node.next.next



