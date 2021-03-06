from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from Splitter import split, alphanum_only, delete_stopwords
import correction
import connections
from Nmaxelements import Nmaxelements

import re

def answers_to_array(input_xlsx, sheet_no = 3, answer_column = 'answer_text'):
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

data = delete_stopwords([alphanum_only(element) for element in data])
dataSplit = split(data)

# correct typos in data
# data = correction.CorrectionFun(dataSplit)

weightlist = Nmaxelements(connections.connectionTable(data,dataSplit),100,dataSplit)
print(weightlist)

edges = pd.DataFrame(columns=['Source','Target','Type','Weight'])
for item in weightlist:
    edges = edges.append({'Source':item[1][0],'Target':item[1][1],'Type':'undirected','Weight':item[0]}, ignore_index=True)
edges.to_csv('edges.csv',index=False)

characters = pd.DataFrame(columns=['Id','Name'])
for item in enumerate(list(set(dataSplit))):
    characters = characters.append({'Id':item[0],'Name':item[1]}, ignore_index=True)
characters.to_csv('characters.csv',index=False)


'''text_file = open("connections.csv", "w",encoding='utf-8')
text_file.write(data)
text_file.close()
'''


#create_wordcloud(data)