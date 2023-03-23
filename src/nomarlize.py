import csv
import sys
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
        print('row count',countRow)
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
                    self.contents[i][j]=str(nomarlize)
                except ValueError:
                    pass
    
    def writeFile(self):
        if self.type=='min-max':
            self.minMaxScaler()
            with open('output/nomarlize.csv','w',newline='') as file:
                    writer=csv.writer(file)
                    for row in self.contents:
                        writer.writerow(row)
            print("Normalized a numeric attribute using min-max")
                    
instance=Nomarlize(sys.argv[1],sys.argv[2])
instance.writeFile()