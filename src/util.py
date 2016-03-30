
import numpy as np      # mathmatical library
import matplotlib.pyplot as plt

def makeBins(matrix, qtd=0, size=0, debug=False):
    #print(matrix[:,3])
    if debug:
        print("min",matrix.min())
        print("max",matrix.max())

    bins = []
    if size==0:
        min = matrix.min()
        max = matrix.max()
        width = (max-min) / qtd
        for i in range(qtd+1):
            bins.append(min + ( i * (max-min) / qtd ) )
    else:
        min = -size * qtd / 2
        width = size
        for i in range(qtd+1):
            bins.append(min + ( i * size ) )
    return bins, width

def hist(matrix, bins, plot=False):
    hist, bins = np.histogram(matrix, bins)
    if plot:
        center = (bins[:-1] + bins[1:]) / 2
        width = bins[1] - bins[0]
        plt.bar(center, hist, align='center', width=width*0.9)
        plt.show()
    return hist
