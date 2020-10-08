with open('data1.txt', 'r') as data1:
    upper = data1.read().upper()
with open('data2.txt', 'a') as data2:
    data2.write(upper)