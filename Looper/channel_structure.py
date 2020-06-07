class channels:
    """multidimensional array representing channels and steps"""

    audio_file_struct = [[5, 0, 5, 0, 5, 0, 5, 0], [3, 0, 0, 0, 3, 0, 0, 0]]

    def __init__(self, tempo,num_channels,num_steps):
        self.tempo = tempo #none of these are really implemented yet
        self.num_channels = num_channels
        self.num_steps = num_steps


    def scan_tracks(self):
        """Fill the step-sequencer array depending on the
        the values yielded by node resistor inputs
        """
        return

    def set_audio_num(self, x, y, val):
        self.audio_file_struct[x][y] = val

    def get_audio_num(self, x, y):
        """simple getter method"""
        return self.audio_file_struct[x][y]
            


