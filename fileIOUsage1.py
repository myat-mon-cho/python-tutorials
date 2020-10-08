try:
    fo=open("D:\Mie Mie\MyAccount.txt","r+")
    
except IOError:
    print("Cant open the file ")
finally:
    fo1=open("data1.txt","r+")
    fo2=open("data2.txt","r+")
    str=fo1.read()
    str1=str.upper()
    fo2.writelines(str1)
    print("The existing file name is "+fo1.name)
    print("The read string is \n"+str)
    #Go to file pointer to the start 
    fo1.seek(0)
    print("The splitting is ")
    for line in fo1:
        splitt=line.split(";")
        #for splitItem in splitt:
            #fo1.writelines(splitItem)
        print(splitt)
    print("After creating uppercase :")
    for line in fo2:
        print(line)
    fo1.close()
    fo2.close()
    

