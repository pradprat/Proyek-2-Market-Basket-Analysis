import csv
import copy

listComb = []
def combinations(target,data):
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        listComb.append(new_target)
        combinations(new_target, new_data)
        
productID = []
with open('products.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        content = list(row)
        cek = content[0]
        cek = cek.split(";")
        productID.append(int(cek[0]))

combinations([], productID)

transactID = []
with open('transaksi.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    transaksi = '-'
    data = []
    for row in readCSV:
        content = list(row)
        cek = content[0]
        cek = cek.split(";")
        if (transaksi != cek[0]):
            transaksi = cek[0]
            data.sort()
            transactID.append(data)
            data = []
        data.append(int(cek[1]))
        
szTransact = len(transactID)
szComb = len(listComb)
freq = [0] * szComb
for i in range(1, szTransact):
    for j in range(szComb):
        iteratorT = 0
	iteratorC = 0
	lenT = len(transactID[i])
	lenC = len(listComb[j])
        while iteratorT < lenT and iteratorC < lenC:
	    if (transactID[i][iteratorT] == listComb[j][iteratorC]):
                iteratorC += 1
            iteratorT += 1
        if (iteratorC == lenC):
            freq[j] += 1

support = [0] * szComb
for i in range(0, szComb):
    support[i] = freq[i]/float(szTransact)
    print "%.2f" % (support[i])


