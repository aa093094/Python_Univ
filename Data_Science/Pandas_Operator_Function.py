# Pandas Operator Function

import pandas as pd
import numpy as np

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': np.nan,
    'Durian': 2
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

print(summary, "\n")
print(summary.notnull(), "\n")
print(summary.isnull(), "\n")
summary['frequency'] = summary['frequency'].fillna('데이터 없음')
print(summary, "\n")

array1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])

array3 = array1.add(array2, fill_value=10)
print(array3, "\n")

array1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])

print(array1)
print(array2)
print('-----------------')
array = array1.add(array2)
print(array)
print('-----------------')
array = array1.add(array2, fill_value=0)
print(array)
print('-----------------')
print(array.sum(), "\n")

array3 = array1.add(array2, fill_value=0)
print(array3, "\n")
print("컬럼 1의 합:", array3[1].sum(), "\n")
print(array3.sum(), "\n")

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 1,
    'Durian': 2
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

print(summary, "\n")
summary = summary.sort_values('frequency', ascending=False)
print(summary)