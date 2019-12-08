#install  langdetect with pip
import csv
import pandas as pd

from langdetect import detect

data_path = 'C:/Users/strmath/Documents/Datasets/lyrics.csv'
df = pd.read_csv(data_path)
df.shape

# eliminate the needless column 
df.drop(['index', 'song', 'year', 'artist'], axis='columns', inplace=True)
df.shape

# eliminate the NaN row
df.dropna(inplace=True)
df.shape
        
#df_dup.reset_index(inplace=True) - 보류합니다.

# language detection process
f = open('C:/Users/strmath/Documents/Datasets/processed.csv', 'w', encoding='utf-8', newline='')

for i in df.index:
    lyric = df.get_value(i, 'lyrics')
    try:
        lang = detect(lyric)
        if lang == 'en':
            f_writer = csv.writer(f)
            f_writer.writerow([df.get_value(i, 'genre'), df.get_value(i, 'lyrics')])
    except Exception as ex:
        print('error detected', ex)
f.close
