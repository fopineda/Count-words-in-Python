
#########################
# By: Felipe O Pineda   #
# 07/29/16              #
# fopineda95@gmail.com  #
#########################
"""Count words in Python """

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    stringerSplit =  s.split()
    wordBank = []   # List holds all the words in string w/o repition
    wordCount = []  # List holds the word and count in a tuple
    top_n = []      # List that will hold the required answer

    for i in range(0, len(stringerSplit)):          # Initial loop to find all words
        if stringerSplit[i] not in wordBank:
            wordBank.append(stringerSplit[i])
            currentWord = stringerSplit[i]
            count = 0
            for x in range(0,len(stringerSplit)):   # loop to compare currentWord with all words
                if currentWord == stringerSplit[x]:
                    count = count + 1
            
            holder = (currentWord,count)
            wordCount.append(holder)

    sortedWordCount = sorted(wordCount,key=lambda(k,v):(-v,k))

    for item in range(0,n):
        top_n.append(sortedWordCount[item])
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
