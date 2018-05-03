import csv
import copy

listID = []
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
            print data
            print len(listID)
            listID.append(data)
            data = []
        data.append(int(cek[1]))

#print listID
listComb = []
