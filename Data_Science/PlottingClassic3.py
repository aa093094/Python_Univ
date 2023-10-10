# PlottingClassic3 is about showing number of periods and number of characters in chapter of two classics.

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

chars_periods_huck_finn = pd.DataFrame({'Huck Finn Chapter Length': (len(s) for s in huck_finn_chapters), 'Number of Periods': np.char.count(huck_finn_chapters, '.')})

chars_periods_little_women = pd.DataFrame({'Little Women Chapter Length': (len(s) for s in little_women_chapters), 'Number of Periods': np.char.count(little_women_chapters, '.')})

plt.figure(figsize=(6, 6))
plt.scatter(chars_periods_huck_finn['Number of Periods'],
              chars_periods_huck_finn['Huck Finn Chapter Length'],
              color='darkblue')
plt.scatter(chars_periods_little_women['Number of Periods'],
              chars_periods_little_women['Little Women Chapter Length'],
              color='gold')
plt.xlabel('Number of periods in chapter')
plt.ylabel('Number of characters in chapter')
plt.grid(True)
plt.show()


