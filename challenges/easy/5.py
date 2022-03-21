"""
    Problem
    Given: A string of length at most 10000 letters.
    
    Return: How many times any word occurred in string. Each letter case (upper or lower) in word
    matters. Lines in output can be in any order.
    
    Sample Dataset :- "We tried list and we tried dicts also we tried Zen"
    
    Sample Output :-
        and 1
        We 1
        tried 3
        dicts 1
        list 1
        we 2
        also 1
        Zen 1
"""

def findWordCount(word):
    store = []
    words = word.split(" ")
    for i in range(len(words)):
        # create a tuple
        store.append((words[i],word.count(words[i])))

    # convert tuple into dictionary, then iterate through and print result
    wordDict = dict(set(store))
    for values, key in wordDict.items():
        print(f" {values} : {key} ")

findWordCount("We tried list and we tried dicts also we tried Zen")