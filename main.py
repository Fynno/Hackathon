from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from Splitter import split, delete_punctuation
import correction
import connections
from Nmaxelements import Nmaxelements

def answers_to_array(input_xlsx, sheet_no = 0, answer_column = 'answer_text'):
    """Returns array of answers from excel file
    Arguments:
        input_xlsx (str): path of input file
        sheet_no (int): index of the sheet to be accessed (zero-indexed)
        answer_column (str): name of column with answers

    Returns:
        array of strings with answers"""

    answers = list(pd.read_excel(input_xlsx, sheet_name = sheet_no)[answer_column])
    answers_cleaned = [element.replace("\n+","").replace("\n","") for element in answers]
    return answers_cleaned

data = answers_to_array('Freitext.xls',sheet_no = 0,answer_column = 'answer_text')


dataunSplit = delete_punctuation(data)
dataSplit = split(delete_punctuation(data))
print(Nmaxelements(connections.connectionTable(dataunSplit,dataSplit),100,dataSplit))


data = correction.CorrectionFun(split(dataunSplit))


wordsForCloud = " ".join(data)

notOfInterest = "und von Der das den wir ist die auf im es da zu sind mit oder auch sein sollten aber wenn alle für ich sollte Nichts wie sie werden eine nach man sehr nicht".split()
STOPWORDS.update(notOfInterest )

wordcloud = WordCloud(width=1600,height=800,background_color="white").generate(wordsForCloud)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
