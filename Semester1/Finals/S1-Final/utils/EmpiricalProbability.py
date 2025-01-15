from enum import Enum
import random

class RunSimulation():
    def __init__(self, trials, dataMax, dataMin, data : Enum):
        self.data = data
        self.trials = trials
        self.dataMax = dataMax
        self.dataMin = dataMin
        self.pieces = {i.name: 0 for i in self.data}
        for i in range(0, self.trials):
            try:
                self.pieces[self.GatherData()] += 1
            except:
                self.pieces[None] = 1
            
        for piece in self.pieces:
            self.pieces[piece] /= trials
    
    def GetEmpirical(self)->dict:
        return self.pieces
            
    def GatherData(self):
        num = random.randint(self.dataMin, self.dataMax)
        for piece in self.data:
            if num in piece.value:
                return piece.name
    