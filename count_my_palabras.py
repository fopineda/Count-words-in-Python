#########################
# By: Felipe O Pineda   #
# 07/29/16              #
# fopineda95@gmail.com  #
#########################

def count_my_palabras(s):
    """ Counts the occurance of every word in a give string """
    stringerSplit =  s.split()
    wordBank = []   # List holds all the words in string w/o repition
    wordCount = []  # List holds the word and count in a tuple

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

    return wordCount

#############################################################################################################
# First loop will loop through the string and choose every word once.                                       #
# This loops basically finds the all the words for the wordback.                                            #
# Now its run and gun loop so it checks if the word is in the wordBank already                              #
# If it isn't then it'll put  it in for later checking and carry on with the same word called currentWord   #
# to the next loop.                                                                                         #
#                                                                                                           #
# Second loop takes the passed on word (currentWord) and iterates through the string again                  #
# comparing it the every word in tbe string. If it matches then it increments the count value.              #
# once the second loop has finished iterating through the string it will have full count of                 #
# how many times it found the currentWord in the string. Now it'll place that word in                       #
# wordCount list as a tuple (word,count). It only appends this tuple once the second loop                   #
# is done with the string (and technically the first loop is done with the currentWord).                    #
# It'll then go to the next word and begin the process again.                                               #
#                                                                                                           #
#############################################################################################################
