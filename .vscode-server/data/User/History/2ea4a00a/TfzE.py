import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# df = pd.read_csv("DATASETS/call_of_duty/cod.csv")
# print(df)
# adult_names = df.loc[df["kills"]>300,["name","level"]]
# print(adult_names)
# new_data = df.iloc[0:3,11]
# print(new_data)

df = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
print(df)
plt.figure()
plt.plot(df) 
plt.show()





# df = pd.read_csv("titanic.csv")
# print(df)
# ages = df["Age"]
# print(ages)
# print(type(df["Age"]))
# print(df["Age"].shape)
# age_sex = df[["Age", "Sex"]]
# print(age_sex)
# print(type(df[["Age","Sex"]]))
# print(df[["Age","Sex"]].shape)
# print("\n")
# above_35 = df[df["Age"]>35]
# print(above_35)
# print(above_35.shape)
# class_23 = df[df["Pclass"].isin([2,3])]
# print(class_23)






# titanic = pd.read_csv("titanic.csv")
# print(titanic)
# print(titanic.dtypes)
# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)






# df = pd.DataFrame({
#     "Name":
#     ["Braund, Mr, Owen Harris",
#     "Allen, Mr, William Henry",
#     "Bonnel, Miss ELizabeth",
# ],
#     "Age":
#     [22,35,58],
#     "Sex":
#     ["male","male","female"],
# })
# print(df)
# print("\n")
# print(df["Sex"])
# ages = pd.Series([22,35,58],name="Age")
# print(ages)
# print(df["Age"].max())
# print(ages.max())
# print(df.describe())




























# nombre_paises=["China","India","Estados Unidos", "Indonesia","Pakistán","Brasil","Nigeria","Bangladesh","Rusia","México"]
# encabezado = ["Poblacion","Porcentaje"]
# datos=[[1439,18.47],
#             [1380,17.70],  
#             [331,4.25],
#             [273,3.51],
#             [220,2.83],
#             [212,2.73],
#             [206,2.64],
#             [164,2.11],
#             [145,1.87],
#             [128,1.65]]
# paises = pd.DataFrame(datos,index=nombre_paises,columns=encabezado)
# print(paises)
# print("\n")
# print(paises.iloc[0:4])
# print("\n")
# print(paises.loc["Brasil"])
# print("\n")
# reglon = pd.Series(name="Japón", data=[126,1.62], index=["Poblacion", "Porcentaje"])
# # print(reglon)
# print("\n")
# paises = paises.append(reglon)
# print(paises)
# print("\n")
# paises.drop(["Japón"],axis=0,inplace=True)
# print(paises)
# print("\n")
# print(paises.cumsum())









# df = pd.DataFrame({"columna1":[1,2,3],
#                                 "Columna2":[4,5,6],
#                                 "Columna3":[7,8,9,]})
# print(df)
# print(df.shape)
# nombres = ["columna0", "columna1","columna2"]
# df.columns=nombres
# print(df)








# pd.set_option("display.max_columns", 20)
# df = pd.read_csv("StudentsPerformance.csv")
# print(df)
# print(df.sum(axis=1))