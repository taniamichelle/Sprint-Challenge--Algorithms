'''
Your function should take in a SINGLE PARAMETER (a string `word`)
Your function should RETURN A COUNT of how many OCCURRENCES of ***"th"*** occur within `word`. CASE MATTERS.
Your function must utilize RECURSION. It CANNOT CONTAIN ANY LOOPS.
'''

def count_th(word):
    if len(word) <= 1:
        return 0
    else:
        if word[0:2] == 'th':
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])
        # return word.find('th')

    
print(count_th('tani'))
print(count_th('tenth'))
print(count_th('t')) 
print(count_th('Thenth'))    
print(count_th('THthThtH'))   
print(count_th('htthth'))   

# count_th('ninth')
# count_th('seven')
# count_th('thenth')
# count_th('Thenth')
# count_th('THthThtH')
# count_th('htthth')

    # if word == 0:
    #     return 0
    # elif word !=0:
    #     if t and h:
    #     word.split('th') == 0:
    #         return 0
    #     elif word.split('th') == 0:
    #         return 1 + count_th(word) 
        
    # if word == 0:
    #     return 0
    # elif word !=0:
    #     if word.split('th') == 0:
    #         return 0
    #     elif word.split('th') == 0:
    #         return 1 + count_th(word) 
    
    # if word == 0:
    #     return 0
    # elif word != 0:
    #     if word.split('th') == 0:
    # return 1 + count_th(word.split('th')) 
    

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

