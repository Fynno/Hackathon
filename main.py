from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from Splitter import split, delete_punctuation, delete_stopwords
import correction
import connections
from Nmaxelements import Nmaxelements

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from frequent_words import create_wordcloud
import pandas as pd
from Splitter import split, delete_punctuation, delete_stopwords
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

data = delete_stopwords(delete_punctuation(data))
dataSplit = split(data)

# print(Nmaxelements(connections.connectionTable(data,dataSplit),100,dataSplit))

# correct typos in data
# data = correction.CorrectionFun(dataSplit)


text_file = open("Answers.txt", "w",encoding='utf-8')
text_file.write(" ".join(data))
text_file.close()

#create_wordcloud(data)