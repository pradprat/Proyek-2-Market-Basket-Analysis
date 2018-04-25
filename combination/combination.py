import csv
import copy
def combinations(target,data):
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        print new_target
        combinations(new_target, new_data)
        
listID = []
with open('products.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        content = list(row)
        cek = content[0]
        cek = cek.split(";")
#        print cek[0]
        listID.append(cek[0])
        
#print listID
listComb = []

combinations(listComb, listID)