'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # looking for how many times "th" string is in the word argument
    
    # base case
    # if i < len(word):
    #     return 0
    check = 'th'

    # check the first two elements for 'th'
    # https://docs.python.org/3/tutorial/introduction.html for the element call-out
    if word[0:2] == check:
        # print('found')
        # print(word[1:])

        return count_th(word[2:]) +1

    elif len(word) < len(check):
        return 0
    else:
        # print('not found')
        # print(word[1:])
        return count_th(word[1:])

    # str.find(str, beg=0, end=len(string))
    # word.find('th', beg=0, end=len(word))
  