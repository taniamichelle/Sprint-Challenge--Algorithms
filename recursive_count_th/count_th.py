'''
Your function should take in a SINGLE PARAMETER (a string `word`)
Your function should RETURN A COUNT of how many OCCURRENCES of ***"th"*** occur within `word`. CASE MATTERS.
Your function must utilize RECURSION. It CANNOT CONTAIN ANY LOOPS.
'''

def count_th(word):
    counter = word.count('th')
    print("Occurrences of 'th': " + str(counter))
    
count_th('ninth')
count_th('seven')
count_th('thenth')
count_th('Thenth')
count_th('THthThtH')
count_th('htthth')
