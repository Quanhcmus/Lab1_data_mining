import sys
class deleteColumn():


    def __init__(self,pathFileName:str,percent):
        self.contents=self.readFile(pathFileName)
        self.amountInstances=self.countInstances()
        self.amountAttributes=self.countAttributes()
        self.percent=float(percent)
    @staticmethod
    def readFile(fileName):
        with open(fileName,'r') as f:
            contents=f.readlines()
        return contents
    
    def countInstances(self):
        return len(self.contents) - 1     # skip the first row

    def countAttributes(self):
        line=self.contents[1]
        return len(line.split(','))
    
    def deteleColumn(self):
        listCountMissing=[0 for i in range(self.amountAttributes)]
        # count the number of mising of each column
        for line in self.contents[1:]:
            elementInLine=line.split(',')
            for i in range(len(elementInLine)):
                if elementInLine[i]=='':
                    listCountMissing[i]+=1
        # get the column to delete
        listColumnDelete=[]
        for i in range(len(listCountMissing)):
            if listCountMissing[i]>self.percent*self.amountInstances:
                listColumnDelete.append(i)
        for i in range(len(listColumnDelete)):
            self.contents = [','.join(line.split(',')[:listColumnDelete[i]-i] + line.split(',')[(listColumnDelete[i]-i)+1:]) for line in self.contents]
            return len(listColumnDelete)
    def writeFile(self):
        countColumnDetele=self.deteleColumn()
        with open('output/deleteColumn.csv','w') as f:
            for line in self.contents:
                f.write(line)
        print('Deleted',countColumnDetele,'columns with the number of missing values is more than','{}%'.format(self.percent*100),'of the number of samples')
        print('Writed in output/deleteColumn.csv file')

instance=deleteColumn(sys.argv[1],sys.argv[2])
instance.writeFile()