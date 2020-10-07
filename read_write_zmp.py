# read text from data1.txt
text_from_data1 = open("./data1.txt").read()
# convert text to uppercase letters
upper_text = text_from_data1.upper()
# write the upper_text into data2.txt
open("./data2.txt", "w").write(upper_text)