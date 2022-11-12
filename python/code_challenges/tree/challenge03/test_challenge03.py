# Write your test here
import pytest
from challenge03 import Tree
def test_sortedArrayToBST():  
    
    tree=Tree()
    tree.root=tree.sortedArrayToBST([1,2,3,5,6,7])
    pre_order_list=tree.pre_order(tree.root)
    expected=[5,2,1,3,7,6]
    actual=pre_order_list
    assert expected==actual