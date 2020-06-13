def split (list):
    wordsCut = []
    for answer in list:
        sentence = answer.split()
        for word in sentence:
            wordsCut.append(word.lower())
    return wordsCut

def delete_punctuation(input):
    import string
    blacklist = list(string.punctuation)
    clean = input
    for letter in blacklist:
        for i in range(0,clean.__len__()):
            if letter in clean[i]:
                clean[i] = clean[i].replace(letter,' ')
    return clean

def alphanum_only(list):
    import re
    return re.sub('[^a-zA-Z0-9 ä,ü,ö]', '', "".join(list))

def delete_stopwords(list1):
    from stop_words import get_stop_words
    stop_words = get_stop_words('german')
    return [' '.join(words) for words in
            [[word for word in answer.split(' ') if not word in stop_words] for answer in list1]]

def delete_short_words(list1):
    return [' '.join(words) for words in [[word for word in answer.split(' ') if len(word)>2]for answer in list1]]


