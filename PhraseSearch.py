# fname = input("Enter file name: ")
fname = "text.txt"
def create_posting_list():
    word_num = 0
    num_words = 0
    Dict = {}
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            for item in words:
                if item in Dict.keys():
                    Dict[item].append(int(word_num))
                else:
                    Dict[item] = []
                    Dict[item].append(int(word_num))
                word_num += 1
            num_words += len(words)
    return Dict, num_words


def next( pos , term , plist):
    indexlist = plist[term]
    if pos >= int(indexlist[len(indexlist)-1]):   #if pos is greater than equal to the last index return -1
        return -1
    for index in indexlist:
        if index > pos:
            return index

def prev( pos , term , plist):
    indexlist = plist[term]
    if pos <= int(indexlist[0]):   #if pos is smalller than equal to the first index return -1
        return -1
    previndex = indexlist[0]
    for index in indexlist:
        if index >= pos:
            return previndex
        previndex = index
    return previndex


def phrasesearch(phrasequery, pos , plist):
    v = pos
    l = len(phrasequery)
    for term in phrasequery:
        v = next(v, term, plist)
        if v == -1:
            return -1, -1

    u = v

    for i in range(l-2,-1,-1):
        u = prev(u, phrasequery[i], plist)
        if u == -1:
            return -1, -1

    if (v-u) == (l-1):
        return u,v
    else:
        return phrasesearch(phrasequery, u, plist)



posting_list, num_words = create_posting_list()

print(posting_list)

print("Number of words in the corpus: " + str(num_words))

phrase = "your time"
print("phrase to be searched : "+ phrase)
phraselist = phrase.split()

exist =1
for terms in phraselist:
    if terms in posting_list.keys():
        exist = 1
    else:
        exist = 0
        print("Sorry, phrase doesnot exist in the corpus")
        break

if exist ==1:
    u = 0
    v = 0
    occurences = 0
    while u != -1 and v !=-1:
        u,v = phrasesearch(phraselist, v, posting_list)
        if u == -1 and v == -1:
            if(occurences == 0):
                print("No Occurence")
        else:
            occurences+=1
            print(str(occurences) +" Occurence at [ "+ str(u)+" to "+ str(v) + " ]\n")

