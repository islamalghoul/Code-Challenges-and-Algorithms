# Write here the code challenge solution

class Node:
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        """
        this function for pushing in the stack
        """
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """
        this function for poping in the stack
        """
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        """
        this function for getting the last value pushed in the stack
        """
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        """
        this function makes the size empty
        """
        return self.size == 0

    def get_size(self):
        """
        this function return the size of the stack
        """
        return self.size

# stack1  = Stack()
# stack1.push("H")
# stack1.push("E")
# stack1.push("L")
# stack1.push("L")
# stack1.push("O")

# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.peek())
