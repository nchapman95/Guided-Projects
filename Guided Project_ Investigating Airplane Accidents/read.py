

import pandas as pd
import numpy as np
import math
reader = open("AviationData.txt")
aviation_data = []
for line in reader:
    aviation_data.append(line)
aviation_list = []
for each in aviation_data:
    aviation_list.append(each.replace(' ','').split('|'))

lax_code = []

for i,row in enumerate(aviation_list):
    for y,col in enumerate(row):
        if "LAX94LA336" in col:
            lax_code.append(row)



"""
There didn't really seem to be any downsides, but looping
Through every row and column does seem like it would be
inefficient as the dataset grows. 

"""

def linear_time(ls,search_string):
    for each in ls:
        temp = ''.join(each)
        if search_string in temp:
            return(each)


"""
This seems like it would be time-complexity O(n)
Because I'm only searching through n times. But I'm not sure how 
things are affected when I combine the strings together. 
"""

aviation_df = pd.DataFrame(aviation_list[1:],columns=aviation_list[0])
aviation_df = aviation_df.sort_values(by='AccidentNumber')

aviation_df = aviation_df.reset_index()                                     
def log_time(df,search_col,search_string):
    length = len(df)
    upper_bound = length - 1
    lower_bound = 0
    index = math.floor((upper_bound + lower_bound) / 2)
    guess = (df.loc[index][search_col])
    
    while search_string != guess and upper_bound >= lower_bound:
        if search_string < guess:
            upper_bound = index - 1
        else:
            lower_bound = index + 1
        index = math.floor((lower_bound + upper_bound) / 2)
        guess = (df.loc[index][search_col])
    
    if search_string == guess:
        return df.loc[index]
    else:
        return -1


#print(log_time(aviation_df,'AccidentNumber','LAX94LA336'))


aviation_dict_list = []
lax_dict = []
for each in aviation_data[1:]:
    row = each.split('|')
    row_dict = {}
    for i,col in enumerate(aviation_data[0].split('|')):
        row_dict[col] = row[i]
    aviation_dict_list.append(row_dict)
    
for item in aviation_dict_list:
    if item[' Accident Number '].replace(' ','') == 'LAX94LA336':
        lax_dict.append(item)
        
"""
I mean, looping through a dictionary of rows can't be less complex than just looking Through
a single array, column, series for the value right?


"""
    

aviation_df['state'] = aviation_df['Location'].str.split(',')[1]

print(aviation_df['state'].value_counts()[0])



  




