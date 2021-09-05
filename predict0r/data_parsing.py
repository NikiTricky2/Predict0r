import pandas as pd
import numpy as np

def load(path):
  return pd.read_csv(path)

def save(df, path):
  return df.to_csv(path)

def column_types(df):
  col = list(df.columns)
  types = [type(it) for it in list(df.iloc[0])]
  return zip(col, types)

def removeCol(df, name):
  return df.drop(name, inplace=True, axis=1)

def replace(df, replace, val):
  df.replace(replace, val, inplace=True)

def replaceNum(df, col, sort=None, replace_list=None, reverse=False):
  num = sorted(df[col].unique(), key=sort, reverse=reverse)
  for n, st in enumerate(num):
    a = n
    if replace_list != None:
      a = replace_list[n]
    df.replace(st, a, inplace=True)
