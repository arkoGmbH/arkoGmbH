#!/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# ----------------
#  02.12.2021 Petros Mitropoulos, arko GmbH
#  LinkedIn Post daten einlesen und Statistik daraus erstellen
#  
#
# ----------------------



import csv
import json
from collections import OrderedDict

TBDate='02.Dez.2021'
TableName='Post_SwitzerlandGlobal' # The name of the table as it will be saved as json file
TableDescription='Blabla'
UniqueHeaderName='name' #Unique header name from which the values will be used as a key for the dictionary


# Source CSV file (really comma separated) with commas in the first row
CSVF='\\Mac\Home\Documents\00_All\3_Arbeit\3_arko_GmbH\9_Projects\01_arko_GmbH\549_Funktionen_Berechnung\03_Marketing\LinkedInTool\BeispielAuswertungEinesPosts.txt' # Text file mit copy paste des LinkedIn Posts

# Directory to export the JSON file
jsonDir='\\Mac\Home\Documents\00_All\3_Arbeit\3_arko_GmbH\9_Projects\01_arko_GmbH\549_Funktionen_Berechnung\03_Marketing\LinkedInTool\'

# Full directory of the JSON file
JSNF=jsonDir+TableName+'.json' # Json as a result

# Initialise the dictionary
data={}
with open(CSVF, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Convention: Header strarts in the third row (hence line_count=3)
    line_count = 0
    for row in csv_reader:
        if line_count == 3:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        #print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        data[line_count]=row
        old_key=line_count
        new_key=data[line_count][str(UniqueHeaderName)]
        data[new_key] = data[old_key] # Assign a new key to the old key
        del data[old_key]                # Delete the old key
        line_count += 1 
    print(f'Processed {line_count} lines.')


# Even more nested dictionary
evenmore={'Date':TBDate,'Table Name':TableName,'UniqueTableID':UniqueTableID,'Table Description:': TableDescription, 'Stored by ' + str(UniqueHeaderName) :data}

# Change the dictionary key from the row number to the desired uniqueHeader one

#d = {'x':1, 'y':2, 'z':3}
#d1 = {'x':'a', 'y':'b', 'z':'c'}

#data((d1[key], value) for (key, value) in d.items())

#data.move_to_end('a')
#Create json and write data
with open(JSNF,'w') as jsonFile:
    # make it readable and pretty
    jsonFile.write(json.dumps(data,indent=4))

with open(JSNF,'w') as jsonFile:
    # make it readable and pretty
    jsonFile.write(json.dumps(evenmore,indent=4))

# Read the json file (notice that it has a nested dictionary inside on the basis of the row number)

with open(JSNF) as json_file:
    redata = json.load(json_file)
    for p in redata['Stored by name']:
        print('Name: ' + redata['Stored by name'][p]['name'])
        print('Bday: ' + redata['Stored by name'][p]['birthday month'])
        print('')
# p is the unique value that helps to retrieve the information we want. Example to find Erica Meyers birthday we do the following
value=redata['Stored by name']['Erica Meyers']['birthday month']
