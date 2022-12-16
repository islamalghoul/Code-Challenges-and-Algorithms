# Write your test here
import pytest
from challenge01 import Tree

def test_findTarget():
    tree1=Tree()
    list=[5,3,6,2,4,7]
    for i in list:  
        tree1.insert(i)
    expected=True
    actual=tree1.findTarget(tree1.root,9)
    assert expected==actual
def test_findTarget2():
    tree1=Tree()
    list=[1,3,5,7,1,2]
    for i in list:  
        tree1.insert(i)
    expected=True
    actual=tree1.findTarget(tree1.root,4)
    assert expected==actual