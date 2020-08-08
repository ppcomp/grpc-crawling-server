import pandas as pd
import sys, os

filename = os.path.dirname(os.path.abspath(__file__)) + '/board_data.csv'
data = pd.read_csv(filename, index_col='code').T
data = data.where(pd.notnull(data), None).to_dict()