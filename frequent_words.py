def create_wordcloud(list1):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    wordsForCloud = " ".join(list1)
    wordcloud = WordCloud(width=1600, height=800, background_color="white").generate(wordsForCloud)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def word_frequency_dict(list):
    word_freq = {}
    for word in list:
        try:
            if word in word_freq:
                word_freq[word] = word_freq[word] + 1
            else:
                word_freq[word] = 1
        except:
            print('Fehler bei Wort: '+ word)
    return dict(sorted(word_freq.items(),key=lambda  x:x[1],reverse=True))

def plot_most_frequent(dictionary, top_n = 10):
    from matplotlib import pyplot as plt
    x,y = zip(*sorted(dict(list(dictionary.items())[:top_n]).items()))
    plt.bar(x,y)
    plt.show()
    return

