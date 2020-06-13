def connectionTable(data,dataSplit):
    words = list(set(dataSplit))

    bigTable=[]
    Fails = 0
    print(words)
    for i in words:
        v =[]
        for a in words:
            v.append(0)
        bigTable.append(v)
 
    for element in words:
        if len(element)> 2:
            print(element)
            for answers in data:
                if element in answers:
                    everyElement = answers.split()
                    for x in everyElement:
                        if x != element:
                            bigTable[words.index(element)][words.index(x.lower())] = bigTable[words.index(element)][words.index(x.lower())] +1 
 
                          
    return bigTable