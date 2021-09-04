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

