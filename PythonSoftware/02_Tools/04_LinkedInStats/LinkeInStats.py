#!/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# ----------------
#  02.12.2021 Petros Mitropoulos, arko GmbH
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

PostTitle='JSON Format29_11_2021' # The name of the table as it will be saved as json file

Dir='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/6_Marketing/00_LinkedIn_Blogs/Auswertung/'
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
            print('Row 0 is: '+ row[0] + ' / Total text: ' + ", ".join(row))
            MyData.append(", ".join(row))
            i_clear += 1
        i_line +=1


# Loop through MyData to get data by company
Firma= {}
i=0
# First row with manual setup
Number=MyData[0].split(",")
Firma[str(MyData[i])]=Number[0]
i=2
j=0
for i in range(2,len(MyData),2):
    if MyData[j]=="Beruf":
        print("Du bist bei Beruf")
        StartBeruf=j
        break
    elif MyData[j+1]=="Beruf":
        print("Du bist bei Beruf")
        StartBeruf=j+1
        break
    Number=MyData[i+1].split(",")
    Firma[str(MyData[i])]=Number[0]
    j=j+1
    print(i)

Beruf= {}
# Manueles Setup für die erste Zeile
Number=MyData[StartBeruf+1].split(",")
Beruf[Number[6]]=Number[1]
j=StartBeruf+2
for i in range(0,len(MyData),2):
    if i>StartBeruf+1:
        if MyData[j]=="Herkunft":
            print("Du bist bei Herkunft")
            StartHerkunft=j
            break
        elif MyData[j+1]=="Herkunft":
            print("Du bist bei Herkunft")
            StartHerkunft=j+1
            break
        Number=MyData[i+1].split(",")
        Beruf[MyData[i]]=Number[0]
        j=j+1
        print(i)
  
        

Herkunft= {}
# Manueles Setup für die erste Zeile
Number=MyData[StartHerkunft+1].split(",")
Herkunft[Number[7]]=Number[0]

for i in range(0,len(MyData),2):
    if i>=StartHerkunft+1:
        Number=MyData[i+1].split(",")
        Herkunft[MyData[i]]=Number[0]
        print(i)


TotalAnalysis={"PostTitle":PostTitle,"Firma":Firma,"Beruf":Beruf,"Herkunft":Herkunft}

#Create json and write data
with open(JSNF,'w', encoding="UTF-8") as jsonFile:
    # make it readable and pretty
    jsonFile.write(json.dumps(TotalAnalysis,indent=4, ensure_ascii=False))

print('---- Ended -----')