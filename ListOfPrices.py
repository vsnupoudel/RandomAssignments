# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import itertools 
import copy

stringAll = "12,345,56,781,789,123,45,6,789,789,223,123"
listStr = stringAll.split(","); length = len(listStr)
listInt = [int(num) for num in listStr]

count = 9 #do not use constant
sumAll = 12345+56781+789+123+45+6+789+789+223123 #do not use constant

# Combinations of commas
rangeLen = list( range(1, length)) #; print(rangeLen)
#rangeCount = list( range(1, count+1)); print(rangeCount)
for comb in itertools.combinations(rangeLen, count-1):
    removeCommas = set(rangeLen) - set(comb) #; print(removeCommas)
    newStr = "" ; counts=0
    for c in stringAll:
        if c==",":
            counts+=1
            if counts not in removeCommas:
                newStr+=c
        else:
            newStr+=c
    # print(newStr)
    listStr = newStr.split(",")    
    # print(listStr)
    listInt = [int(num) for num in listStr]
    
    if sum(listInt)==sumAll:
        print("Hell Yeah!!")
        print( listInt, newStr)
        # return listInt, newStr
    
    
    




