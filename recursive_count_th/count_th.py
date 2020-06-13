'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

'''
def count_th(word):
    
    # base case
    if len(word) < 2:
        return 0

    # use find() method. https://www.geeksforgeeks.org/python-string-find/
    #   "returns the lowest index of the substring if it is found in given string. 
    #       If it’s not found then it returns -1."
    elif word.find("th") >= 0:
        # store the index where the "th" is found
        found = word.find("th") 

        # since find returns the lowest index of the substring,
        # add 2 to go to the start of the next index to check
        new_count = found +2

        # identify where to start the next search for recursion
        new_word = word[new_count: len(word)]

        # when "th" is found, go to the next set to check.
        return 1 + count_th(new_word)

    # if it is not found (word.find() returns -1)
    else:
        return 0