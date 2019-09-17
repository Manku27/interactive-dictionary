import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def inpword(w):
	w = w.lower()
	x = get_close_matches(w,data.keys())
	if w in data:
		return data[w]
	elif len(x)>0:
		yn = input("Did you mean "+ x[0] + "? Y/N \n")
		yn = yn.lower()
		if yn == 'y':
			return data[x[0]]
		elif yn == 'n':
			return "Check. Nothing similar found"
		else:
			return "You're dumb as soup bruh"
	else:
		return "Doesnt exist"

while 1:
	word = input("Word for meaning:")
	y = inpword(word)[0]
	print(y)
