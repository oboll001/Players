#This program will grab all information in the players_20.csv file located in
#the data folder. It goes through multiple different functions to get the desired output
#It uses the csv module to

import csv
from matplotlib import pyplot as plt
#This function will print out the top ten countries and generate a list that
#will allow me to get all the players for a nationality.
def topTenCountries(countries):
    topTen = []
    count = 0
    i = 0
    while count < 10:
        trip = False
        for c in topTen:
            if c == countries[i]:
                print("Same Country")
                trip = True
        if trip == False:
            topTen.append(countries[i])
            count = count + 1
        i = i + 1
    print(topTen)
    return topTen

#This function finds and prints the number of players with the same nationality in
#the top ten countries
def allThePlayers(rows, topTen):
    numberOfPlayers = []
    for t in topTen:
        idList = []
        count = 0
        for r in rows:
            if r['nationality'] == t:
                count = count + 1
        print(t + " has "+ str(count)+" of players")
        numberOfPlayers.append(str(count))
    return numberOfPlayers

#This function will print the top 5 players and wages
def topFive (rows):
    count = 0
    print("Short | Wage")
    for r in rows:
        if count < 5:
            print(r['short_name']+" " +r['wage_eur'])
        count = count + 1

#This function will print the 5 top paid players
def topFivePaid (rows):
    limit = 5
    paid = []
    for r in rows:
        if len(paid) < limit:
            temp = [r['wage_eur'], r['short_name']]
            paid.append(temp)
        else:
            i = 0
            while i < len(paid):
                if int(paid[i][0]) < int(r['wage_eur']):
                    paid[i][0] = r['wage_eur']
                    paid[i][1] = r['short_name']
                    break
                i = i + 1
    print(paid)

#This function will print the first ten records of Germany
def topTenGermany (rows):
    ten = []
    for r in rows:
        if len(ten) < 10 and r['nationality'] == "Germany":
            ten.append(r)
    for i in ten:
        print("Record -------------------------------" )
        print(i)

#This function will print the top 5 records of Germany players
#based on height, weight, and wages. Three different things
def topFiveRecords (rows, category):
    print("---------------------------------------------\n\n\n\n")
    limit = 5
    newList = []
    for r in rows:
        if len(newList) < limit and r['nationality']== "Germany":
            newList.append(r)
        else:
            i = 0
            while i < len(newList):
                if int(newList[i][category]) < int(r[category]) and r['nationality']== "Germany":
                    newList[i] = r
                    break
                i = i + 1
    for i in newList:
        print("Record -------------------------------" )
        print(i)

#This function will show the short name and wages of the first 5 Germany
#players
def topFiveGermanyWages(rows):
    limit = 5
    paid = []
    for r in rows:
        if len(paid) < limit and r['nationality'] == "Germany":
            temp = [r['wage_eur'], r['short_name']]
            paid.append(temp)
        else:
            i = 0
            while i < len(paid):
                if int(paid[i][0]) < int(r['wage_eur']) and r['nationality'] == "Germany":
                    paid[i][0] = r['wage_eur']
                    paid[i][1] = r['short_name']
                    break
                i = i + 1
    print(paid)
    
#This function is going to print out the top 5 shooters in the data file
def topFiveShooters (rows):
    limit = 5
    Legs = []
    for r in rows:
        try:
            if r['shooting'] == "":
                raise SyntaxError
            if len(Legs) < limit :
                temp = [r['shooting'], r['short_name']]
                Legs.append(temp)
            else:
                i = 0
                while i < len(Legs):
                    if int(Legs[i][0]) < int(r['shooting']):
                        Legs[i][0] = r['shooting']
                        Legs[i][1] = r['short_name']
                        break
                    i = i + 1
        except:
            i = 1
    print(Legs)

#This function will show the top 5 players that have awesome defending skills
def topFiveDefender (rows):
    limit = 5
    #NOT THE COMIC BOOK ONES!!
    defenders = []
    for r in rows:
        try:
            if r['defending'] == "":
                raise SyntaxError
            elif len(defenders) < limit:
                temp = [r['short_name'],r['defending'],r['nationality'],r['club']]
                defenders.append(temp)
            else:
                i = 0
                while i < len(defenders):
                    if int(defenders[i][1]) < int(r['defending']):
                        defenders[i][0] = r['short_name']
                        defenders[i][1] = r['defending']
                        defenders[i][2] = r['nationality']
                        defenders[i][3] = r['club']
                        break
                    i = i +1
        except:
            i = 1
    print(defenders)

#This function will go through the Real Madrid club and find the top 5
#It will show the category of records from the top 5
def topFiveRealMadrid (rows, category):
    limit = 5
    club = 'Real Madrid'
    players = []
    for r in rows:
        if len(players) < limit and r['club'] == club:
            temp = [r['sofifa_id'],r[category]]
            players.append(temp)
    print("The following list is with "+ category)
    print(players)
            

file = open('data\players_20.csv','r', encoding='utf-8')
csvreader = csv.DictReader(file)

rows = []
for row in csvreader:
    rows.append(row)
#i = 0
#while i < 5:
 #   print("Person: " + str(i))
  #  print(rows[i])
   # i = i+1
#This makes a list of nationalies
countries = []
for row in rows:
    countries.append(row['nationality'])
#print("The dataset has " + str(len(rows[0]))+ " number of categories.")
#print("The dataset has " + str(len(rows))+" number of records.")

#topTen = topTenCountries(countries)
#numb = allThePlayers(rows, topTen)
#print(numb)

# Set the figure size
#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True

#plt.bar(numb,numb, color = 'green')
#plt.xticks(numb, topTen)
#plt.show()
#topFive(rows)   

#topFivePaid(rows)
#topTenGermany(rows)
#topFiveRecords (rows, 'weight_kg')
#topFiveRecords (rows, 'wage_eur')
#topFiveRecords (rows, 'height_cm')
#topFiveGermanyWages(rows)
#topFiveShooters (rows)
#topFiveDefender (rows)
#topFiveRealMadrid (rows, 'wage_eur')
topFiveRealMadrid (rows, 'shooting')
topFiveRealMadrid (rows, 'defending')
topFiveRealMadrid (rows, 'nationality')
    
file.close()
