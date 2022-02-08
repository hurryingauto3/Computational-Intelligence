#Class of generic evolutionary algorithm
class EvolAlgo:
    def __init__(file):
        readFile(file)
        pass
    
    def readFile(self, file):
        f = with open(file):
            for line in f:
                self.fileData.append(line)

    def run(self):
        pass
    

