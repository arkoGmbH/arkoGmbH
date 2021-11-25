#!/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# ----------------
#  25.11.2021 Petros Mitropoulos, arko GmbH
#  Converts CSV file into a JSON file
#  Conditions: 
#   - File must be comma separated
#    - The first line is the header row
#    - All furhter lines contain the values in comma separated format
# ----------------------
# INPUT:
#    - Fullpath of CSV file
#    - Directory to export the JSON file
#    - Date                (='11.05.2015')
#    - UniqueTableID       (='BSchr_11052015')     -> Unique table ID as defined by the convention for table identifivation
#    - TableName           (='BSchr_11052015')     -> The name of the table as it will be saved as .json file
#    - TableDescription    (='Festigkeitswerte')   -> Freie Beschreibung der Tabelle
#    - UniqueHeaderName    (='name')               -> Name of the header with the UniqueValues used for identifying values
# 
#
#
# Source: https://medium.com/@hannah15198/convert-csv-to-json-with-python-b8899c722f6d
# Note to self:
# Dictionaries — maps a set of objects (keys) to another set of objects (values).
# - Use {} to create a dictionary and [] to index it.
# - Separate key and value pairs with : and commas between each key pair
# CSV Module: https://docs.python.org/3/library/csv.html
# JSON Module: https://docs.python.org/3/library/json.html?highlight=json#module-json
# Nested dictionary access elements: https://www.programiz.com/python-programming/nested-dictionary


import csv
import json
from collections import OrderedDict

TBDate='11.05.2015'
UniqueTableID='BSchr_11052015'
TableName='BSchr_11052015' # The name of the table as it will be saved as json file
TableDescription='Festigkeitswerte'
UniqueHeaderName='name' #Unique header name from which the values will be used as a key for the dictionary


# Source CSV file (really comma separated) with commas in the first row
CSVF='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/02_Tools/03_CSVtoJSON/CSVF.txt' # Text file to convert

# Directory to export the JSON file
jsonDir='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/02_Tools/03_CSVtoJSON/'

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
