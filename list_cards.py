
#pulls information from a searched card and displays it


def dr():
	drCardName = ['innervate', 'malore']
	maCardName = ['fireball', 'pyroblast']
	allCardName = drCardName + maCardName
	drCardCost = [0, 7]
	maCardCost = [4, 10]
	allCardCost = drCardCost + maCardCost
	cardRequest =  input('What Card: ')

	cardRequest = cardRequest.lower() #makes any input/card searched lowercase
	
	cardSearched = ([s for s in allCardName if cardRequest in s]) #If you want them separated by newlines: ----> print "\n".join([s for s in list if sub in s])
	strCardFound = ''.join(cardSearched)
	strCardFoundSearchable = strCardFound #Creates a variable for stat searchability loc
	strCardFound = strCardFound.capitalize() #Capitalizes the output

	print (strCardFound)
	if strCardFound == '':
		print(strCardFound)
	
		print('No card found')

	if strCardFoundSearchable in allCardName:
		loc(allCardName, allCardCost, strCardFoundSearchable) 


def loc(a, b, c): #allows for gathering of data from different lists for a card
#a is the list you know the variables position  
#c is the variable in the list  
#b is the list you want to search
		for loc in [loc for loc,cardIndex in enumerate(a) if cardIndex == c]: #checks to see if a card exists in a list --- also checks for duplicates
			print(loc)
			manaCost = str(b[loc])
			print('Mana Cost > ' + manaCost)
	#print(drCardName[0])
	
	
#create deck NEED Django for this
#sort list by mana cost/attackhealth	
	

#from list_cards import c
#c() (IDE)
#'Druid', 'Hunter', 'Mage', 'Paladin', 'Priest', 'Rougue', 'Shaman', 'Warlock', 'Warrior', 'Neutral'
#py list_cards (cmd)