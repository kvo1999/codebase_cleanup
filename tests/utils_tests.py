# this is the test/utils_test.py file 

#def test_answer():
    #assert inc(3) == 5

from app.utils import to_usd

def test_to_usd():
    #it rounds two decimal places and has $ sign, 
    #and if large numbers, should use thousands seperator
    assert to_usd(0.4555555) == "$0.46"
    assert to_usd(123456789.98) == "$123,456,789.98"


