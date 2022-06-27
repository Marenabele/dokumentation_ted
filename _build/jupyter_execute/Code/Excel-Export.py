#!/usr/bin/env python
# coding: utf-8

# ### Hier Dokumentiert, was in den einzelnen Schritten gemacht wird. 
# Die restliche Dokumentation wird über Kommentare in den Codeblöcken gemacht. 
# Die Codes der Analyse werden aus der "Ted-Talks.ipynb-Datei" kopiert

# In[1]:


#Die Libraries die gebraucht werden, werden importiert.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import spacy as spacy
from collections import Counter
import xlwings as xw
from xlwings import Picture
#Der Datensatz wird als Variable df aus der CSV importiert. 
#In diesem Datensatz werden die Inhalte mit einem Kommata getrennt. 
df = pd.read_csv("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/ted-talks.csv", sep =",")
df


# ##### Erster Tab mit dem origianelen Dataframe

# In[4]:


#Neue Excel-Datei erstellen 
#Datei Speichern 
#book.save("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Excel_Export.xlsx")

book = xw.Book("Excel_Export.xlsx")

#Neuen Tabs in der Datei erstellen. Zugriff auf die Tabs via Namen
sheet1 = book.sheets["Kompletter Datensatz"]
sheet2 = book.sheets["Häufigkeit Autoren"]
sheet3 = book.sheets["Häufigkeit Jahre"]
sheet4 = book.sheets["Häufigkeit Monat und Jahr"]
sheet5 = book.sheets["Autoren Likes"]
sheet6 = book.sheets["Autoren Views"]
sheet7 = book.sheets["Talks nach Likes"]
sheet8 = book.sheets["Talks nach View"]
sheet9 = book.sheets["Keywords"]

#Allgemeinen Datensatz importieren
df_start = pd.read_csv("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/ted-talks.csv", sep =",")
df_start

#Tab eins mit dem allgemeinen Datensatz füllen
sheet1["A1"].value = df_start


# ##### 2. Tab mit der Häufigkeiten der Autoren

# In[5]:


df_common_author = df.value_counts("author", ascending = False).to_frame(name="Anzahl der Videos")

#Tab 2 mit der Liste an Autren füllen
sheet2["A1"].value = df_common_author


# ##### 3. Tab mit den Videos pro Jahr

# In[15]:


#Datums-Spalte konvertieren und die Jahre zählen
from datetime import datetime, timedelta
df["date"] = pd.to_datetime(df["date"])

df["year"]= df["date"].dt.year
df["month"]= df["date"].dt.month

df_year = df

df_count_years = df_year.value_counts("year", ascending = False).to_frame(name= "Videos pro Jahr")

#Tab 3 mit der Liste an Jahren und Häufigkeiten füllen
sheet3["A1"].value = df_count_years

#Grafik hinzufügen
#https://docs.xlwings.org/en/stable/api.html#xlwings.main.Pictures.add
sheet3.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Verteilung_allerVideos.png", top=rng.top, left=rng.left)



# ##### 4. Tab mit den Videos pro Monat und Jahr

# In[23]:


#Zählen der Monate und Jahre
df_count_month_and_year = df.value_counts("date", ascending = False).to_frame(name="Anzahl der Videos")

#Grafik hinzufügen
#https://docs.xlwings.org/en/stable/api.html#xlwings.main.Pictures.add
rng = book.sheets["Häufigkeit Monat und Jahr"].range("A204")

#Tab 4 mit der Liste füllen und die Grafiken ergänzen
sheet4["A1"].value = df_count_month_and_year
sheet4.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/2017_Monate.png", top=rng.top, left=rng.left)

rng= book.sheets["Häufigkeit Monat und Jahr"].range("G204")
sheet4.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Monat_2018.png", top=rng.top, left=rng.left)
rng= book.sheets["Häufigkeit Monat und Jahr"].range("A217")
sheet4.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Monat_2019.png", top=rng.top, left=rng.left)
rng= book.sheets["Häufigkeit Monat und Jahr"].range("G217")
sheet4.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Monat_2020.png", top=rng.top, left=rng.left)
rng= book.sheets["Häufigkeit Monat und Jahr"].range("A230")
sheet4.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Monat_2021.png", top=rng.top, left=rng.left)


# ##### 5. Tab 8 Häufigsten Autoren und die durchschnittlichen Likes

# In[29]:


mask = (df["author"] == "Alex Gendler") | (df["author"] == "Iseult Gillespie") | (df["author"] == "Matt Walker	") | (df["author"] == "Alex Rosenthal") | (df["author"] == "Elizabeth Cox") | (df["author"] == "Emma Bryce") | (df["author"] == "Daniel Finkel") | (df["author"] == "Juan Enriquez") 
df_author_likes = df[mask]

top_8_autoren = ["Alex Gendler", "Iseult Gillespie", "Matt Walker", "Alex Rosenthal", "Elizabeth Cox", "Emma Bryce",
                 "Daniel Finkel", "Juan Enriquez"]

author_agg = dict()

for author in top_8_autoren:
    mask = df["author"] == author
    author_agg[author] = df[mask]["likes"].mean().__round__()
author_agg

#https://stackoverflow.com/questions/20340844/pandas-create-named-columns-in-dataframe-from-dict

df_top8_likes = pd.DataFrame(list(author_agg.items()),
                      columns=["Autor", "Durchschnittliche Likes"])

#df_top8_likes = pd.DataFrame.from_dict(author_agg, orient="index")
df_top8_likes

rng = book.sheets["Autoren Likes"].range("A12")
#Tab 5 mit Liste füllen
sheet5["A1"].value = df_top8_likes

#Grafik hinzufügen
#https://docs.xlwings.org/en/stable/api.html#xlwings.main.Pictures.add
sheet5.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Autoren_Likes.png", top=rng.top, left=rng.left)


