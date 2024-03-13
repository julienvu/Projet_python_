# mot le plus court le plus long

# ordre dans la phrase en premier
def get_min_and_max_words(sentence):
    sentence_split=sentence.split(" ")
    #splitter la phrase fractionner découper les mots avec le séparateur
    min_w=min(sentence_split, key=len)
    max_w=max(sentence_split, key=len)
    return (min_w,max_w)
    
def get_min_and_max_words_sorted(sentence):  
    words= sentence.split(" ")
    min_w, max_w=get_min_and_max_words(sentence)
    all_max_words=[ w for w in words if len(w)== len(max_w)]
    all_min_words=[ w for w in words if len(w)== len(min_w)]
    all_min_words.sort()
    all_max_words.sort()
    return all_min_words[0], all_max_words[0]
    
    
    
    
s="Un aa sachant chasser sait chasser sans son chier"

#min_word, max_word= get_min_and_max_words(s)
#print("Mot le plus petit: ", min_word)
#print("Mot le plus long: ", max_word)

min_word1, max_word1=  get_min_and_max_words_sorted(s)
print("Mot le plus petit: ", min_word1)
print("Mot le plus long: ", max_word1)
#split ("")
#min max

#print(max([2,9,5]))
#print(min([2,9,5]))
#print(min(["aa", "aaaaa", "zzz"], key=len))
#print(max(["aa", "aaaaa", "zzz"], key=len))