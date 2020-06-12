def splitter (list):
    wordsCut = []
    for answer in list:
        sentence = answer.split()
        for word in sentence:
            wordsCut.append(word)
    return wordsCut

