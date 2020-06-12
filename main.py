import pandas as pd

def answers_to_array(input_xlsx, sheet_no = 0, answer_column):
    """Returns array of answers from excel file

    Arguments:
        input_xlsx (str): path of input file
        sheet_no (int): index of the sheet to be accessed (zero-indexed)
        answer_column (str): name of column with answers"""

    return list(pd.read_excel(input_xlsx, sheet_name = sheet_no)[answer_column])