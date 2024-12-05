from enum import Enum
import random

class RunSimulation():
    def __init__(self, trials, condition, data : Enum):
        self.average = 0
        self.data = data
        self.trials = trials
        self.condition = condition
        self.pieces = {i.name: 0 for i in self.data}
        for i in range(0, trials):
            self.average += self.CollectData()

    def getAverage(self) -> float:
        return self.average / self.trials
    
    def getAveragePieces(self) -> dict:
        average = self.pieces
        for value in self.pieces.keys():
            average[value] = self.pieces[value] / self.trials
            
        return average
    
    def getPieces(self) -> dict:
        return self.pieces
    
    def GetData(self, pick):
        for piece in self.data:
            if pick in piece.value:
                return piece.name
            
    def CollectData(self) -> int:
        pieces = {i.name: 0 for i in self.data}
        while True:
            allCollected = True
            total = 0
            for i in pieces.values():
                total += i
                if(i < self.condition):
                    allCollected = False
            if(allCollected):
                self.UpdatePieces(pieces)
                return total
            pick = random.randint(1, 99)
            pieces[self.GetData(pick)] += 1
        
    def UpdatePieces(self, piece):
        for value in self.pieces.keys():
            self.pieces[value] += piece[value]