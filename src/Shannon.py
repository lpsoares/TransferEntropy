import util
import math

class Shannon:

    def __init__(self, matrix):
        self.matrix = matrix
        self.sample_size = len(matrix)

    def p(self, value):
        return value/self.sample_size

    def shannon_entropy(self, hist):
        H=0
        for i in hist:
            pi = self.p(i)
            if pi > 0:
                H += pi*math.log(pi,2)
        return -H

    def calcH(self, qtd=40,plot=False):
        #bins, width = util.makeBins(matrix[:,3],qtd=4, size=0.11, debug=True)
        bins, bin_size = util.makeBins(self.matrix,qtd)
        hist = util.hist(self.matrix, bins, plot)
        H = self.shannon_entropy(hist)
        return H,bin_size