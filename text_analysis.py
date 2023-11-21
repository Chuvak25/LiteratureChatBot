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

print(wordafter("the","The army crossed the river in june."))
def dist(word, text):
        if word in text:
                x = 0
                for item in text:
                        if word == text[x]:
                                fx = x
                        x += 1
                text_ln = len(text)
                dist = text_ln - fx - 1
                print(dist)
ilist = ["the","army","crossed","great","raging","river","in","the","month","of","june"]
dist("the",ilist)

         
