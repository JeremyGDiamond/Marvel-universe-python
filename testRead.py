import csv

comics = []

characters = []

with open('nodes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        
        name = row[0]
        typeOf = row[1]
    
        if typeOf == 'comic':
            comics.append(name)
        else:
            characters.append(name)

collabArray = [[0] * len(characters) for i in range(len(characters))]

for x in range(len(characters)):
    collabArray[0][x] = characters[x]
    collabArray[x][0] = characters[x]


inBookArray = [[0] * len(comics) for i in range(len(characters))]
for x in range(len(characters)):
    inBookArray[x][0] = characters[x]
for x in range(len(comics)):
    inBookArray[0][x] = comics[x]
