import sys

class list_missing():

    def __init__(self,dataset):
        self.dataset = []
        with open(dataset,'r') as f:
            for line in f:
                self.dataset.append(line.strip().split(','))

    def extract(self):
        headers = self.dataset[0]
        missing_columns = []
        for i in range(len(headers)):
            col = [row[i] for row in self.dataset[1:]]
            if '' in col:
                missing_columns.append(i)
        result = [[row[i] for i in missing_columns] for row in self.dataset]
        return result
    
    def writeFile(self):
        result = self.extract()
        with open('test.csv','w') as f:
            for row in result:
                f.write(','.join(row) + '\n')
        
instance = list_missing(sys.argv[1])
print(instance.extract())
instance.writeFile()