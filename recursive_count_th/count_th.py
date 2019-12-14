'''
Your function should take in a SINGLE PARAMETER (a string `word`)
Your function should RETURN A COUNT of how many OCCURRENCES of ***"th"*** occur within `word`. CASE MATTERS.
Your function must utilize RECURSION. It CANNOT CONTAIN ANY LOOPS.
'''

def count_th(word):
    count = 0
    w = len(word)
    i = 0
    j = 1
    if word == 0:
        return 0
    elif word > 0:
        if i == 't' and j == 'h':
            i = i+1
            j = j+1
            count = count+1
        elif i != 't' or j != 'h': 
            i = i+1
            j = j+1
            count = 0
            
        count_th(word)   
        return count 
    

# def helper(i, j, count):
    # if i == 't' and j == 'h':
    #         i = i+1
    #         j = j+1
            # count = count+1

# def count_th(word):
#     string = 'th'
#     occurrences = 0
#     w = len(word)
#     s = len(string)

#     if string not in word[0:s]:  # base case: if 'word' does not contain 'string' (which is equal to 'th'), return 0
#         return 0
#     elif string in word[0:s]:  # recursive function: if 'string'('th') is in 'word', add to occurrences list
#         occurrences = 1
    
#     return count_th(word[s-1:])
 

# def count_th(word):
    # w = len(word)
    # t = word[0]
    # h = word[1]
    # string = t + h
    # occurrences = 0
    # if string not in w:
    #     return 0
    # elif string in w == 1:
    #     occurrences = 1
    # elif string in w > 1:
    #     return count_th(word)
    

count_th('ninth')
count_th('seven')
count_th('thenth')
count_th('Thenth')
count_th('THthThtH')
count_th('htthth')