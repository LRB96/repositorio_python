import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 5)
students = pd.read_csv("StudentsPerformance.csv")
print(students)