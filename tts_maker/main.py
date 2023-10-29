
import pandas as pd
from gtts import gTTS
import os

df = pd.read_csv('csv_files/wordlist_huis.csv')

lang_dict = {'English': 'en', 'German': 'de', 'Russian': 'ru', 'Indonesian': 'id', 'French': 'fr', 'Korean': 'ko', 'Japanese': 'ja', 'Spanish': 'es', 'Italian': 'it', 'Ambonese': 'id'}



for x in range(len(lang_dict)): # loop through all languages in lang_list

        lang_name = list(lang_dict.keys())[x]

        wordlist = df[lang_name]
        spoken_lang = lang_dict[lang_name]

        print(f'Creating audio files for %s' % lang_name)  # {index}...\n')
        dir_name = './tts_files/langs' + lang_name.lower()
        if not os.path.exists(dir_name):
                os.mkdir(dir_name)

        for i in range(len(df[lang_name])):
                tts = gTTS(wordlist[i], lang=spoken_lang)
                tts.save(dir_name + '/' + wordlist[i] + '.mp3')
                print(f'Entry {(i+1)} complete.')
                print('File created!')
