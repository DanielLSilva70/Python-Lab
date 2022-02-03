cup_cakes = open('CupcakeInvoices.csv')

for row in cup_cakes:
    print(row)

for row in cup_cakes:
    values = row.split(',')
    print(values[2])    

for row in cup_cakes:
    values = row.split(',')
    total = int(values[3]) * float(values[4])
    print(total)

total = 0

for row in cup_cakes:
    values = row.split(',')
    total =  total + int(values[3]) * float(values[4])
    print(total)