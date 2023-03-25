import argparse

class impute():

    def __init__(self,dataset,method,columns, output):
        self.dataset = []
        self.method = method
        self.columns = columns
        self.output = output
        with open(dataset,'r') as f:
            for line in f:
                self.dataset.append(line.strip().split(','))
    def can_convert_to_float(self,string):
        try:
            float(string)
            return True
        except ValueError:
            return False
        
    def fillMissingValues(self):
        headers = self.dataset[0]
        for col in self.columns:
            col_idx = headers.index(col)
            values = []
            for row in self.dataset[1:]:
                if row[col_idx] != '':
                    values.append(row[col_idx])
            if all(self.can_convert_to_float(value) for value in values):
                values = [float(value) for value in values]
                if self.method == 'mean':
                    imputed_value = sum(values)/len(values)
                elif self.method == 'median':
                    values.sort()
                    n = len(values)
                    if n % 2 == 0:
                        imputed_value = (values[n // 2] + values[n // 2 - 1]) / 2
                    else:
                        imputed_value = values[n // 2]
                else:
                    raise SyntaxError("It's the wrong method")   
            else:
                if self.method == 'mode':
                    counts = {}
                    for value in values:
                        if value not in counts:
                            counts[value] = 0
                        counts[value] += 1
                    mode_value = max(counts, key=counts.get)
                    imputed_value = mode_value
                else: 
                    raise SyntaxError("It's the wrong method")  
            for row in self.dataset:
                    if row[col_idx] == '':
                        row[col_idx] = str(imputed_value)
        return self.dataset    
    
    def writeFile(self): 
        result = self.fillMissingValues()
        with open(self.output,'w') as f:
            for row in result:
                f.write(','.join(row) + '\n')

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Impute missing values in a CSV file')
   parser.add_argument('data_file', help='path to input CSV file')
   parser.add_argument('--method', choices=['mean', 'median', 'mode'], default='mean', help='imputation method')
   parser.add_argument('--columns', nargs='+', help='columns to impute')
   parser.add_argument('--out', dest='out_file', default='result.csv', help='path to output CSV file')
   args = parser.parse_args()
   args = parser.parse_args()
   list_mv_col = impute(args.data_file,args.method,args.columns,args.out_file)
   print(list_mv_col.fillMissingValues())
   list_mv_col.writeFile()
