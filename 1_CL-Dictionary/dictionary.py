import json

data = json.load(open("data.json"))

def retrieve_definition(word):

	word = word.lower() #convert input to all lowercase

	if word in data:
		return data[word]
	elif word.title() in data: #catches capitalized words
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()] #catches acronyms
	elif len(get_close_matches(word, data.keys())) > 0:
		action = input("Did you mean %s instead??? [y or n]" % get_close_matches(word, data.keys())[0])
		if (action == 'y'):
			return data[get_close_matches(word, data.keys())[0]]
		elif (action == 'n'):
			return "Sorry this word does not exist"
		else:
			return "Sorry we don't understand your request. Make sure to use [y or n], not [yes or no]"
	else:
		return "Sorry this word does not exist"


word_user = input("Please enter a word: ")

output = retrieve_definition(word_user)

if type(output) == list:
	for item in output:
		print("-", item)
else:
	print("-", output)

print("output type: ", type(output))