# Programmed by: Rebekah Joy E. Sevial
# Test Driver Program

# Import the TV class of TV file
from TV import TV
# Define function for testing the two TV's
def TestTV():
    tv1 = TV()
    tv2 = TV()
# Assigning the values of each attributes of TV1 and TV2
    # TV1
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)
    # TV2
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)
# Print the TV1's and TV2's channel and volume
    print("tv1's channel is", tv1.setChannel, "and the volume level is", tv1.setVolume)
    print("tv2's channel is", tv2.setChannel, "and the volume level is", tv2.setVolume)

# Call the main function
TestTV()
