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
            col = [row[i] for row in self.dataset]
            if '' in col:
                missing_columns.append(i)
        result = [[row[i] for i in missing_columns] for row in self.dataset]
        return result
    
    def writeFile(self):
        result = self.extract()
        with open('output/list_missing.csv','w') as f:
            for row in result:
                f.write(','.join(row) + '\n')
        
list_mv_cols = list_missing(sys.argv[1])
print("List columns with missing value: \n")
print(list_mv_cols.extract())
list_mv_cols.writeFile()