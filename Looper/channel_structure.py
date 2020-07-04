from gpiozero import MCP3008
import smbus2

#initializing i2c protocall
bus = smbus2.SMBus(1)
arduino_address = 0x04

def read():
    """returns 16 bytes in an array for, each byte corresponding to an analog input from arduino mega"""
    input = bus.read_i2c_block_data(arduino_address, 0, 16)
    return input


def to_sound_code(resistor_value):
    """temporary helper"""
    if resistor_value <= 5:
        print("empty position, resistor value < 5")
        return "000"
    
    else :
        return "010"
        print(resistor_value)

class channels:
    """multidimensional array representing channels and steps"""

    def __init__(self, tempo,num_channels,num_steps):
        self.tempo = tempo #none of these are really implemented yet
        self.num_channels = num_channels
        self.num_steps = num_steps
        self.audio_file_struct = [["000" for i in range(0,num_steps)] for j in range(0,num_channels)]
        self.steps_resistance_values = []#holds current resistor values
        

    def scan_tracks(self):
        """Fill the step-sequencer array depending on the
        the values yielded by node resistor inputs"""
        self.steps_resistance_values = read()#i hope this works

        for j in range(0, self.num_channels):
            print("entering j loop")
            for i in range(0, self.num_steps):#assigning sound_codes based on resistance value in the steps
                self.audio_file_struct[j][i] = to_sound_code(self.steps_resistance_values[i + (self.num_steps*j)])#only doing this in first channel(for now!!)
                #print(round(self.steps_resistance_values[i + (4*j)].value, 2))


    #don't think this is being used
    def print_audio_file_struct(self):
        for i in range(0, self.num_channels):
            print(self.audio_file_struct[i])

    def set_audio_num(self, x, y, val):
        self.audio_file_struct[x][y] = val

    def get_audio_num(self, x, y):
        """simple getter method"""
        return self.audio_file_struct[x][y]
            


