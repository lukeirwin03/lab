from classes import *
from pytest import *

tv1 = Television()

def test_TV():
    tv1 = Television()
    print(tv1)
    assert tv1.getChan() == 0
    tv1.channel_down()
    assert tv.



if __name__ == '__main__':
    test_TV()