import csv
import sys
import numpy as np
class Nomarlize():
    def __init__(self,pathFileName,type) :
        self.contents=self.readFile(pathFileName)
        self.type=type
    @staticmethod
    def readFile(fileName):
        contents=[]
        with open(fileName,'r') as f:
            reader=csv.reader(f)
            for row in reader:
                contents.append(row)
        return contents
    
    def listSample(self):
        listTest=[]
        amountAttributes=len(self.contents[1])
        countRow=0
        for i in range(1,len(self.contents)):
            for j in range(amountAttributes):
                if self.contents[i][j]!='' and j not in listTest:
                    listTest.append(j)
            if len(listTest)==amountAttributes-1:
                countRow=i
                break
        return countRow
    
    def numericalAttributes(self):
        listNumericalAttributes=[]
        countRow=self.listSample()
        for i in range(countRow):
            for j,value in enumerate(self.contents[i]):
                if j not in listNumericalAttributes:
                    try:
                        floatValue=float(value)
                        listNumericalAttributes.append(j)
                    except ValueError:
                        pass
        return listNumericalAttributes
    
    def minMaxScaler(self):
        listNumericalAttributes=self.numericalAttributes()
        maxValue=float('-inf')
        minValue=float('inf')
        for row in self.contents:
            for i in listNumericalAttributes:
                try:
                    if maxValue<float(row[i]):
                        maxValue=float(row[i])
                    elif minValue>float(row[i]):
                        minValue=float(row[i])
                except ValueError:
                    pass
        for i in range(len(self.contents)):
            for j in listNumericalAttributes:
                try:
                    value=float(self.contents[i][j])
                    nomarlize=(value-minValue)/(maxValue-minValue)
                    self.contents[i][j]='{:.8f}'.format(nomarlize)
                except ValueError:
                    pass
    
    def zScore(self):
        listNumericalAttributes=self.numericalAttributes()
        listNumerical=[]
        for row in self.contents:

            for j in listNumericalAttributes:
                try:
                    value=float(row[j])
                    listNumerical.append(value)
                except ValueError:
                    pass
        numpyArray=np.array(listNumerical)
        mean=numpyArray.mean()
        std=numpyArray.std()
        for i in range(len(self.contents)):
            for j in listNumericalAttributes:
                try:
                    value=float(self.contents[i][j])
                    nomarlize=(value-mean)/std
                    self.contents[i][j]='{:.8f}'.format(nomarlize)
                except ValueError:
                    pass
    
    def writeFile(self):
        if self.type=='min-max':
            self.minMaxScaler()
            with open('output/nomarlize_min-max.csv','w',newline='') as file:
                    writer=csv.writer(file)
                    for row in self.contents:
                        writer.writerow(row)
            print("Normalized a numeric attribute using min-max")
        elif self.type=='z-score':
            self.zScore()
            with open('output/nomarlize_z-score.csv','w',newline='') as file:
                    writer=csv.writer(file)
                    for row in self.contents:
                        writer.writerow(row)
            print("Normalized a numeric attribute using z-score")
                    
instance=Nomarlize(sys.argv[1],sys.argv[2])
instance.writeFile()