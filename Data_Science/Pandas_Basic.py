# Pandas Basic

import pandas as pd

array = pd.Series(['사과', '바나나', '당근'], index=['a', 'b', 'c'])

print(array)
print(array['a'], "\n")

data = {
    'a': '사과',
    'b': '바나나',
    'c': '당근'
}

# Dict 자료형을 Series로 바꾸기
array_d = pd.Series(data)
print(array_d['a'])
print(array_d, "\n")

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)

# 이름(Name): 값(Values)
summary = pd.DataFrame({
    'word': word,
    'frequency': frequency
})

print(summary, "\n")

data_2 = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data_2, index = ['June', 'Robert', 'Lily', 'David'])
print(purchases, "\n")

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1
}

importance = pd.Series(importance_dict)
summary_2  = pd.DataFrame({
    'word' : word,
    'frequency' : frequency,
    'importance' : importance
})

score = summary_2['frequency'] * summary_2['importance']
summary_2['score'] = score

print(summary_2, "\n")

print(summary_2.loc['Banana' : 'Carrot', 'importance'], "\n")
print(summary_2.iloc[0:3, 1:3], "\n")

print(summary_2, "\n")
summary_2.loc['Apple', 'importance'] = 5
summary_2.loc['Elderberry'] = ['엘더베리', 5, 3, 15]
print(summary_2)