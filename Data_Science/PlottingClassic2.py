# PlottingClassic2 is about little_women.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

try:
    huck_finn_url = 'https://www.inferentialthinking.com/data/huck_finn.txt'
    huck_finn_text = requests.get(huck_finn_url)
    #print("HTML:\n", huck_finn_text.text)
except:
    print("Invalid huck_finn_url or some error occured while making the GET request to the specified huck_finn_url")

huck_finn_chapters = huck_finn_text.text.split('CHAPTER ')[44:]

try:
    little_women_url = 'https://www.inferentialthinking.com/data/little_women.txt'
    little_women_text = requests.get(little_women_url)
    #print("HTML:\n", huck_finn_text.text)
except:
    print("Invalid little_women_url or some error occured while making the GET request to the specified little_women_url")

little_women_chapters = little_women_text.text.split('CHAPTER ')[1:]

df2 = pd.DataFrame({'Chapters': little_women_chapters})
print(df2)

counts2 = pd.DataFrame({'Amy': np.char.count(little_women_chapters, 'Amy'), 'Beth': np.char.count(little_women_chapters, 'Beth'), 'Jo': np.char.count(little_women_chapters, 'Jo'), 'Meg': np.char.count(little_women_chapters, 'Meg'), 'Laurie': np.char.count(little_women_chapters, 'Laurie')})
cum_counts2 = counts2.cumsum()
cum_counts2.plot.line(figsize = (10,5))

plt.title('Cumulative Mention Counts of Characters in Little Women')
plt.xlabel('Chapter')
plt.ylabel('Cumulative Counts')
plt.legend(['Amy', 'Beth', 'Jo', 'Meg', 'Laurie'])
plt.grid(True)
plt.show()
