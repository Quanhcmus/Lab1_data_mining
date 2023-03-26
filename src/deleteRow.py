import sys

class deleteRow():

    def __init__(self,dataset,max_missing_percent):
        self.dataset = []
        self.max_missing_percent = float(max_missing_percent)
        with open(dataset,'r') as f:
            for line in f:
                self.dataset.append(line.strip().split(','))

    def delete_missing_rows(self):
        headers = self.dataset[0]
        num_cols = len(headers)
        max_missing_count = int(self.max_missing_percent*num_cols)
        delete_indices = []
        for i in range(1,len(self.dataset)):
            row = self.dataset[i]
            missing_count = 0
            for j in range(num_cols):
                if row[j] == '':
                    missing_count += 1
            if missing_count > max_missing_count:
                delete_indices.append(i)
        new_data = [row for i, row in enumerate(self.dataset) if i not in delete_indices]
        return new_data
    
    def writeFile(self):
        result = self.delete_missing_rows()
        with open('output/deleteRow.csv','w') as f:
            for row in result:
                f.write(','.join(row) + '\n')

list_mv_cols = deleteRow(sys.argv[1],sys.argv[2])
print(list_mv_cols.delete_missing_rows())
list_mv_cols.writeFile()