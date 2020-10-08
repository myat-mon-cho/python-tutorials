from datetime import datetime
origin=open("highscore.txt","r")

def sortResult(sortedList,sortList,lineposition,criteria):

    origin.seek(0)
    for line in origin:
        splitting=line.split(",")
        if lineposition==2:
            eachItem=splitting[lineposition].strip()
        else:
            eachItem=splitting[lineposition]
        index=sortedList.index(eachItem)
        sortList[index]=line.strip()
        #sortList.insert(index,line.strip())
        #print("The position of "+line+" is"+str(index)+"and sortList(index) is "+sortList[index])

    print("Sorted the file according to "+criteria+" is")
    """for line in sortList:
        print(line)"""
    index=0
    while(index<len(sortList)):
        print( sortList[index])
        index=index+1

name=[]
score=[]
date=[]
dateText=[]
for line in origin:
    record=line.split(",")
    print(record)
    name.append(record[0])
    score.append(record[1])
    datestring=record[2]
    #trim the white space and \n
    dateTrim=datestring.strip()
    #convert string to date format to complete sorting
    dateObject=datetime.strptime(dateTrim,"%m/%d/%Y").date()
    date.append(dateObject)
print("name array is "+str(name))
name.sort()
print("Sort the name is "+str(name))

print("score array is "+str(score))
score.sort()
print("Sort the name is "+str(score))

print("date array is "+str(date))
date.sort()
for dateFormat in date:
    dateText1=dateFormat.strftime("%m/%d/%Y")
    dateText.append(dateText1)
print("Sort the date is "+str(dateText))

sortName=[None]*len(name)
sortScore=[None]*len(score)
sortDate=[None]*len(dateText)

"""
origin.seek(0)
for line in origin:
    splitting=line.split(",")
    eachname=splitting[0]
    index=name.index(eachname)
    print("Index of "+line+" is "+str(index))
    sortName.insert(index,line)

print("Sorted the file according to name is")
for line in sortName:
    print(line)
"""
sortResult(name,sortName,0,"Name")
sortResult(score,sortScore,1,"Score")
sortResult(dateText,sortDate,2,"Date")

"""
origin.seek(0)
for line in origin:
    splitting=line.split(",")
    eachscore=splitting[1]
    index=score.index(eachscore)
    sortScore.insert(index,line)

print("Sorted the file according to score is"+str(sortScore))

origin.seek(0)
for line in origin:
    splitting=line.split(",")
    eachdate=splitting[2]
    eachdatetrim=eachdate.strip()
    index=dateText.index(eachdatetrim)
    sortDate.insert(index,line)

print("Sorted the file according to date is"+str(sortDate))
"""



