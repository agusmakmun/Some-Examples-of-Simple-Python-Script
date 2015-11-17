import csv
f = open('data.csv', 'rb')
reader = csv.reader(f)
next(reader)
out = []
inject_list = []
counter = 0
for row in reader:
    counter += 1
    out.append(row[0][4:])
    angkatan = ''
    if row[0][4:7] == '110':
        angkatan = '110'
    elif row[0][4:7] == '120':
        angkatan = '120'
    elif row[0][4:7] == '130':
        angkatan = '130'
    elif row[0][4:7] == '140':
        angkatan = '140'
    elif row[0][4:7] == '150':
        angkatan = '150'
    else:
        pass
    inject = angkatan+'{0:03}'.format(counter)
    if len(inject) != 6:
        inject = ''
    else:
        inject = inject
    inject_list.append(inject)
    
sortED = sorted(out)
f.close()

#print sortED
if inject_list not in sortED:
    for mhs in inject_list:
        if mhs == '':
            pass
        else:
            print "L200"+mhs

