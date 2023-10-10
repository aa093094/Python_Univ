# This program is about plotting two classics(Adventures of Huckleberry Finn and Little Women) by using numpy, pandas and pyplot
# PlottingClassic1 is about huck_finn.

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

df = pd.DataFrame({'Chapters': huck_finn_chapters})
print(df)

counts = pd.DataFrame({'Jim': np.char.count(huck_finn_chapters, 'Jim'), 'Tom': np.char.count(huck_finn_chapters, 'Tom'), 'Huck': np.char.count(huck_finn_chapters, 'Huck')})
cum_counts = counts.cumsum()
cum_counts.plot.line(figsize = (10,5))

plt.title('Cumulative Mention Counts of Characters in Huck Finn')
plt.xlabel('Chapter')
plt.ylabel('Cumulative Counts')
plt.legend(['Jim', 'Tom', 'Huck'])
plt.grid(True)
plt.show()
