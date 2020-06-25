from gpiozero import MCP3008


def to_sound_code(resistor_value):
    """temporary helper"""
    if round(resistor_value, 2) <= 0.05:
        print("resistor value did not match up with sound file")
        return "000"
    elif 0.05 < round(resistor_value, 2) <= 0.10:
        return "100"
    elif 0.10 < round(resistor_value, 2) <= 0.15:
        return "010"
    elif 0.15 < round(resistor_value, 2) <= 0.20:
        return "312"
    elif 0.20 < round(resistor_value, 2) <= 0.25:
        return "002"
    elif 0.25 < round(resistor_value, 2) <= 0.30:
        return "002"
    elif 0.30 < round(resistor_value, 2) <= 0.35:
        return "002"
    elif 0.35 < round(resistor_value, 2) <= 0.40:
        return "002"
    elif 0.40 < round(resistor_value, 2) <= 0.45:
        return "002"
    elif 0.45 < round(resistor_value, 2) <= 0.50:
        return "002"
    elif 0.55 < round(resistor_value, 2) <= 0.60:
        return "002"
    elif 0.60 < round(resistor_value, 2) <= 0.65:
        return "002"
    elif 0.65 < round(resistor_value, 2) <= 0.70:
        return "002"
    elif 0.70 < round(resistor_value, 2) <= 0.75:
        return "002"
    elif 0.75 < round(resistor_value, 2) <= 0.80:
        return "002"
    elif 0.80 < round(resistor_value, 2) <= 0.85:
        return "002"
    elif 0.85 < round(resistor_value, 2) <= 0.90:
        return "002"
    elif 0.90 < round(resistor_value, 2) <= 0.95:
        return "002"
    elif 0.95 < round(resistor_value, 2) <= 1.0:
        return "002"
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
        self.steps_resistance_values = []#holds resistor scanning objects at each step

    def init_analog_inputs(self):
        """setup the channel resistor reads for each step in a 
        SINGLE channel(at least to start)"""
        for i in range(0, self.num_steps * self.num_channels):#will need change when MC3008 values no longer linear
            self.steps_resistance_values.append(MCP3008(i))#[MCP3008[0],MCP3008[1], etc.]

    def scan_tracks(self):
        """Fill the step-sequencer array depending on the
        the values yielded by node resistor inputs"""
        for j in range(0, 2):
            print("entering j loop")
            for i in range(0, self.num_steps):#assigning sound_codes based on resistance value in the steps
                self.audio_file_struct[j][i] = to_sound_code(self.steps_resistance_values[i + (4*j)].value)#only doing this in first channel(for now!!)
                print(round(self.steps_resistance_values[i + (4*j)].value, 2))

    def print_audio_file_struct(self):
        for i in range(0, self.num_channels):
            print(self.audio_file_struct[i])

    def set_audio_num(self, x, y, val):
        self.audio_file_struct[x][y] = val

    def get_audio_num(self, x, y):
        """simple getter method"""
        return self.audio_file_struct[x][y]
            


