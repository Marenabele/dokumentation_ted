# Datenauswertung & Datenselektion mit Pandas
Bevor ich die Daten visualisieren kann, müssen diese Daten zunächst einmal ausgewertet werden. Hierfür habe ich mir bevor ich angefangen habe, Gedanken dazu gemacht, was ich aus den Daten für Erkenntnisse ziehen kann und welche davon für das Dashboard und den Report wichtig sind.

Hierzu habe ich die Vorgehensweise der Vorlesungsfolien angewandt. 
1. Brainstorming
2. Edit
3. Get Feedback

Wobei ich mir beim 3. Schritt selbst nochmal klar gemacht habe, ob das Vorgehen und die ausgewählten Daten Sinn machen und ob ich alles erklären kann. 

Die Aufgaben können in die 6 Kategorien aus den Vorlesungsfolien eingeteilt werden. So kann die Reihenfolge ebenfalls noch einmal angepasst werden. Ich habe die Reihenfolge der Vorgehensweise aber bereits während des Brainstormings angepasst, da ich es für mein Vorgehen passender fand. 

![Vorgehensweise](/Users/marenabele/datastorytelling_newbook/Data_Storytelling_TED/Bild_7.png)
Quelle: Nussbaumer Knaflic, 2020 in Kirenz, J. (2021–09-28). Data Storytelling. 1. The importance of context.[Vorlesungsfolien]. Github Slides. [https://github.com/kirenz/data-storytelling/blob/main/slides/L01_context.pdf](https://github.com/kirenz/data-storytelling/blob/main/slides/L01_context.pdf) [Stand: 11.06.2022]

**Data:**
* Da diese Abgabe nicht im Unternehmenskontext erstellt wird, wurde ein Datensatz von Kaggle zu einem von mir als interessant angesehenen Thema gewählt.
* Dazu können Sie nochmal den Beitrag [“Einleitung”](/Users/marenabele/datastorytelling_newbook/Data_Storytelling_TED/Einleitung.md) und Beitrag [“Gewählter Datensatz”](/Users/marenabele/datastorytelling_newbook/Data_Storytelling_TED/Gewählter_Datensatz.md) lesen.

**Problem Statement:**
* Das Problem Statement wurde mit Hilfe des Big Idea Worksheet bereits herausgearbeitet. Dazu können Sie nochmal den Beitrag [“Big Idea Worksheet”](/Users/marenabele/datastorytelling_newbook/Data_Storytelling_TED/Bid_Idea_Worksheet.md) lesen. 
* Die finale Big Idea lautet wie folgt: “Durch die Erstellung eines Dashboards soll die User Experience der Fans gesteigert werden und die Verantwortlichen zusätzlich neue Erkenntnisse über bereits veröffentlichte Talks erhalten.”

**Background:**
* Wissenswertes über TED (siehe Beitrag [“TED Talks”](/Users/marenabele/datastorytelling_newbook/Data_Storytelling_TED/TED_Talks.md))
* Wissenswertes über den Datensatz
    * Woher stammt der Datensatz → Bezug auf Data
    * Wie viele Videos gibt es insgesamt im Datensatz?
    * Von wann ist das erste Video des Datensatzes?
    * Von wann ist das letzte Video des Datensatzes?
    * In welchem Jahr wurden die meisten TED Talks veröffentlicht?
    * Wie viele Autoren gibt es?
    * Wie hoch ist die durschnittliche Like-Anzahl?
    * Was hoch ist die durschnittliche View-Anzahl?
    * Welches ist das Video mit den meisten Likes?
    * Welches ist das Video mit den wenigsten Likes?

**Analysis:**
* In welchem Monat und Jahr kamen die meisten Ted Talks heraus?
* Wie viele Videos wurden über die Jahre jährlich veröffentlicht?
* Korrelation zwischen Views und Likes
* Welche Keywords können aus den Titeln der Talks abgeleitet werden?
* Wie häufig kommen diese Keywords in den Titeln der Talks vor?

**Recommendation:**
* Autoren mit einer hohen Like-Anzahl häufiger einsetzen.
* Die Verhältnisse zwischen Views und Likes für die Videos anzeigen, damit dem Suchenden direkt ein Prozentsatz angezeigt wird. So ist es für die Suchenden besser einzuordnen.
* Häufige Keywords visualisieren, damit die Suchenden ein besseres Gefühl für diese bekommen. 

**Findings:**
* Die Findings werden nach allen Schritten im Report dargelegt, da alle Schritte erst durchlaufen worden sein müssen um die Findings zu kennen. 

Die Dokumentation der eigentlichen Auswertung finden Sie in dem Jupyter Notebook im Github Repository. Hier wurden die Schritte in der Datei kommentiert. 

### Quellen:
Nussbaumer Knaflic, 2020 in Kirenz, J. (2021–09-28). Data Storytelling. 1. The importance of context.[Vorlesungsfolien]. Github Slides. [https://github.com/kirenz/data-storytelling/blob/main/slides/L01_context.pdf](https://github.com/kirenz/data-storytelling/blob/main/slides/L01_context.pdf) [Stand: 11.06.2022]