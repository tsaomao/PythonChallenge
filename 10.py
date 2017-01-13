# Page: 
# Clicking bull yields:
#   a = [1, 11, 21, 1211, 111221, 
# On page: len(a[30]) = ?
# Sequence is look-and-say sequence, where each term describes the previous
# Starts with 1
# Then 1 1 is one numeral 1
# Then 2 1 is two numeral 1s
# Then 1 2 1 1 is one numeral 2 and one numeral 1
# We want a[30].
# Start string
a = '1'
tmp = ''

# Do 31 times:
for x in range(0,30):
	# a saves state, so no need to init beyond zero out
	y = 0
	z = 0
	# iterate through a
	while y < len(a):
		# while character is same, increment z
		while z < len(a) and a[z] == a[y]: 
			z += 1
		# start building next a string
		tmp += str(z-y) + a[y]
		y = z
	print(tmp)
	# save state
	a = tmp
	# reinit
	tmp = ''

print("SOLUTION: http://www.pythonchallenge.com/pc/return/{}.html".format(len(a)))
