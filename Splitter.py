def split (list):
    wordsCut = []
    for answer in list:
        sentence = answer.split()
        for word in sentence:
            wordsCut.append(word.lower())
    return wordsCut

def delete_punctuation(input):
    import string
    whitelist = set('abcdefghijklmnopqrstuvwxyz äöüß')
    blacklist = list(string.punctuation)
    clean = input
    for letter in blacklist:
        for i in range(0,clean.__len__()):
            if letter in clean[i]:
                clean[i] = clean[i].replace(letter,' ')
    return clean








97-122

def count(list=[]):
    uniques = set(list)
    counter = {}


