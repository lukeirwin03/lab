import classes

def setUp_method(self):
    self.tv1 = Television()

def tearDown_method(self):
    del self.tv1

def test__init__(self):
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'

def testPower(self):
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'
    self.tv1.power()
    assert self.tv1.__str__() == 'TV status: is on = True, Channel = 0, Volume = 0'

def testChanUp(self):
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'
    self.tv1.channel_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'

    self.tv1.power()
    self.tv1.channel_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 1, Volume = 0'
    self.tv1.channel_up()
    self.tv1.channel_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 3, Volume = 0'
    self.tv1.channel_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'

def testChanDown(self):
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'
    self.tv1.channel_down()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'

    self.tv1.power()
    self.tv1.channel_down()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 3, Volume = 0'
    self.tv1.channel_down()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 2, Volume = 0'

def testVolUp(self):
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'
    self.tv1.volume_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'

    self.tv1.power()
    self.tv1.volume_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 1'
    self.tv1.volume_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 2'
    self.tv1.volume_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 2'

def testVolDown(self):
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'
    self.tv1.volume_down()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'

    self.tv1.power()
    self.tv1.volume_down()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'
    self.tv1.volume_up()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 1'
    self.tv1.volume_down()
    assert self.tv1.__str__() == 'TV status: is on = False, Channel = 0, Volume = 0'
