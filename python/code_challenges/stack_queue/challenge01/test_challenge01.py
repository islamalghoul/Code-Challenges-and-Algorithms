# Write your test herf
from challenge01 import Stack
import pytest


def test_delete():
    stack1  = Stack()
    stack1.push("W")
    stack1.push("E")
    stack1.push("L")
    stack1.push("C")
    stack1.push("O")
    stack1.push("M")
    stack1.push("E")
    stack2= Stack()
    str=""
    for i in range(7):
        stack2.push(stack1.pop())
    for i in range(7):
        str+=stack2.pop()

    print(str)
    """
     0 1 2 3 4 5
    [m,o,c,L,E,W]
    """
    
    expected="WELCOME"
    actual=str
    assert expected==actual



