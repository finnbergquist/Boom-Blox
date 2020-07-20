import smbus2


def to_sound_code(resistor_value):
    """temporary helper"""
    if resistor_value <= 5:
        return "000"
    
    else:
        print(resistor_value)
        return "200"
    """
    elif 5 < resistor_value <= 18 :#16barsharp
        return "800"
    elif 18 < resistor_value <= 30 :#chimes
        return "400"
    elif 30 < resistor_value <= 100 :#8bars
        return "200"
    elif 100 < resistor_value <= 150:
        return "210"#crash
    else:
        return "410"#4barspiano"""
    

class channels:
    """multidimensional array representing channels and steps"""

    def __init__(self, tempo,num_channels,num_steps, bus):
        self.tempo = tempo #none of these are really implemented yet
        self.num_channels = num_channels
        self.num_steps = num_steps
        self.audio_file_struct = [["000" for i in range(0,num_steps)] for j in range(0,num_channels)]
        self.steps_resistance_values = []#holds current resistor values
        self.bus = bus#i2c bus, initialized in driver
        self.arduino_address0 = 0x04

    def scan_tracks(self):
        """Fill the step-sequencer array depending on the
        the values yielded by node resistor inputs"""
        self.steps_resistance_values = self.bus.read_i2c_block_data(self.arduino_address0, 0, 16)#i hope this works

        for j in range(0, self.num_channels):
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
            


