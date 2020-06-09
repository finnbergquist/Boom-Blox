from gpiozero import MCP3008


class channels:
    """multidimensional array representing channels and steps"""

    def __init__(self, tempo,num_channels,num_steps):
        self.tempo = tempo #none of these are really implemented yet
        self.num_channels = num_channels
        self.num_steps = num_steps
        self.audio_file_struct = [["000" for i in range(0,num_steps)] for j in range(0,num_channels)]
        self.steps_resistance_values = []#holds resistor scanning objects at each step

    def init_analog_inputs(self):
        """setup the channel resistor reads fro each step in a 
        SINGLE channel(at least to start)"""
        for i in range(0, self.num_steps):
            self.steps_resistance_values.append(MCP3008(i))
        
    def to_sound_code(resistor_value):
        if resistor_value == 0.49:
            return "001"
        elif resistor_value == 0.10:
            return "010"
        elif resistor_value == 0.18:
            return "100"
        elif resistor_value == 0.22:
            return "002"
        else:
            print("resistor value did not match up with sound file")
            return


    def scan_tracks(self):
        """Fill the step-sequencer array depending on the
        the values yielded by node resistor inputs"""
        for i in self.steps_resistance_values:#assigning sound_codes based on resistance value in the steps
            self.audio_file_struct[0][i] = to_sound_code(self.steps_resistance_values[i].value)#only doing this in first channel(for now!!)


    def print_audio_file_struct(self):
        for i in range(0, self.num_channels):
            print(self.audio_file_struct[i])

    def set_audio_num(self, x, y, val):
        self.audio_file_struct[x][y] = val

    def get_audio_num(self, x, y):
        """simple getter method"""
        return self.audio_file_struct[x][y]
            


