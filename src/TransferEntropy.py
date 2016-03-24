# Condigo do Leo convertido para Python
# Luciano 24 março 2016

import numpy as np      # mathmatical library
import xls
import matplotlib.pyplot as plt

#filename = '../data/FinancialTE.xlsx'
filename = '../data/Exemplo.xlsx'
worksheet = 'Log-Rets'
#last_column = 'HF'      # specify the last column to read
last_column = 'E'

XLS = xls.xls(filename, worksheet)
matrix,name,time = XLS.getValues(last_column) #retriev matrix with number, names and time

print(matrix[:,3])
#print(min(matrix[3]))
#print(max(matrix[3]))

hist, bins = np.histogram(matrix[:,3], bins=32)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()


'''
M,N=size(Rets,nargout=2) #Input Rets (log-returns for all time series)
passo=0.05 #% Set step for the calculation of the probability distributions.
Peq=_min(_min(Rets)) #% Calculates minimum and maximum values, according to step
Gran=_max(_max(Rets))
minihist=passo * floor((1 / passo) * Peq)
maxihist=passo * ceil((1 / passo) * Gran)
xhist=arange_(minihist,maxihist,passo)
for i in arange_(1,N).reshape(-1): #% Starts the sequence of calculations
    i
    for j in arange_(1,N).reshape(-1):
        clear(char('termo'))
        clear(char('ProbABC'))
        clear(char('ProbAB'))
        clear(char('ProbBC'))
        clear(char('ProbB'))
        clear(char('SortedABC'))
        clear(char('SortedAB'))
        clear(char('SortedBC'))
        clear(char('SortedB'))
        # Collects time series for i, j, and i-1.
        A[arange_(1,M - 1),1]=Rets(arange_(2,M),i)
        B[arange_(1,M - 1),1]=Rets(arange_(1,M - 1),i)
        C[arange_(1,M - 1),1]=Rets(arange_(1,M - 1),j)
        #  Writes the distributions according to the symbols.
        for L in arange_(1,M - 1).reshape(-1):
            classific[L,1]=ceil((A(L,1) - minihist) / passo)
            classific[L,2]=ceil((B(L,1) - minihist) / passo)
            classific[L,3]=ceil((C(L,1) - minihist) / passo)
        #Sorts rows.
        SortedABC=sortrows(classific,[1,2,3])
        TempoAB[arange_(),arange_(1,2)]=classific(arange_(),arange_(1,2))
        SortedAB=sortrows(TempoAB,[1,2])
        TempoBC[arange_(),arange_(1,2)]=classific(arange_(),arange_(2,3))
        SortedBC=sortrows(TempoBC,[1,2])
        TempoB[arange_(),1]=classific(arange_(),2)
        SortedB=sortrows(TempoB)
        #Calculates probability distributions
        clear(char('Au'))
        clear(char('I'))
        clear(char('J'))
        clear(char('Count'))
        Au,I,J=unique(SortedABC,char('rows'),nargout=3)
        Count=accumarray(J,1)
        ProbABC[arange_(),arange_(1,3)]=Au(arange_(),arange_(1,3))
        ProbABC[arange_(),4]=Count(arange_(),1)
        clear(char('Au'))
        clear(char('I'))
        clear(char('J'))
        clear(char('Count'))
        Au,I,J=unique(SortedAB,char('rows'),nargout=3)
        Count=accumarray(J,1)
        ProbAB[arange_(),arange_(1,2)]=Au(arange_(),arange_(1,2))
        ProbAB[arange_(),3]=Count(arange_(),1)
        clear(char('Au'))
        clear(char('I'))
        clear(char('J'))
        clear(char('Count'))
        Au,I,J=unique(SortedBC,char('rows'),nargout=3)
        Count=accumarray(J,1)
        ProbBC[arange_(),arange_(1,2)]=Au(arange_(),arange_(1,2))
        ProbBC[arange_(),3]=Count(arange_(),1)
        clear(char('Au'))
        clear(char('I'))
        clear(char('J'))
        clear(char('Count'))
        Au,I,J=unique(SortedB,char('rows'),nargout=3)
        Count=accumarray(J,1)
        ProbB[arange_(),1]=Au(arange_(),1)
        ProbB[arange_(),2]=Count(arange_(),1)
        #Calculates transfer entropy
        U,V=size(ProbABC,nargout=2)
        for k in arange_(1,U).reshape(-1):
            caixa[1,arange_(1,3)]=ProbABC(k,arange_(1,3))
            num1=0
            oi,oj=size(ProbAB,nargout=2)
            for ele in arange_(1,oi).reshape(-1):
                if ProbABC(k,arange_(1,2)) == ProbAB(ele,arange_(1,2)):
                    num1=copy_(ele)
            num2=0
            oi,oj=size(ProbBC,nargout=2)
            for ele in arange_(1,oi).reshape(-1):
                if ProbABC(k,arange_(2,3)) == ProbBC(ele,arange_(1,2)):
                    num2=copy_(ele)
            num3=0
            oi,oj=size(ProbB,nargout=2)
            for ele in arange_(1,oi).reshape(-1):
                if ProbABC(k,2) == ProbB(ele,1):
                    num3=copy_(ele)
            if num1 * num2 * num3 == 0:
                termo[k,1]=0
            else:
                termo[k,1]=(ProbABC(k,4) / (M - 1)) * log((ProbABC(k,4) * ProbB(num3,2)) / (ProbBC(num2,3) * ProbAB(num1,3))) / log(2)
        TE[i,j]=_sum(termo)

'''