def split (list):
    wordsCut = []
    for answer in list:
        sentence = answer.split()
        for word in sentence:
            wordsCut.append(word.lower())
    return wordsCut

def count(list=[]):
    uniques = set(list)
    counter = {}


