# Write your test here
import pytest
from challenge02 import repeated_word

def test_repeated():
    expected='ASAC'
    actual=repeated_word('ASAC is a department at LTUC. ASAC teaches programming in LTUC')
    assert expected==actual
    
def test_repeated2():
    expected='empty string'
    actual=repeated_word('')
    assert expected==actual