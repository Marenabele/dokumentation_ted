#!/usr/bin/env python
# coding: utf-8

# ### Hier Dokumentiert, was in den einzelnen Schritten gemacht wird. 
# Die restliche Dokumentation wird über Kommentare in den Codeblöcken gemacht. 

# In[1]:


#Die Libraries die gebraucht werden, werden importiert.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import spacy as spacy
from collections import Counter
#Der Datensatz wird als Variable df aus der CSV importiert. 
#In diesem Datensatz werden die Inhalte mit einem Kommata getrennt. 
df = pd.read_csv("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/ted-talks.csv", sep =",")
df

#https://dash.plotly.com/dash-core-components/dropdown


# In[3]:


#Wie viele Autoren gibt es?
count_authors = df["author"].nunique()

#Welche sind die Top Autoren?
#df.value_counts("author", ascending = False).to_frame()
#wurde ausgeklammert, da ich es nun als Variable speichere. Um es zu Stylen muss die Variable 
#als Dataset gespeichert werden, deswegen wird die Serie mit .to_frame umgewandelt.

df_common_author = df.value_counts("author", ascending = False).to_frame(name="Anzahl der Videos")


# In[5]:


#TOP 8 Autoren durchschnittliche Likes
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


# In[16]:


#https://medium.com/plotly/introducing-jupyterdash-811f1f57c02e
#https://blog.finxter.com Cheat Sheet zu Dash
import dash_table
import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#JupyterDash damit die Ausgabe auch schon in VisualCode angezeigt werden kann.
#Starten der App
app = JupyterDash(__name__)

#Gibt das Layout der App an. Bzw. welche Komponenten enthalten sein sollen.
app.layout = html.Div([
    html.H1("TED Talk Explorer"),
    dcc.Dropdown(options=top_8_autoren, value="Alex Gendler", id="dropdown", multi=True),
    dcc.Graph(id="graph"),
    html.Div(id="table")
])

#Für Interaktivitäten des Users
#Verbindet die Dash Komponenten mit Grafiken
#Gibt an, wie die Komponenten mit den Grafiken interagieren.
#Werden aufgerufen, wenn ein Input sich ändert
#Output und Input werden festgelegt
@app.callback(
    Output('table', 'children'),
    [Input("dropdown", "value")]
)
#Updaten des Tables je nach Input-Auswahl
def update_table(dropdown):
    if isinstance(dropdown, str):
        dropdown = [dropdown]
    mask = [a in dropdown for a in df["author"]]
    df_table = df[mask]
    return dash_table.DataTable(df_table.to_dict("records"), [{"name": i, "id": i} for i in df_table.columns])


#Update callback zum Updaten der Grafik
@app.callback(
    Output('graph', 'figure'),
    [Input("dropdown", "value")]
)
def update_figure(dropdown):
    print(dropdown)
    return px.bar(df_top8_likes, x="Durchschnittliche Likes", y="Autor")
#Ausführen der App und Anzeigen der resultate
app.run_server(mode= "inline")

