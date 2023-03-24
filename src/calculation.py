import sys
import numpy as np
import csv
class calculation():
    
    def __init__(self,pathFileName,operation,indexCol1,indexCol2):
        """_summary_

        Args:
            pathFileName (string): file input name
            operation (_type_): add or sub or mul or div
            indexCol1 (_type_): col 1
            indexCol2 (_type_): col 2
        """
        self.contents=self.readFile(pathFileName)
        self.operation=operation
        self.indexCol1=indexCol1
        self.indexCol2=indexCol2
    
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
    
    def readCol(self,indexCol):
        valueCol=[]
        for row in self.contents[1:]:
            try:
                value=float(row[int(indexCol)])
                valueCol.append(value)
            except ValueError:
                valueCol.append(0)
        return valueCol
    
    def  addition(self):
        col1=np.array(self.readCol(self.indexCol1))
        col2=np.array(self.readCol(self.indexCol2))
        return col1+col2
    
    def subtraction(self):
        col1=np.array(self.readCol(self.indexCol1))
        col2=np.array(self.readCol(self.indexCol2))
        return col1-col2

    def multiplication(self):
        col1=np.array(self.readCol(self.indexCol1))
        col2=np.array(self.readCol(self.indexCol2))
        return col1*col2
    
    def division(self):
        col1=np.array(self.readCol(self.indexCol1))
        col2=np.array(self.readCol(self.indexCol2))
        return col1/col2
    
    def calc(self):
        if self.operation=='add':
            return self.addition()
        elif self.operation=='sub':
            return self.subtraction()
        elif self.operation=='mul':
            return self.multiplication()
        elif self.operation=='div':
            return self.division()

instance=calculation(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
print('col['+sys.argv[3]+']',sys.argv[2],'col['+sys.argv[4]+']:')
print(instance.calc())