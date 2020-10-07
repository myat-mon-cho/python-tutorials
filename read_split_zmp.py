file = open("./data1.txt")
text = file.read()
for t in text.split(";"):
    print(t)