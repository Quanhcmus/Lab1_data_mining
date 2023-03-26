import sys

class count_missing_lines():

    def __init__(self,dataset):
        self.dataset = []
        self.missing_lines_count = 0
        with open(dataset,'r') as f:
            for line in f:
                self.dataset.append(line.strip().split(','))

    def countMissingLines(self): 
        for line in self.dataset:
            if "" in line: 
                self.missing_lines_count += 1
    
    def result(self):
        return self.missing_lines_count

count_mv_instances = count_missing_lines(sys.argv[1])
count_mv_instances.countMissingLines()
print("Number of lines with missing value: ",count_mv_instances.result())