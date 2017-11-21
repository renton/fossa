import numpy

class PixelInfo():
    def __init__(self):
        self.entries = {}

        self.mean = []
        self.stdd = []

        # TODO count clusters

    def __repr__(self):
        return str(len(self.entries.keys()))

    def add_entry(self, entry):
        if entry not in self.entries:
            self.entries[entry] = 0
        self.entries[entry] += 1

    def calculate(self):
        for i in range(3):
            vals = []

            for hex_val,count in self.entries.items():
                # TODO should count come into play?
                vals.append(hex_val[i])

            #TODO why is vals sometimes empty?????
            if len(vals) != 0:
                self.mean.append(int(numpy.mean(vals).item()))
                self.stdd.append(int(numpy.std(vals).item()))
            else:
                self.mean = [0,0,0]
                self.stdd = [0,0,0]
