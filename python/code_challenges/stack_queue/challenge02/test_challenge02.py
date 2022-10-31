# Write your test here
from challenge02 import Stack,isValid
import pytest
def test_valid():  
    expected=True
    actual=isValid("(()){[()]}")
    assert expected==actual
