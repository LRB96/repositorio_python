import pandas as pd
import numpy as np

df = pd.DataFrame({"columna1":[1,2,3],
                                "Columna2":[4,5,6],
                                "Columna3":[7,8,9,]})
print(df)
print(df.shape)
nombres = ["columna0", "columna1","columna2"]
df.columns=nombres
print(df)
print(df.index)
print(df.describe)
