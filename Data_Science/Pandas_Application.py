# Pandas Application

import numpy as np
import pandas as pd
import seaborn as sns

c = np.random.randint(1, 5, size=(2, 3))
print(c, "\n")

df = pd.DataFrame(np.random.randint(1, 10, (2, 2)), index=[0, 1], columns=["A", "B"])
# 데이터 프레임 출력하기
print(df, "\n")
# 컬럼 A의 각 원소가 5보다 작거나 같은지 출력
print(df["A"] <= 5, "\n")
# 컬럼 A의 원소가 5보다 작고, 컬럼 B의 원소가 8보다 작은 행 추출
print(df.query("A <= 5 and B <= 8"))
print('----------------------')
print(df.query("A <= 5 and B <= 8"), "\n")

df_2 = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index=[0, 1], columns=["A", "B", "C", "D"])
print(df_2)
print('----------------')
df_2 = df_2.apply(lambda x: x + 1)
print(df_2, "\n")
print('----------------')

def addOne(x):
  return x + 1

df_2 = df_2.apply(addOne)
print(df_2, "\n")

df_3 = pd.DataFrame([
  ['Apple', 'Apple', 'Carrot', 'Banana'],
  ['Durian', 'Banana', 'Apple', 'Carrot']],
  index=[0, 1],
  columns=["A", "B", "C", "D"])

print(df_3, "\n")
df_3 = df_3.replace({"Apple": "Airport"})
print(df_3, "\n")

df_4 = pd.DataFrame([
  ['Apple', 7, 5, 'Fruit'],
  ['Banana', 3, 6, 'Fruit'],
  ['Beef', 5, 2, 'Meal'],
  ['Kimchi', 4, 8, 'Meal']],
  columns=["Name", "Frequency", "Importance", "Type"])

print(df_4, "\n")
print(df_4.groupby(['Type']).sum(), "\n")

def my_filter(data):
  return data["Frequency"].mean() >= 5

print(df_4.groupby("Type").filter(my_filter), "\n")
print(df_4.groupby("Type").get_group("Fruit"), "\n")

# Pivot table

df_5 = sns.load_dataset('titanic')[['age','sex','class','fare','survived']]
print(df_5.head(), "\n")
pdf_1 = pd.pivot_table(df_5,
                       index = 'class', 
                       columns = 'sex', 
                       values = 'age', 
                       aggfunc = 'mean')
print(pdf_1, "\n")

pdf_2 = pd.pivot_table(df_5,
                       index = 'class',
                       columns = 'sex',
                       values = 'survived',
                       aggfunc = ['mean', 'sum'])
print(pdf_2, "\n")

df_4 = df_4.pivot_table( index = 'Importance',
                        columns = "Type",
                        values = "Frequency",
                        aggfunc = "max"
                        )
print(df_4)