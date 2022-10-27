import pandas as pd
import numpy as np

students = pd.read_csv("StudentsPerformance.csv")
print(students)
pd.set_option("display.max_columns", 20)