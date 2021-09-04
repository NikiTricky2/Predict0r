import pandas as pd
import numpy as np

def load(path):
  return pd.read_csv(path)

def column_types(df):
  col = list(df.columns)
  types = [typeof it for it in list(df.iloc[0])]
  return zip(col, types)
