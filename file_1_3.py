with open('data1.txt') as data:
    for x in data.read().split(';'):
        print(x)
