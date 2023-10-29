<h1 align="center">KaruTranslator</h1>

<p align="center">
  KaruTranslator is a simple CLI application that I have created to create wordlists for (Karu)[https://github.com/Hitijahujessy/karu-app] without spending too much time finding
  translations for the different languages. It also includes another simple application that creates text-to-speech .mp3 files for all
  of the translations.
</p>

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features
- Write a wordlist in a language of your choice, and let the app translate it to any language available on Google Translate.
- Translates the wordlist to as many languages needed in one go, and save it all to a .csv file
- Use the text-to-speech application (```./tts_maker/main.py```) to create text-to-speech audio files for all entries in the .csv file

## Installation
Use the following command to install all libraries used for this project.

```pip install -r requirements.txt```

## Usage

### KaruTranslator
Open ```main.py``` with your IDE of choice. On line 4 is the default/example list called ````wordlist_numbers```. This list may be used,
or replaced with another list. 

If replaced with another language, please change ````data = {'English': wordlist_numbers}``` (line 11) to 
````data = {'LANGUAGE NAME': WORDLIST NAME}```. Also replace all instances of ```wordlist_numbers``` (lines 31, 40, 58) to the new wordlist name,
and also on line 40, replace ```from_language='en'``` with the translator language (i.e. for French use ```fr```).

Run ```main.py``` and the translation process will start. The words will be translated per language, saved to dest_lang list, and will be appended to 
a DataFrame after all of the words are translated. This process will be repeated until the wordlist is translated to every specified language. This may 
all take a while, depending on the amount of words in the wordlist and the amount of specified languages. When the process is complete, the DataFrame will
be saved as a .csv file in the ```csv_files``` directory.

### TTS_Maker
It's also possible to create text-to-speech files for the entire .csv file. To do this, open ```tts_maker/main.py``` and change ```df = pd.read_csv('csv_files/wordlist_numbers.csv')```
to ```df = pd.read_csv('csv_files/your_wordlist_filename.csv')```. Run ```tts_maker/main.py``` and all of the text-to-speech files will be created and saved as .mp3 files in the ```tts_files```
directory.

### Not optimized
The applications are not that optimized because they were created during the beginning stages of Karu app and I didn't know too much abouy Python programming at that time. Maybe I will update
the apps sometime to make the process easier and faster, but it's not a priority of mine right now.

