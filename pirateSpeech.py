import urllib

def readText():
    quotes = open("quotes.txt")
    contentsOfFile = quotes.read()
    #print (contentsOfFile)
    quotes.close()
    checkProfanity(contentsOfFile)

def checkProfanity (textToCheck):
	connection = urllib.urlopen ("http://www.isithackday.com/arrpi.php?text=" + textToCheck)
	output = connection.read()
	print (output)
	connection.close()
	

readText()

