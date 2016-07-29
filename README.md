# Count-words-in-Python

###Description...
**count_my_palabras.py:** Counts the words from a given string in Python.

**countWords.py:** Is my answer to a python quiz given in the Udacity course [Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree-by-google--nd009)

>*The quiz wanted:*
>Implement a function count_words() in Python that takes as input a string s and a number n, and returns the n most frequently-occuring words in s. The return value should be a list of tuples - the top n words paired with their respective counts [(<word>, <count>), (<word>, <count>), ...], sorted in descending count order.
>You can assume that all input will be in lowercase and that there will be no punctuations or other characters (only letters and single separating spaces). In case of a tie (equal count), order the tied words alphabetically.

###Installation...
For the most part all you need to do is download it and run it with a python interpreter it. If you do not have python installed on your computer you will have to install it. You can install it from [here](https://www.python.org/downloads/).


### How to work it...
Run the python file.
```
>>>count_words("did a lot of stuff just to live this here lifestyle", 3)
[('a', 1), ('did', 1), ('here', 1)]

>>> count_my_palabras("Well I like candy but candy does not like me")
[('Well', 1), ('I', 1), ('like', 2), ('candy', 2), ('but', 1), ('does', 1), ('not', 1), ('me', 1)]
```
WARNING: If you put punctation in the sentence it will count incorrectly. Please see example below #TreadLightly
```
>>>count_my_palabras("Well I like candy, but candy does not like me")
[('Well', 1), ('I', 1), ('like', 2), ('candy,', 1), ('but', 1), ('candy', 1), ('does', 1), ('not', 1), ('me', 1)]
```

###Why I wrote it...
Great way to show-off my python skills :fire:. This script is great for anyone ever needs to count words in a string (sentence).

###Motivation from me...
Have a great day counting and coding! Dueces :v:
