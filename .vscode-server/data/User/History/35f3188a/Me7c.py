import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 20)
df = pd.read_csv("Studentsperformance.csv")
print(df)
print(df.sum(axis=1))