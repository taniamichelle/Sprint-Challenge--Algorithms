'''
Your function should take in a SINGLE PARAMETER (a string `word`)
Your function should RETURN A COUNT of how many OCCURRENCES of ***"th"*** occur within `word`. CASE MATTERS.
Your function must utilize RECURSION. It CANNOT CONTAIN ANY LOOPS.
'''

def count_th(word):
    string = 'th'
    # if string in word == 0:
    #     return 0
    # elif string in word > 0:
        
    def counter(word, string, occurrences=[]):
        w = len(word)
        s = len(string)
        string = 'th'
        if string not in word[0:w]:  # base case
            return 0
        elif string in word[0:s] > 0:  # recursive function
            occurrences.append[word]
        #     return counter(str1[n2-1:], str2 +1)
        # return counter(str1[n2-1:], str2)
    
count_th('ninth')
count_th('seven')
count_th('thenth')
count_th('Thenth')
count_th('THthThtH')
count_th('htthth')
