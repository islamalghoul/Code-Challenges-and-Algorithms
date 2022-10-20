# Write your test here
import pytest
from challenge01 import Node,Linked_list

def test_delete():
    first_node=Linked_list()
    first_node.append("12")
    first_node.append("13")
    first_node.append("14")
    first_node.append("15")
    first_node.append("16")
    node=first_node.get_node("13")
    first_node.delete_node(node)
    expected=["12","14","15","16"]
    actual=first_node.transfer_to_list()
    assert expected==actual




    