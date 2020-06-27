from gpiozero import MCP3008
import smbus2

bus = smbus2.SMBus(1)
arduino_address = 0x04

def read():
    """returns 16 bytes in an array for, each byte corresponding to an analog input from arduino mega"""
    input = bus.read_i2c_block_data(arduino_address, 0, 16)
    return input


def to_sound_code(resistor_value):
    """temporary helper"""
    if round(resistor_value, 2) <= 5:
        print("resistor value less than 5")
        return "010"
    
    else:
        print("resistor value read incorrectly. Value not between 0,1")
        return "000"

class channels:
    """multidimensional array representing channels and steps"""

    def __init__(self, tempo,num_channels,num_steps):
        self.tempo = tempo #none of these are really implemented yet
        self.num_channels = num_channels
        self.num_steps = num_steps
        self.audio_file_struct = [["000" for i in range(0,num_steps)] for j in range(0,num_channels)]
        self.steps_resistance_values = []#holds current resistor values

    def init_analog_inputs(self):
        """setup the channel resistor reads for each step in a 
        SINGLE channel(at least to start)"""
        for i in range(0, self.num_steps * self.num_channels):#will need change when MC3008 values no longer linear
            self.steps_resistance_values.append(MCP3008(i))#[MCP3008[0],MCP3008[1], etc.]

    def scan_tracks(self):
        """Fill the step-sequencer array depending on the
        the values yielded by node resistor inputs"""
        self.steps_resistance_values = read()#i hope this works

        for j in range(0, self.num_channels):
            print("entering j loop")
            for i in range(0, self.num_steps):#assigning sound_codes based on resistance value in the steps
                self.audio_file_struct[j][i] = to_sound_code(self.steps_resistance_values[i + (4*j)])#only doing this in first channel(for now!!)
                #print(round(self.steps_resistance_values[i + (4*j)].value, 2))

    def print_audio_file_struct(self):
        for i in range(0, self.num_channels):
            print(self.audio_file_struct[i])

    def set_audio_num(self, x, y, val):
        self.audio_file_struct[x][y] = val

    def get_audio_num(self, x, y):
        """simple getter method"""
        return self.audio_file_struct[x][y]
            


