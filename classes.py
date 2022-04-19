class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume


    def __init__(self) -> None:
        """
        Method to constuct a TV object.
        """
        self.__chan = self.MIN_CHANNEL
        self.__vol = self.MIN_VOLUME
        self.__ison = False

    def power(self) -> None:
        """
        Method to change the value of the variable that determines if the TV is on or off.
        """
        if(self.__ison == False):
            self.__ison = True
        else:
            self.__ison = False

    def channel_up(self)-> None:
        """
        Method to increase the value of the variable that represents the TV's channel by 1
        """
        if(self.__ison == True):
            if(self.__chan < self.MAX_CHANNEL):
                self.__chan += 1
            elif(self.__chan == self.MAX_CHANNEL):
                self.__chan = self.MIN_CHANNEL


    def channel_down(self)-> None:
        """
        Method to decrease the value of the variable that represents the TV's channel by 1
        """
        if(self.__ison == True):
            if(self.__chan > self.MIN_CHANNEL):
                self.__chan -= 1
            elif(self.__chan == self.MIN_CHANNEL):
                self.__chan = self.MAX_CHANNEL

    def volume_up(self)-> None:
        """
        Method to increase the value of the variable that represents the TV's volume by 1
        """
        if(self.__ison == True):
            if(self.__vol < self.MAX_VOLUME):
                self.__vol += 1

    def volume_down(self)-> None:
        """
        Method to decrease the value of the variable that represents the TV's volume by 1
        """
        if(self.__ison == True):
            if(self.__vol > self.MIN_VOLUME):
                self.__vol -= 1

    def getVol(self):
        """
        Method to get the current volume
        """
        return self.__vol

    def getChan(self):
        """
        Method to get the current channel
        """
        return self.__chan

    def getIson(self):
        """
        Method to get the current ison status
        """
        return self.__ison

    def __str__(self) -> str:
        """
        Method to print out the TV object and display its atributes
        """
        return(f'TV status: is on = {self.__ison}, Channel = {self.__chan}, Volume = {self.__vol}')
