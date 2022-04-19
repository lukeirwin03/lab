from classes import *
from pytest import *

#tv1 = Television()

def test_TV():
    tv1 = Television()
    
    """
    Testing the ison methods in the Television class
    """
    assert tv1.getIson() == False
    tv1.power()
    assert tv1.getIson() == True

    """
    Testing the channel methods in the Television class
    """
    assert tv1.getChan() == 0
    tv1.channel_down()
    assert tv1.getChan() == 3
    tv1.channel_up()
    assert tv1.getChan() == 0
    tv1.channel_up()
    tv1.channel_up()
    assert tv1.getChan() == 2
    tv1.channel_up()
    tv1.channel_up()
    assert tv1.getChan() == 0
    

    """
    Testing the volume methods in the Television class
    """
    assert tv1.getVol() == 0
    tv1.volume_down()
    assert tv1.getVol() == 0
    tv1.volume_up()
    tv1.volume_up()
    assert tv1.getVol() == 2
    tv1.volume_up()
    assert tv1.getVol() == 2


if __name__ == '__main__':
    test_TV()