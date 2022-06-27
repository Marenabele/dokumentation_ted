#!/usr/bin/env python
# coding: utf-8

# ### Hier Dokumentiert, was in den einzelnen Schritten gemacht wird. 
# Die restliche Dokumentation wird über Kommentare in den Codeblöcken gemacht. 

# In[1]:


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.graphics import shapes
from reportlab.graphics import charts
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing
import pandas as pd


#Page-Layout imports
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, BaseDocTemplate, Frame, PageBreak, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, landscape 
import random
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Frame, Paragraph, Table, TableStyle

breite, hoehe = landscape(A4)
styles = getSampleStyleSheet

#https://www.youtube.com/watch?v=ZDR7-iSuwkQ
#https://www.reportlab.com/docs/reportlab-userguide.pdf

#Inhalt als Variable speichern, um daraug zurückzugreifen
pdf_name = "TED-Talk-Explorer-Report_reportlab.pdf"
pdf_title= "TED Talk Explorer - Report"
img_head = "/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/report_head.png"
img_header = "/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/header_logo.png"
img_ted_logo = "/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/logo_ted.gif"
cover_page_txt = ["In diesem Report werden die Ergebnisse der" , 
"Datenanalyse mit Grafiken detallieter dargestellt und erläutert."]

#Help für das Ausrichten
#https://www.youtube.com/watch?v=ZDR7-iSuwkQ
def drawMyRuler(pdf):
    pdf.drawString(100, 810, "x100")
    pdf.drawString(200, 810, "x200")
    pdf.drawString(300, 810, "x300")
    pdf.drawString(400, 810, "x400")
    pdf.drawString(500, 810, "x500")

    pdf.drawString(10, 100, "y100")
    pdf.drawString(10, 200, "y200")
    pdf.drawString(10, 300, "y300")
    pdf.drawString(10, 400, "y400")
    pdf.drawString(10, 500, "y500")
    pdf.drawString(10, 600, "y600")
    pdf.drawString(10, 700, "y700")
    pdf.drawString(10, 800, "y800")


# In[1343]:


#Cover-Page kreieren
#Das Raster wird auskommentiert, sobald die Seite fertig gestellt wurde
#drawMyRuler(pdf)

pdf = canvas.Canvas(pdf_name)

pdf.setTitle(pdf_title)
pdf.drawInlineImage(img_head, 0, 700, width=600, height=150)
pdf.setFillColor("#FF2B06")
pdf.setFont("Helvetica-Bold", 40)
pdf.drawString(50,650, pdf_title)
pdf.drawInlineImage(img_ted_logo, 100, 390, width=400, height=200)
pdf.setFont("Helvetica", 18)
pdf.setFillColor("#00000")
pdf.drawCentredString(300,325, "In diesem Report werden die Ergebnisse") 
pdf.drawCentredString(300,305, "der Datenanalyse mit Grafiken detallieter") 
pdf.drawCentredString(300,285, "dargestellt und erläutert.")
pdf.showPage()


# In[1344]:


#2 Seite 

#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 1 von 9")

#Überschrift 
pdf.setFont("Helvetica", 16)
pdf.setFillColor("#FF2B06")
pdf.drawString(32, 765, "1. Wissenswertes über den Datensatz")

