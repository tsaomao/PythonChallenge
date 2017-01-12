# Start URL: http://www.pythonchallenge.com/pc/def/channel.html
# Look at source. See comment: zip
# Open URL: http://www.pythonchallenge.com/pc/def/channel.zip
# Download channel.zip and look at structure.
# There is a readme. Which reads:
#   welcome to my zipped list.
#    
#   hint1: start from 90052
#   hint2: answer is inside the zip
# Guess on approach:
# Use some zip libraries to navigate through zip for info in files, starting with 90052.txt, and find
# answer. Sort of like 6.py but with zip archive handling.
# 90052.txt within ZIP archive reads:
#   Next nothing is 94191 
import zipfile
import re

# Handle on zip file "channel.zip"
f = zipfile.ZipFile("channel.zip", "r")

# Start filename
filenum = 90052
collcomments = ""

# Crashes at filenum = 46145 (iteration 908)
# Because the yield is 'Collect the comments', retroactively collect
# comments in order
for x in range(0, 908):
	filecont = f.read("{}.txt".format(str(filenum))).decode("utf-8")
	nothing = re.findall('Next nothing is ([0-9]*)', filecont)
	filenum = int(nothing[0])
	collcomments += f.getinfo("{}.txt".format(filenum)).comment.decode("utf-8")
	print('retrieval: {}, full text: {}, nothing: {}'.format(x, filecont, filenum))


filefincont = str(f.read("{}.txt".format(str(46145))))
print(filefincont)

print(collcomments)

print("http://www.pythonchallenge.com/pc/def/{}.html".format("hockey"))

# Yields clue, to look at the letters that make up the HOCKEY banner
print("SOLUTION: http://www.pythonchallenge.com/pc/def/{}.html".format("oxygen"))
