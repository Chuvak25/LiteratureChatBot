def wordafter(word, text): 
	text = text.lower()
	text = text.split()
	word = word.lower()
	wordslist = []
	if word in text:
		x = 0
		for words in text:
			if word == text[x]:
				wordslist.append(text[x+1])
			x += 1
		return wordslist
    #Returns all words in the text used after the specific mentioned word.

def sentence(wordslist):
	space = " "
	words = ""
	for word in wordslist:
		words += word
		words += space
	return words
    #Generates a sentence from a list of words, primitive at this level but a good foundation.

print(wordafter("the","the army crossed the river in june."))
def freq(word, text):
        x = 0
        text = text.lower()
        text = text.split()
        if word in text:
                for item in text:
                        if item == word:
                                x += 1
        return x/len(text)
print(freq("the","the army crossed the river in june."))
