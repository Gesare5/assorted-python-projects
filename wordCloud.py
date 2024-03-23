# new_string = "!hi. wh?at is the weat[h]er lik?e."
words = '!hi. wh?at is the weat[h]er lik?e. create a dictionary with word and word frequencies that can be passed to the'
# wordsarray = words.split()
frequencies = {}

my_set= set(['and', 'if', 'is', 'a', 'that', 'the'])

# remove punctuation
def removePunctuation(sentence):
    txt =sentence
    for character in sentence:   
        isPunctuation = character.isalpha()
        # print(isPunctuation)
        if isPunctuation == False and character !=" ":
            txt = txt.replace(character, "")
            # print(txt)
    return txt        

# create word array
def createWordArray(text):
    return text.split()

# create dictionary excluding words in the set
def createDictionary(newarray, newset):
    for word in newarray:
        if word not in newset:
            if word not in frequencies:
                frequencies[word] = 1
            else: 
                frequencies[word] += 1 
    return frequencies


new_sentence = removePunctuation(words)

new_array = createWordArray(new_sentence)

print(createDictionary(new_array, my_set))
