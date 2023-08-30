from lib.space import *
from datetime import date

def test_space_initialises():
    space = Space(1,'House_1', 'nice house', 150.00, date(2023,1,1), date(2023,10,1), 1)
    assert space.id == 1
    assert space.name == 'House_1'
    assert space.description == 'nice house'
    assert space.price == 150.00
    assert space.avail_from == date(2023,1,1)
    assert space.avail_to == date(2023,10,1)
    assert space.user_id == 1

def test_equal():
    space1 = Space(1,'House_1', 'nice house', 150.00, date(2023,1,1), date(2023,10,1), 1)
    space2 = Space(1,'House_1', 'nice house', 150.00, date(2023,1,1), date(2023,10,1), 1)
    assert space1 == space2