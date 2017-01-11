# From HTML at http://www.pythonchallenge.com/pc/def/linkedlist.php:
# <a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"></a>
# <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
# end. 400 times is more than enough. -->
import requests
import re

# Start nothing number
# nothing = ['12345']
# on iteration 84, the output breaks, and reads
# "Yes. Divide by two and keep going"
# nothing value here is 16044 so new nothing Start value is:
nothing = ['8022']

for x in range(0, 200):
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(nothing[0])	
	print (url)
	r = requests.get(url)
	# Original findall() regex:
	# nothing = re.findall('and the next nothing is ([0-9]*)', r.text)
	# After first run, iteration 55 specified exact regex pattern to 
	# look for:
	nothing = re.findall('and the next nothing is ([0-9]*)', r.text)
	print('retrieval: {}, full text: {}, nothing: {}'.format(x, r.text, nothing[0]))


