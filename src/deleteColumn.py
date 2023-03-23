import sys
class deleteColumn():

    def __init__(self,pathFileName:str):
        self.contents=self.readFile(pathFileName)
        self.amountInstances=self.countInstances()
        self.amountAttributes=self.countAttributes()
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
            if listCountMissing[i]>500:
                listColumnDelete.append(i)
        for i in range(len(listColumnDelete)):
            self.contents = [','.join(line.split(',')[:listColumnDelete[i]-i] + line.split(',')[(listColumnDelete[i]-i)+1:]) for line in self.contents]
            return len(listColumnDelete)
    def writeFile(self):
        countColumnDetele=self.deteleColumn()
        with open('output/deleteColumn.csv','w') as f:
            for line in self.contents:
                f.write(line)
        print('deleted',countColumnDetele,'columns with the number of missing values is more than 50% of the number of samples')

instance=deleteColumn(sys.argv[1])
instance.writeFile()