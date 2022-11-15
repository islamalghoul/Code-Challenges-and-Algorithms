# Write your test here
import pytest
from challenge03 import Tree
def test_sortedArrayToBST():  
    
    tree=Tree()
    tree.root=tree.sortedArrayToBST([-10,-3,0,5,9])
    array=tree.BFS()

    expected=[0,-3,9,-10,5]
    actual=array
    assert expected==actual