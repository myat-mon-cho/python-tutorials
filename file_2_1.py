import csv
import operator
sample=open('hightscore.dat','r')
csv1=csv.reader(sample,delimiter=',')
sort = sorted(csv1,key=operator.itemgetter(0))
for line in sort:
    print(line)