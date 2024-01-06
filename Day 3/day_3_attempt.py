import pandas as pd 
import numpy as np
import re

with open("input.txt","r") as file:
    data = file.read().split("\n")

df = pd.read_csv("input.txt", header=None, names=["string"])
df = df["string"].apply(lambda x: pd.Series(list(x)))


def check_surrounding(row_num : int, col_num : int, symbols : list):
    '''Returns True if we have a symbol around the number
       returns False if we don't
    '''
    if row_num == 0:
        if col_num == 0: 
            d = df.iloc[row_num: row_num + 2,
                    col_num: col_num + 2]
        elif col_num == (df.shape[1]-1):
            d = df.iloc[row_num: row_num + 2,
                    col_num - 1: col_num + 1]
        else:
            d = df.iloc[row_num: row_num + 2,
                    col_num - 1: col_num + 2] 
    elif row_num == (df.shape[0]-1):
        if col_num == 0:
            d = df.iloc[row_num - 1: row_num + 1,
                    col_num: col_num + 2]
        elif col_num == (df.shape[1]-1):
            d = df.iloc[row_num - 1: row_num + 1,
                    col_num - 1: col_num + 1]
        else:
            d = df.iloc[row_num - 1: row_num + 1,
                    col_num - 1: col_num + 2] 
    elif col_num == 0:
        d = df.iloc[row_num - 1: row_num + 2,
                    col_num: col_num + 2]
    elif col_num == (df.shape[1]-1):
            d = df.iloc[row_num - 1: row_num + 2,
                        col_num - 1: col_num + 1]   
    else:
        d = df.iloc[row_num - 1: row_num + 2,
                    col_num - 1: col_num + 2]
    
    if d.isin(symbols).any().any():
        return True
    else:
        return False



def parta():
    symbols = []
    for lines in data:
        for char in lines:
            if (not char.isnumeric() and char != "."):
                symbols += char

    symbols = list(dict.fromkeys(symbols))

    sum = 0
    all_num = []

    for line in data:
        delimiters = "".join(symbols)
        pattern = '[' + re.escape(delimiters) + "." + ']'
        a = [x for x in re.split(pattern, line) if x!= ""]
        numbers = [x for x in a if x.isnumeric()]
        temp_line = line

        for num in numbers:
            all_num.append(num)
            start = temp_line.find(num)
            length = len(num)
            replacement_str = ""
            for i in range(0,length):
                replacement_str += "."
            temp_line = temp_line.replace(num,replacement_str,1)
            is_part = False

            for i in range(0,length):
                row = data.index(line)
                col = start + i
                if check_surrounding(row_num= row, col_num= col, symbols=symbols):
                    is_part = True

            if is_part:
                sum += int(num)

    print(sum)
    print(max(all_num))

parta()

for line in data:
    temp_line = line
    for char in line:
        if char == "*":
            col_num = temp_line.find("*")
            row_num = data.index(line)
            temp_line = temp_line.replace("*",".",1)


            