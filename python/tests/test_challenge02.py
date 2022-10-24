# Write your test here
import pytest
from code_challenges.linkedlist.challenge02.challenge02 import Linked_list,find_middle_node

def test_find_middle_node():
    first_node=Linked_list()
    first_node.append("12")
    first_node.append("13")
    first_node.append("14")
    first_node.append("15")
    first_node.append("16")
    first_node.append("17")
    node=first_node.get_node("12")
    middle=find_middle_node(node)
    expected=['15', '16', '17']
    actual=middle
    assert expected==actual
