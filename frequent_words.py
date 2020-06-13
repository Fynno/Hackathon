def create_wordcloud(list1):
    from wordcloud import  WordCloud
    import matplotlib.pyplot as plt
    wordsForCloud = " ".join(list1)
    wordcloud = WordCloud(width=1600, height=800, background_color="white").generate(wordsForCloud)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

