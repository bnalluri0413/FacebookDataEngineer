def countCharOcinStr(testString,charOccur):
   charCount = 0
   if testString == charOccur:
    return 1
   else:
    for s in testString:
        if s.lower() == charOccur.lower() :
            charCount = charCount + 1
    return charCount


#print ("Count of e in GeeksforGeeks is : " +  str(countCharOcinStr('GeeksforGeeks','e'))) 
#print ("Count of e in GeeksforGeeks is : " +  str(countCharOcinStr('e','e'))) 
#print ("Count of e in GeeksforGeeks is : " +  str(countCharOcinStr('Brb','b'))) 

def avgWordLenth(wordList):
    if not wordList:
      return None
    return sum(map(len,wordList))/float(len(wordList))

print ("The Average length of String in list is : " +  str(avgWordLenth(['gfg', 'is', 'best', 'for', 'geeks']))) 
print ("The Average length of String in list is : " +  str(avgWordLenth([]))) 
print ("The Average length of String in list is : " +  str(avgWordLenth(['gfg']))) 