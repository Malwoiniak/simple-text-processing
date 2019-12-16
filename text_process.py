def strip_delimiters(a):
	""" Removes delimiters: ',' and '.' from the list of strings

	Parameters:
	a (list): The list of strings to remove delimiters ',' and '.' 

	Returns: list of strings without delimiters ',' and '.'
	""" 
	words_strip=[]
	for item in a:
		words_strip.append(item.strip(',.'))
	return(words_strip)



def five_longest(a):
	"""Returns elements [0:5] of list of string sorted by length in descending order 

	Parameters:
	a (list): The list of strings to perform above

	Returns: Elements [0:5] of list of string sorted by length in descending order 
	""" 
	a=[item.lower() for item in a]
	for item in a:
		new=(sorted(list(set(a)), key=len, reverse=True)[:5])
		return(new)

def words_in_sentences(a,b):
	""" Returns length of string split by whitespace at given index in list of strings 

	Parameters:
	a (list): The list of strings to perform above
	b (int): index of an element in string list 

	Returns: Length of string split by whitespace at given index in list of strings 
	""" 
	for item in a:
		return (len(a[b].split()))


text = """We have developed speed, but we have shut ourselves in. Machinery that gives abundance has left us in want. Our knowledge has made us cynical. Our cleverness, hard and unkind. We think too much and feel too little. More than machinery we need humanity. More than cleverness we need kindness and gentleness."""

#Count sentences in text
sentences=text.split('.')
print('This text contains', len(sentences)-1, 'sentences.\n')

#Count words in text
words=text.split()
print('This text contains', len(words), 'words.\n')

#Remove delimiters in words list
words_stripped = strip_delimiters(words)

#Sort five longest words alphabetically in descending order
words_longest=(five_longest(words_stripped))
words_final=(sorted(words_longest))

#Sort sentences in text by length in descending order
sentences_sorted = sorted(sentences,key=lambda x: len(x.split()), reverse=True) 

#Create a list of strings (word counts in each sentence in descending order)
sen=[]
i=0
for x in range(0,len(sentences_sorted)-1,1):
	sen.append(words_in_sentences(sentences_sorted,i))
	i=i+1

 
print('The longest sentence in this text contains', sen[0], 'words; The second longest sentence in this text contains', sen[1], 'words; Two third longest sentences in this text contain', sen[2], 'words; Two fourth longest sentences in this text contain', sen[4], 'words; The shortest sentence in this text contains', sen[-1], 'words.\n')

print('Five longest words in this text ordered alphabetically are:',f"'{words_final[0]}',",f"'{words_final[1]}',",f"'{words_final[2]}',", f"'{words_final[3]}',", f"'{words_final[-1]}'.")
