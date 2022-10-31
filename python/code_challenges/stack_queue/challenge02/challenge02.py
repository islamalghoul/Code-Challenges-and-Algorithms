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
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    def len(self):
        return self.size

def isValid(s):
    """
    :type s: str
    :rtype: bool
    this function checkes if it is a valid parentheses or not 
    """
    arr= Stack()
    valid=["()","[]","{}"]
    closing=")]}"
    opening="([{"
    if len(s)==0 or s[0] in closing or s[len(s)-1] in opening:
        return False
    for ch in s:
        if ch not in closing and ch not in opening :
            continue
        if ch in opening:
            arr.push(ch)
        else:
            if arr.len()==0:
                return False
            str=arr.pop()

            if str + ch in valid: 
                continue 
            else:
                return False
    if arr.len()!=0:
        return False
    return True