#TEXT
#https://wiki.ubuntuusers.de/ReportLab/
style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 26*cm)
story.append(Paragraph("TED steht für Technology, Entertainment und Design. Der Name geht  auf die Anfangszeiten zurück, als TED noch eine Konferenz für die im Namen vorkommenden Themen war. Die erste TED Konferenz fand im Jahr 1984 statt. Später wurden die Vorträge beziehungsweise kurzen Talks (Vorträge) auf der Webseite kostenlos zur Verfügung gestellt. Heute findet man eine Vielzahl an Vorträgen zu vielen Themengebieten. TED Talks finden nicht nur zu den ursprünglichen Themen statt. Außerdem gibt es die Vorträge inzwischen in 110 Sprachen.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 23.5*cm)
story.append(Paragraph("Für diesen Report wurden Daten aus einem Kaggle Datensatz verwendet. Der Ersteller des Datensatzes heißt Ashish Jangra und ist ein Entrepreneur und KI Trainer in Indien. In der Beschreibung des Datensatzes steht zudem, wie Herr Jangra die Daten zusammengestellt hat. Er hat dafür die Webseite von TED gecrawlt und sich die Daten gezogen, die er in den Datensatz packen wollte. Der Datensatz besteht aus den Variablen: Titel, Autor, Datum, Views, Likes und Links. Auf Grundlage dieser Variablen und Daten wurden Untersuchungen vorgenommen.", style["BodyText"]))
frame.addFromList(story, pdf)

pdf.setFont("Helvetica", 16)
pdf.setFillColor("#FF2B06")
pdf.drawString(32, 600, "2. Verteilung der Videos")

frame = Frame(1*cm, 1*cm, breite-(11*cm), 20.2*cm)
story.append(Paragraph("Der Datensatz besteht aus insgesamt 5440 Videos.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO 
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Verteilung_allerVideos.png", 32, 320, width = 400, height=250)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 10.2*cm)
story.append(Paragraph("Diese Videos wurde über die Jahre 1970 bis 2022 veröffentlicht. Wie die Grafik zeigt, sind es in den Jahren ab 1970 bis ca. 2022 nur vereinzelte Videos. Ab 2002 sieht man einen deutlichen Anstieg an Videos pro Jahr. Was sich natürlich durch das Internet und die steigende Bekanntheit über die USA heraus erklären lässt. Die erste TED Konferenz fand 1984 statt, deswegen ist zu hinterfragen, was es mit den Videos vor diesem Jahr auf sich hat. Sind diese Talks im nachhinein auf die Webseite gestellt worden? Evtl. gibt es noch ein Video aus dieser Zeit, das zu der Idee der TED Konferenz geführt hat. Diese Videos könnten auch Fehler im System aufweisen und falsch datiert worden sein.", style["BodyText"]))
frame.addFromList(story, pdf)


frame = Frame(1*cm, 1*cm, breite-(11*cm), 7.0*cm)
story.append(Paragraph("Das erste Video des Datensatzes ist auf Januar 1970 und das letzte Video des Datensatzes auf Februar 2022 datiert.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 5.9*cm)
story.append(Paragraph("Im Jahr 2019 wurden 544 Videos veröffentlicht. Hier sieht man auch in der Grafik den höchsten Punkt. Gefolgt von den Jahren 2020 mit 501 und 2017 mit 495 Videos.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 4.8*cm)
story.append(Paragraph("Dies zeigt, dass die meisten Videos in den letzten Jahren veröffentlicht wurden. Deswegen werden nun die Veröffentlichungen der letzten 5 Jahre aufgeschlüsselt.", style["BodyText"]))
frame.addFromList(story, pdf)

pdf.showPage()


# In[1345]:


#Seite 2
#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 2 von 9")

#FOTO 
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/letzten5Jahre-kompletterDurchschnitt.png", 32, 520, width = 400, height=250)

#TEXT
style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 17.5*cm)
story.append(Paragraph("Die rote Linie zeigt den Durchschnitt der Videos über den kompletten Datensatz. Zieht man alle Jahre heran, wurden durchschnittlich 181 Videos veröffentlicht. Dieser Durchschnitt wurde in den letzten 5 Jahren immer deutlich übertroffen. Dieser Fakt ist nicht weiter verwunderlich, wenn drei dieser 5 Jahre zu den Jahren mit den meisten veröffentlichten Videos gehört.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 15.5*cm)
story.append(Paragraph("Deswegen schauen wir uns diese 5 Jahre noch mal etwas genauer an. Zieht man nämlich den durchschnitt dieser 5 Jahre heran, steigt dieser auf 481 Videos pro Jahr. So fällt auf, dass die drei Top Jahre über dem Durchschnitt liegen. 2018 ist etwas schwächer, kratzt aber noch an dem Durchschnitt. Es fällt jedoch auf, dass 2021 deutlich schwächer ist, als die Jahre davor. Es wurden weniger Talks veröffentlicht. Hierfür könnte ein möglicher Grund die Corona-Pandemie sein. Es mussten Maßnahmen eingehalten werden und es durften keine Großveranstaltungen stattfinden. Meistens werden TED Talks vor einem Live-Publikum aufgenommen. Deswegen könnte es hier zu einem Abfall der Veröffentlichungen gekommen sein.", 
style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO 
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/letzte5jahre-durchschnitt5.png", 32, 110, width = 400, height=250)


pdf.showPage()


# In[1346]:


#Seite 3
#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 3 von 9")

#Überschrift 
pdf.setFont("Helvetica", 16)
pdf.setFillColor("#FF2B06")
pdf.drawString(32, 765, "3. Likes und Views")

#TEXT
style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 26*cm)
story.append(Paragraph("Zwei weitere Variablen zum detaillierten Analysieren der Talks sind die Likes und Views der Videos. Zieht man alle 5440 des Datensatzes heran ergibt es eine durchschnittliche Like-Anzahl von 62.608 Likes pro Video.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 25*cm)
story.append(Paragraph("Die Top 3 Videos mit den häufigsten Likes sind “Do schools kill creativity?” von Sir Ken Robinson, “Your body language may shape who you are” von Amy Cuddy und “Inside the mind of a master procrastinator” von Tim Urban. Diese Videos liegen mit 2.100.000, 1.900.000 und 1.800.000 weit über den durchschnittlichen Werten der Likes.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 23.5*cm)
story.append(Paragraph("Die schlechtesten Videos gemessen an den Likes sind “Year In Ideas 2015” von unbekannt, “Post-Pandemic Paradise in Rapa Nui” von Far Flung und “Virtual Worlds” von Far Flung. Mit 15, 37 und 39 Likes sind diese Videos weit vom Durchschnitt entfernt.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 21.5*cm)
story.append(Paragraph("Die durschnittliche View-Anzahl liegt bei 2.061.576 Aufrufen pro Video. Auch hier werden wieder die Top und die Flop Videos angeschaut. Mit 72.000.000, 64.000.000 und 60.000.000 Aufrufen sind es genau die gleichen Top 3 Videos gemessen an den Likes. Die schlechtesten 3 Videos gemessen an den Likes haben ebenfalls die schlechtesten Aufruf-Zahlen. Mit 532, 1200 und 1300 Aufrufen liegen diese Videos auch weit unter diesem Durchschnitt.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 19.5*cm)
story.append(Paragraph("Aufgrund dieser Erkenntnisse kann man annehmen, dass es eine Korrelation zwischen Likes und Views gibt. ", style["BodyText"]))
frame.addFromList(story, pdf)

pdf.setFont("Helvetica-Bold", 10)
pdf.setFillColor("#FF2B06")
pdf.drawString(34, 537, "Korrelation")

frame = Frame(1*cm, 1*cm, breite-(11*cm), 17.8*cm)
story.append(Paragraph("Errechnet man den Korrelationskoeffizienten zwischen Views und Likes liegt dieser bei 0.99. Der Korrelationskoeffizient ist eine Einheit für den Grad eines linearen Zusammenhangs. Bei +1 besteht ein perfekter linearer Zusammenhang zwischen den zwei Variablen. Mit 0.99 ist der Zusammenhang zwischen den Views und Likes nahezu perfekt. Dies lässt sich auch gut in der Grafik erkennen.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO 
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/korrelation.png", 32, 105)


frame = Frame(1*cm, 1*cm, breite-(11*cm), 2.5*cm)
story.append(Paragraph("Eine gute Ergänzung zum Datensatz wäre eine Like-Quote, die das Verhältnis zwischen Views und Likes direkt angibt. So muss man nicht erst selbst ausrechnen, wie vielen Zuschauern das Video gefallen hat. Das beste Verhältnis sind 36.4%, das schlechteste sind 30.4%. Dies zeigt, dass rund einem Drittel der Zuschauer das Video auch gefällt.", style["BodyText"]))
frame.addFromList(story, pdf)

pdf.showPage()


# In[1347]:


#Seite 4
#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 4 von 9")

#Überschrift 
pdf.setFont("Helvetica", 16)
pdf.setFillColor("#FF2B06")
pdf.drawString(32, 765, "4. Keywords")

style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 26*cm)
story.append(Paragraph("Da es diese Vielzahl an Videos gibt, die auch aus verschiedensten Themengebieten stammen, wurden die Titel genauer analysiert. Die Titel bestehen aus insgesamt 41.645 Wörtern. Wenn man die gleichen Wörter zählt, kommt man auf 7.160. In diesen Wörtern sind die Top Wörter, solche wie “the”, “of”, “how”, “to”. Diese Wörter sagen allerdings nichts über den Inhalt des Videos aus. Diese Wörter werden aussortiert.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO 
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/wordcloud.png", 29, 515)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 17*cm)
story.append(Paragraph("Die Top 10 Wörter in den Titeln sind dann life, world, new, future, change, work, help, climate, art und need. Diese Wörter sind auch gut in der Word Cloud sichtbar, da diese die Häufigkeit der Wörter mit einbezieht und dadurch die Größe der Wörter bestimmt.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Tabelle_Wörter.png", 30, 10, width=300, height=450)

pdf.showPage()


# In[1348]:


#Seite 5
#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 5 von 9")

#Überschrift 
pdf.setFont("Helvetica", 16)
pdf.setFillColor("#FF2B06")
pdf.drawString(32, 765, "5. Autoren")

style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 26*cm)
story.append(Paragraph("Die TED Talks wurden von 4443 Autoren bzw. Speakern geschrieben und gehalten. Die Autoren mit den meisten Videos sind:", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 25.2*cm)
story.append(Paragraph("Alex Gendler mit 45 Videos, Iseult Gillespie mit 33, Matt Walker mit 18, Alex Rosenthal mit 5, Elizabeth Cox mit 13, Emma Bryce mit 12, Daniel Finkel mit 11 und Juan Enriquez mit 11. Für diese 8 Autoren habe ich mich entschieden noch eine genauere Analyse zu erstellen. Da danach 6 Autoren mit einer gleichen Anzahl von Videos (9) folgen, habe ich den Cut bei 8 Autoren gesetzt.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Autoren_Views.png", 30, 390, width=440, height=290)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 12.5*cm)
story.append(Paragraph("In dieser Grafik werden die durchschnittlichen Views des Autors aufgezeigt. Wie man erkennen kann übertreffen nur 3 dieser 8 Autoren die durschnittliche View-Anzahl aller Videos von 2.061.576.", style["BodyText"]))
frame.addFromList(story, pdf)
#FOTO
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Autoren_Likes.png", 30, 35, width=440, height=290)

pdf.showPage()


# In[1349]:


#Seite 6
#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 6 von 9")

style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 26.5*cm)
story.append(Paragraph("Auch bei den Likes haben es nur Alex Gendler, Daniel Finkel und Emmy Bryce über die durchschnittliche Like-Anzahl von 62.608 geschafft. Das liegt natürlich auch am Zusammenhang zwischen Views und Likes.", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 25*cm)
story.append(Paragraph("Dennoch gilt, nur weil die Autoren viele Videos herausgebracht haben heißt das nicht, dass die Videos auch gleichzeitig eine gute Performance haben. Deswegen sollte man in Zukunft schauen, welche Autoren eine gute Performance auf ihre Videos haben.", style["BodyText"]))
frame.addFromList(story, pdf)

#Überschrift 
pdf.setFont("Helvetica", 16)
pdf.setFillColor("#FF2B06")
pdf.drawString(32, 660, "6. Monatsvergleich")

frame = Frame(1*cm, 1*cm, breite-(11*cm), 22.2*cm)
story.append(Paragraph("Am Anfang wurden schon die Verteilungen der Videos nach Jahren dargestellt. Nun folgt noch eine Aufschlüsselung der Videos für die letzten 5 Jahre nach Monaten. ", style["BodyText"]))
frame.addFromList(story, pdf)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 21*cm)
story.append(Paragraph("Die grauen Linien stellen die durchschnittlichen Videos pro Monat da. Es wurden in den letzten 5 Jahren durchschnittlich 40 Videos pro Monat veröffentlicht.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/2017_Monate.png", 30, 260, width=470, height=320)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 8*cm)
story.append(Paragraph("Im Jahr 2017 gibt es 4 Monate die den Durchschnitt übersteigen. Der Monat mit den meisten Videos ist der April gefolgt von November, August und Dezember.", style["BodyText"]))
frame.addFromList(story, pdf)

pdf.showPage()


# In[1350]:


#Seite 7
#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 7 von 9")

style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 26.5*cm)
story.append(Paragraph("Im Jahr 2018 gibt es ebenfalls 4 Monate die den Durchschnitt übersteigen. Ebenfalls der April, November und Dezember. Aber auch im Oktober.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Monat_2018.png", 30, 420, width=470, height=320)

pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Monat_2019.png", 30, 80, width=470, height=320)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 1.5*cm)
story.append(Paragraph("In 2019 übersteigen die Monate April, Juli, September und November den durchschnittlichen Wert.", style["BodyText"]))
frame.addFromList(story, pdf)

pdf.showPage()


# In[1351]:


#Seite 7
#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 8 von 9")

style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 26.5*cm)
story.append(Paragraph("Der Oktober ist 2020 der Monat mit den meisten Videos. Aber auch im Februar, März, Juni und November wurde der Durchschnitt überschritten.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Monat_2020.png", 30, 420, width=470, height=320)

frame = Frame(1*cm, 1*cm, breite-(11*cm), 13.5*cm)
story.append(Paragraph("2021 wurde 3 mal der Durchschnitt erreicht: im Mai, August und Oktober.", style["BodyText"]))
frame.addFromList(story, pdf)

#FOTO
pdf.drawInlineImage("/Users/marenabele/Desktop/Data-Storytelling_2.0/Data/Grafiken/Monat_2021.png", 30, 50, width=470, height=320)

pdf.showPage()


# In[1352]:


#Seite 8
#CODE für den HEADER
pdf.drawInlineImage(img_header, 20, 790, width = 100, height=45)
pdf.setFont("Helvetica", 10)
pdf.setFillColor("#9a9695")
pdf.drawString(130, 807, "TED Talk Explorer - Report")
pdf.drawString(330, 807, "Maren Abele")
pdf.drawString(500, 807, "Seite 9 von 9")

style = getSampleStyleSheet()

story=[]

frame = Frame(1*cm, 1*cm, breite-(11*cm), 26.5*cm)
story.append(Paragraph("Es fällt auf, dass im April und eher am Ende des Jahres die meisten Videos veröffentlicht werden. Das hängt evtl. mit dem Zeitpunkt der eigentlichen Konferenz zusammen. Außerdem lässt es auf ein “Sommer-Loch” schließen, denn in den Monaten Juni, Juli werden eher weniger Videos veröffentlicht. Hier wäre es gut, wenn pro Monat ungefähr gleich viele Videos veröffentlicht werden würden, so gibt es keine Monate an denen es deutlich mehr neue Videos gibt und die Zuschauer überfordern könnten.", style["BodyText"]))
frame.addFromList(story, pdf)

pdf.showPage()
pdf.save()


# ##### Quellen
# * https://www.reportlab.com/docs/reportlab-userguide.pdf Generelle Doku
# * https://code-maven.com/create-multipage-pdf-file-in-python
# * https://www.youtube.com/watch?v=kzmyFTwIJw8&list=PLI8raxzYtfGzwEqGLm4fCnnbTAGbSHa6- Hier mehrere Videos aus der Playliste
