import urllib

def readText(textFile):
    quotes = open(textFile)
    contentsOfFile = quotes.read()
    quotes.close()
    makePirateSpeech(contentsOfFile)

def makePirateSpeech (textToCheck):
	connection = urllib.urlopen ("http://www.isithackday.com/arrpi.php?text=" + textToCheck)
	output = connection.read()
	print (output)
	connection.close()


readText("quotes.txt")
