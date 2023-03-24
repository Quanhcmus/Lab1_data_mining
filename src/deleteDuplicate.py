import sys
class deleteDuplicate():
    
    def __init__(self,pathFileName:str):
        self.contents= self.readFile(pathFileName)
        
        
    @staticmethod
    def readFile(fileName):
        with open(fileName,'r') as f:
            contents=f.readlines()
        return contents
    
    def deleteDuplicate(self):
        rowUnique=[]
        indexDuplicate=[]
        for i in range(len(self.contents)):
            if self.contents[i] in rowUnique:
                indexDuplicate.append(i)
            else:
                rowUnique.append(self.contents[i])
        for i in range(len(indexDuplicate)):
            del self.contents[indexDuplicate[i]-i]
        return len(indexDuplicate)
    
    def writeFile(self):
        amountRow=self.deleteDuplicate()
        with open('output/deleteDuplicate.csv','w') as f:
            for line in self.contents:
                f.write(line)
        print(amountRow,'templates have been deleted')

instance=deleteDuplicate(sys.argv[1])
instance.writeFile()