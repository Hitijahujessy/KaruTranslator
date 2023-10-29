import translators as ts
import pandas as pd

#wordlist_huis = ['Huis', 'Deur', 'Lamp', 'Bed', 'Bank', 'Stoel', 'Televisie', 'Keuken', 'Douche', 'Wc']
#wordlist_dieren = ['Koe', 'Schaap', 'Kip', 'Varken', 'Hond', 'Kat', 'Konijn', 'Eend', 'Muis', 'Paard', 'Ezel', 'Zebra',
            #'Leeuw', 'Tijger', 'Aap', 'Rat', 'Hert', 'Hamster', 'Papegaai', 'Duif', 'Slang',
            #'Krokodil', 'Vis', 'Haai', 'Dolfijn', 'Walvis', 'Orka', 'Giraffe', 'Olifant', 'Neushoorn',
            #'Wolf', 'Beer', 'Vos']
wordlist_huis = ["middag", "avond", "ochtend"]

# All languages that need to be in wordlist
lang_dict = {'English': 'en', 'German': 'de', 'Russian': 'ru', 'Indonesian': 'id', 'French': 'fr', 'Korean': 'ko', 'Japanese': 'ja', 'Spanish': 'es', 'Italian': 'it'}

# Links the words in wordlist to a language. This language should not be in lang_dict since it doesn't need to be translated
# If your wordlist is for example Russian, remove it from lang_dict (or optionally replace it with 'Dutch': 'nl')
data = {'Dutch': wordlist_huis}

# Dataframe will take 'data' as input and turn it into a table.
df = pd.DataFrame(data)

# loop through all languages in 'lang_list'
for x in range(len(lang_dict)):
    # The translated words will be put in this list
    dest_lang_list = []

    # 'index' represents the key (language name) from 'lang_dict'
    index = list(lang_dict.keys())[x]

    # 'current_lang' represents the translator language name, which is the value of the used key from 'lang_dict' in 'index'
    current_lang = lang_dict[index]

    # Print the following string to have a clearer view of where we are while running the code, in case of an error.
    print(f'Creating word list in {index}...\n')

    # Loop in loop to translate all the words in 'wordlist'
    for i in range(len(wordlist_huis)):
        '''
        Try-except block to ensure that all tables are filled. In this case, the value is '*translated word' when succeeded
        and 'NAN' when there's an error. These errors show up a lot when translating to languages like Italian or Spanish, where "Cat"
        could be translated as both "Gato" ad "Gata". This seems to be a Google translate issue, where both translations are outputted as
        two translations, while the code only expects one.
        '''
        try:
            # This variable will become the translated word. It takes a word, from language Dutch, to the current language in the loop.
            translation = ts.translate_text(wordlist_huis[i], translator='google', from_language='nl', to_language=current_lang).capitalize()

            # The translated word will be put in the 'dest_lang_list' variable
            dest_lang_list.append(translation)

            # # Print the following string to have a clearer view of where we are while running the code, in case of an error
            print(f'Entry {(i + 1)} complete.')
        except Exception as e:
            # Print the exception
            print(e)
            # Assign a NAN-value instead, otherwise the dataframe will fail.
            dest_lang_list.append('NAN')

    # All words in the list are translated to one language. It will now be added to the dataframe, and then continue to the next language
    df[index] = dest_lang_list
    print(f'List {(x + 1)} created!\n')

# The dataframe will be converted to a .csv file
df.to_csv('csv_files/wordlist_huis.csv', index=False)
print('File created!')

