# Programmed by: Rebekah Joy E. Sevial
# Creating Class named TV

# Creating the class named TV
class TV:
    # Define constructor of the TV
    def __init__(self, power_on=True, channel=1, volume=1):
        self.power_on = power_on
        self.channel = channel
        self.volume = volume
    # Define function to turn on the TV
    def turnOn(self):
        self.power_on = True
    # Define function to turn off the TV
    def turnOff(self):
        self.power_on = False
    # Define function to return the channel
    def getChannel(self):
        return self.channel
    # Define function to check if the channel is existing
    def setChannel(self, channel):
        if self.power_on and 1 <= channel <= 120:
            self.channel = channel
    # Define function to return the volume
    def getVolume(self):
        return self.volume
    # Define function to check if the volume is within the range
    def setVolume(self, volume):
        if self.power_on and 1 <= volume <= 7:
            self.volume = volume
# Define function that will you change the channel up
# Define function that will you chnage the channel down
# Define function that will you increase the volume
# Define function that will you decrease the volume 


