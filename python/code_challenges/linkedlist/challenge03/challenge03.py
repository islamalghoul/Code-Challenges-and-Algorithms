# Write here the code challenge solution
from contextlib import nullcontext


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
    def reverse(self):
        """
        []
        """
        prev=None
        next=self.head.next
        current=self.head
        while current !=None:
            current.next=prev
            prev=current
            current=next
            if next !=None:
                next=next.next
        self.head=prev

 

   
            
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

def get_indx(head,revers_indx):
    """
    this function for getting the node index
    """
    current=head
    count=0
    while current!=None:
        count+=1
        current=current.next
    idx=count-revers_indx
    return [idx,count]
def get_node(head,idx):
    """
    this function for getting the node 
    """
    current=head
    count=0
    while current!=None:
        if count==idx:
            return current
        current=current.next
        count+=1
    
def removeNthFromEnd(head, n):
        """
        this function  is taking the head of the node and the revers index and delete the node that have the same index return the linkedlist without that node 
        """
        length=get_indx(head,n)[1]
        idx= get_indx(head,n)[0]
        node_for_delete=get_node(head,idx)
        
        if length==1:
            return None
        idx2=get_indx(head,n+1)[0]
        previous_node=get_node(head,idx2)
        if node_for_delete.next!=None:
            delete_node(node_for_delete)

        else :
            previous_node.next=previous_node.next.next
        
        return head


        
    
        


# first_node=Linked_list()
# first_node.append("12")
# first_node.append("13")
# first_node.append("14")
# first_node.append("15")
# first_node.append("16")
# node=first_node.get_node("12")
# first_node.reverse()
# print(first_node.transfer_to_list())


