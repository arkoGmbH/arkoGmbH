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

PostDatum='02_Dez_2021'
PostTitle='Post_SwitzerlandGlobal' # The name of the table as it will be saved as json file
UniqueHeaderName='name' #Unique header name from which the values will be used as a key for the dictionary


# Source CSV file (really comma separated) with commas in the first row
CSVF='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/02_Tools/04_LinkedInStats/AuswertungEinesPosts.txt' # Text file mit copy paste des LinkedIn Posts

# Directory to export the JSON file
jsonDir='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/02_Tools/04_LinkedInStats/'

# Full directory of the JSON file
JSNF=jsonDir+PostTitle+" "+PostDatum+'.json' # Json as a result
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
Number=MyData[i+1].split(",")
Firma[str(MyData[i])]=Number[0]
i=2

for x in MyData:
    if x=="Beruf":
        print("Du bist bei Beruf")
        break
    Number=MyData[i+1].split(",")
    Firma[str(MyData[i])]=Number[0]
    i=i+2
    print(x)
   


Beruf= {}
# Manueles Setup für die erste Zeile
Number=MyData[15].split(",")
Beruf[Number[6]]=Number[1]
i=16
for x in MyData:
    if MyData[i]=="Herkunft":
        print("Du bist bei Herkunft")
        break
    Number=MyData[i+1].split(",")
    Beruf[MyData[i]]=Number[0]
    i=i+2
    print(x + ' i: ' + str(i))

Herkunft= {}
# Manueles Setup für die erste Zeile
Number=MyData[33].split(",")
Herkunft[Number[7]]=Number[0]
i=34
for x in MyData:
    if i>=len(MyData)-1:
        break
    Number=MyData[i+1].split(",")
    Herkunft[MyData[i]]=Number[0]
    i=i+2
    print(x + ' i: ' + str(i))


TotalAnalysis={"PostTitle":PostTitle,"PostDatum":PostDatum,"Firma":Firma,"Beruf":Beruf,"Herkunft":Herkunft}

#Create json and write data
with open(JSNF,'w', encoding="UTF-8") as jsonFile:
    # make it readable and pretty
    jsonFile.write(json.dumps(TotalAnalysis,indent=4, ensure_ascii=False))

print('---- Ended -----')
