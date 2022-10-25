# Write your test here
import pytest
from code_challenges.linkedlist.challenge03.challenge03 import Linked_list,removeNthFromEnd

def test_removeNth():
    first_node=Linked_list()
    first_node.append("12")
    first_node.append("13")
    first_node.append("14")
    first_node.append("15")
    first_node.append("16")
    node=first_node.get_node("12")
    removeNthFromEnd(node,4)
    array=first_node.transfer_to_list()
    expected=['12', '14', '15','16']
    actual=array
    assert expected==actual
