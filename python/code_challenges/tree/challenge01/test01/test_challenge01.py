# # Write your test here
import pytest
from code_challenges.tree.challenge01.tree01.challenge01 import Tree
def test_tree():  
    tree1=Tree()
    tree1.root=tree1.tree_construct_BT([1,2,4,8,9,10,11,5,3,6,7],[8,4,10,9,11,2,5,1,6,3,7])
    expected=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    actual=tree1.BFS()
    assert expected==actual

