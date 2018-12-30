import csv

def outputTest(name, testArray = []):
    #testing output
    with open(name + ".csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(testArray)

comics = []

characters = []

#read in data from nodes.csv

with open('nodes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        
        name = row[0]
        typeOf = row[1]
    
        if name == "node":
            print ("reading nodes.csv")
            comics.append(0)
            characters.append(0)
        elif typeOf == 'comic':
            comics.append(name)
        else:
            characters.append(name)

# build arrays for collabs and book apperanaces

collabArray = [[0] * len(characters) for i in range(len(characters))]
for x in range(len(characters)):
    collabArray[0][x] = characters[x]
    collabArray[x][0] = characters[x]


inBookArray = [[0] * len(comics) for i in range(len(characters))]
for x in range(len(characters)):
    y = x+1
    inBookArray[x][0] = characters[x]
for x in range(len(comics)):
    inBookArray[0][x] = comics[x]

# outputTest("collab",collabArray)

# outputTest("inbook",inBookArray)

#populate the arrays

#populate inBookArray
with open('edges.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        
        hero = row[0]
        comic = row[1]
    
        if hero == "hero":
            print ("reading edges.csv")
        else:
            y = characters.index(hero)
            x = comics.index(comic)

            inBookArray[y][x] = 1

#outputTest("inbook2",inBookArray)

count = -1

#populate collaberate array

with open('hero-network.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        
        count = count+1

        hero1 = row[0]
        hero2 = row[1]

        if hero1.endswith(" "):
            hero1 = hero1[:-1]

        if hero2.endswith(" "):
            hero2 = hero2[:-1]
    
        if hero1 == "hero1":
            print ("reading hero-network.csv")
        else:
            y = characters.index(hero1)
            x = characters.index(hero2)

            collabArray[y][x] = 1

#outputTest("chars2",collabArray)

# evaluate the max min and mean arrays and print results

print ("The number of comics is: " + str(len(comics)))
print ("The number of charaters is: " + str(len(characters)))

CharsPerBook = []
for x in range(1, len(comics)):
    sum = 0
    for i in range(1, len(characters)):
        sum = sum + inBookArray[i][x]    
    CharsPerBook.append(sum)

CharsPerBook.sort()

minim = CharsPerBook[0]

maxim = CharsPerBook[len(CharsPerBook)-1]

mean = 0

for x in range(len(CharsPerBook)):
    mean = mean + CharsPerBook[x]
mean = mean/len(CharsPerBook)

print ("The max, mean, and min number of charaters per book are :" + str(minim) + ", " + str(mean) + ", and " + str(maxim))

BooksPerChar = []
for y in range(1, len(characters)):
    sum = 0
    for i in range(1, len(comics)):
        sum = sum + inBookArray[y][i]
    BooksPerChar.append(sum)

BooksPerChar.sort()

minim = BooksPerChar[0]

maxim = BooksPerChar[len(BooksPerChar)-1]

mean = 0

for x in range(len(BooksPerChar)):
    mean = mean + BooksPerChar[x]
mean = mean/len(BooksPerChar)

print ("The max, mean, and min number of book apperances per charater are :" + str(minim) + ", " + str(mean) + ", and " + str(maxim))



CollabsPerChar = []
for x in range(1, len(characters)):
    sum = 0
    for i in range(1, len(characters)):
        sum = sum + collabArray[i][x]
    CollabsPerChar.append(sum)

CollabsPerChar.sort()

minim = CollabsPerChar[0]

maxim = CollabsPerChar[len(CollabsPerChar)-1]

mean = 0

for x in range(len(CollabsPerChar)):
    mean = mean + CollabsPerChar[x]
mean = mean/len(CollabsPerChar)

print ("The max, mean, and min number of collaborators per charater are :" + str(minim) + ", " + str(mean) + ", and " + str(maxim))