# ##### 6. Tab 8 Häufigsten Autoren und die durchschnittlichen Views

# In[30]:


mask = (df["author"] == "Alex Gendler") | (df["author"] == "Iseult Gillespie") | (df["author"] == "Matt Walker	") | (df["author"] == "Alex Rosenthal") | (df["author"] == "Elizabeth Cox") | (df["author"] == "Emma Bryce") | (df["author"] == "Daniel Finkel") | (df["author"] == "Juan Enriquez") 
df_author_views = df[mask]

top_8_autoren = ["Alex Gendler", "Iseult Gillespie", "Matt Walker", "Alex Rosenthal", "Elizabeth Cox", "Emma Bryce",
                 "Daniel Finkel", "Juan Enriquez"]

author_agg = dict()

for author in top_8_autoren:
    mask = df["author"] == author
    author_agg[author] = df[mask]["views"].mean().__round__()
author_agg

df_top8_views = pd.DataFrame(list(author_agg.items()),
                      columns=["Autor", "Durchschnittliche Views"])
df_top8_views

rng = book.sheets["Autoren Views"].range("A12")
#Tab 6 mit Liste befüllen
sheet6["A1"].value = df_top8_views
#Grafik hinzufügen
#https://docs.xlwings.org/en/stable/api.html#xlwings.main.Pictures.add
sheet6.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Autoren_Views.png", top=rng.top, left=rng.left)


# ##### 7. Tab Talks nach Likes

# In[37]:


df_video_likes_max = df.sort_values("likes", ascending = False)

#Tab 7 mit sortieretem Datensatz füllen
sheet7["A1"].value = df_video_likes_max


# ##### 8. Tab Talks nach Views

# In[39]:


df_video_views_max = df.sort_values("views", ascending = False)

#Tab 8 mit sortiertem Datensatz füllen
sheet8["A1"].value = df_video_views_max


# ##### 9. Tab Keywords

# In[31]:


import spacy as spacy
from collections import Counter

df_title = df["title"]

from spacy.lang.en.examples import sentences
nlp = spacy.load("en_core_web_md")
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
import re

df["txt"] = [nlp(text) for text in df.title]

#Wie viele Wörter haben alle Titel zusammen
all_words = []
for text in df.txt:
    wordrow = [word.text for word in text]
    all_words.extend(wordrow)

word_freq = Counter(all_words)

common_words = word_freq.most_common(50)

#Wir wollen häufig vorkommende Wörter, die nichts über den Sinn aussagen, wie "the", "a" oder Satzzeichen rausstreichen
#Text säubern von Sonderzeichen, Satzzeichen und Emojis
def clean_text(text):
    if isinstance((text), (str)):
        text = re.sub('<[^>]*>', '', text)
        text = re.sub('[\d]+', '', text.lower())
        text = re.sub('"', '', text.lower())
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        text = re.sub('\'','', text)
        return text
    if isinstance((text), (list)):
        return_list = []
        for i in range(len(text)):
            temp_text = re.sub('<[^>]*>', '', text[i])
            temp_text = re.sub('[\d]+', '', temp_text.lower())
            temp_text = re.sub('"', '', temp_text.lower())
            temp_text = re.sub('\[.*?\]', '', temp_text)
            temp_text = re.sub('https?://\S+|www\.\S+', '', temp_text)
            temp_text = re.sub('<.*?>+', '', temp_text)
            temp_text = re.sub('\n', '', temp_text)
            temp_text = re.sub('\w*\d\w*', '', temp_text)
            temp_text = re.sub('\'','', temp_text)
            return_list.append(temp_text)
        return(return_list)
    else:
        pass

#Füllwörter entfernen
def remove_stopwords(text):
    wordrow = [word for word in text if word.is_stop != True and word.is_punct != True]
    return wordrow

# Wörter zählen, die zurück gegeben werden
def wordcounter(text):
    freq = len(text)
    return freq

#Dem Datensatz werden neue Spalten hinzugefügt. Die gefilterten Wörter, die Wörter als Keywords, wie viele Wörter es gesäubert sind und wie viele Wörter gestrichen wurden.
df["keywords"] = df['title'].apply(lambda x : clean_text(x))
df["keywords"] = [nlp(text) for text in df.keywords]

df["keywords"] = df["keywords"].apply(lambda x : remove_stopwords(x))
df['word_numb_orig'] = df['txt'].apply(lambda x : wordcounter(x))
df['word_numb_cleaned'] = df["keywords"].apply(lambda x : wordcounter(x))

#Alle Wörter angezeigt bekommen
#Wie viele Wörter, die nur min. 1x vorkommen es gibt
#Welche die meist vorkommenden Wörter sind. 
all_words = []
for text in df.keywords:
    wordrow = [word.text for word in text if word.is_stop != True and word.is_punct != True and word.text != ' ']
    all_words.extend(wordrow)

# word count
word_freq = Counter(all_words)

word_count_clean = len(all_words)
unique_words_clean = len(word_freq)
common_words = word_freq.most_common()

#Tab 9 füllen
sheet9["A1"].value = common_words

rng = book.sheets["Keywords"].range("D5")
#Grafik hinzufügen
#https://docs.xlwings.org/en/stable/api.html#xlwings.main.Pictures.add
sheet9.pictures.add(r"/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/wordcloud.png", top=rng.top, left=rng.left)


# ##### Quellen:
# * [https://docs.xlwings.org/en/stable/api.html#xlwings.main.Pictures.add](https://docs.xlwings.org/en/stable/api.html#xlwings.main.Pictures.add)
# * [https://www.youtube.com/watch?v=5iyL9tMw8vA](https://www.youtube.com/watch?v=5iyL9tMw8vA)
