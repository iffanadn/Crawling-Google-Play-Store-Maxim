# -*- coding: utf-8 -*-
"""scrapping_googleplay.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mu1uHDSIpep5D-EGTKVOpnKEFC3d1l5y
"""

!pip install google_play_scraper

# Scrape All available reviews
# untuk mengambil semua review
from google_play_scraper import Sort, reviews_all
import pandas as pd

scrapreview = reviews_all(
    'com.taxsee.taxsee',  # ID aplikasi bisa cek di https://play.google.com/
    lang='id',  # defaults to ‘en’
    country='id',  # defaults to ‘us’
    sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
    filter_score_with=2  # defaults to None (means all score)

)

print(scrapreview)
app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.to_csv('dataset_gplay3.csv', index=None, header=True)

#SCRAPPING DATASET YANG RELEVAN

#Scrape desired number of reviews
#Run kode ini jika ingin scrape data dengan jumlah tertentu. Ganti (misal, ingin scrape sejumlah 1000, maka ganti kode , count = 1000 )
!pip install google_play_scraper

from google_play_scraper import Sort, reviews
import pandas as pd

result, continuation_token = reviews(
    'com.taxsee.taxsee',
    lang='id', # defaults to 'en'
    country='id', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT you can use Sort.NEWEST to get newst reviews
    count=50000, # defaults to 100
    filter_score_with=None # defaults to None(means all score) Use 1 or 2 or 3 or 4 or 5 to select certain score
)

print(result)
app_reviews_df = pd.DataFrame(result)
app_reviews_df.to_csv('dataset_gplayID.csv', index=None, header=True)

#scrapping DATASE TERBARU
!pip install google_play_scraper

from google_play_scraper import Sort, reviews
import pandas as pd

result, continuation_token = reviews(
    'com.taxsee.taxsee',
    lang='id', # defaults to 'en'
    country='id', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT you can use Sort.NEWEST to get newst reviews
    count=50000, # defaults to 100
    filter_score_with=None # defaults to None(means all score) Use 1 or 2 or 3 or 4 or 5 to select certain score
)

print(result)
app_reviews_df = pd.DataFrame(result)
app_reviews_df.to_csv('dataset_gplayID.csv', index=None, header=True)

