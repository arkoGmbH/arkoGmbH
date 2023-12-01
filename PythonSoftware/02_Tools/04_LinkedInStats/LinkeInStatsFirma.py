#!/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# ----------------
#  02.12.2021 Petros Mitropoulos, arko GmbH, all rights reserved
#  LinkedIn Post daten einlesen und Statistik daraus erstellen
#  
#
# ----------------------
# References:
# https://realpython.com/python-print/
# https://www.w3schools.com/python/ref_string_join.asp
# The join() method takes all items in an iterable and joins them into one string. "separator".join(iterable)
# string.split(separator, maxsplit) -> Split a string into a list where each word is a list item:

import csv
import json
from datetime import datetime

selection=2     #Wähle 1 für Manuel oder 2 für Automatisch über File Maker Schnittstelle
PostTitle='TBD' #The name of the table as it will be saved as json file. Example: PostTitle='2021_12_03DieGartenvonZug'
Stichtag= datetime.today().strftime('%d.%m.%Y')

# Manual text file selection (selection=1) or through PythonCom.txt file (selection=2)?

Dir='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/6_Marketing/00_LinkedIn_Blogs/Auswertung/'

if selection==1:
    #Continue with manually set name
    PostTitle=PostTitle
    print('--- Manual defined post name will be used ---')
elif selection==2:
    #Read post name from the PythonCom file
    CSVF=Dir+'PythonCom.txt' 
    with open(CSVF, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';') # No delimiter needed in reality
        for row in csv_reader:
            PostTitle=row[0]
            print(PostTitle)
        print('--- Python Com post name will be used ---')



# Source CSV file (really comma separated) with commas in the first row
CSVF=Dir+PostTitle+'.txt' # Text file mit copy paste des LinkedIn Posts

# Full directory of the JSON file
JSNF=Dir+PostTitle+'.json' # Json as a result

print('--- Start ----')
MyData=[]
# Initialise the dictionary
with open(CSVF, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ') # No delimiter needed in reality
    i_line = 0
    i_clear=0
    for row in csv_reader:
        # Use only the non empty rows
        if row:
            #print('Row 0 is: '+ row[0] + ' / Total text: ' + ", ".join(row))
            MyData.append(", ".join(row))
            i_clear += 1
        i_line +=1

# Loop through MyData to get data by company
Firma= {}
i=0
# First row with manual setup
Number=MyData[1].split(",")
Firma[MyData[0]]=Number[0]
i=2
for i in range(2,len(MyData),2):
    if MyData[i]=="Beruf":
        print("Du bist bei Beruf")
        StartBeruf=i
        break

    Number=MyData[i+1].split(",")
    Firma[str(MyData[i])]=Number[0]


TotalAnalysis={"PostTitle":PostTitle,"Stichtag":Stichtag,"Firma":Firma}

#Create json and write data
with open(JSNF,'w', encoding="UTF-8") as jsonFile:
    # make it readable and pretty
    jsonFile.write(json.dumps(TotalAnalysis,indent=4, ensure_ascii=False))

print('---- Ended -----')
