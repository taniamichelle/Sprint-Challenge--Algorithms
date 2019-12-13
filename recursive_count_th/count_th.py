'''
Your function should take in a SINGLE PARAMETER (a string `word`)
Your function should RETURN A COUNT of how many OCCURRENCES of ***"th"*** occur within `word`. CASE MATTERS.
Your function must utilize RECURSION. It CANNOT CONTAIN ANY LOOPS.
'''
# def count_th(word, occurrences= None):
#     string = 'th'
    
#     if string in word == 0:
#         return 0
#     elif occurrences and occurrences[string] in word > 0:
#         return occurrences[string]

def count_th(word):
    string = 'th'
    occurrences = []
    w = len(word)
    s = len(string)

    if string not in word[0:s]:  # base case: if 'word' does not contain 'string' (which is equal to 'th'), return 0
        return 0
    elif string in word[0:s]:  # recursive function: if 'string'('th') is in 'word', add to occurrences list
        occurrences.append(word)
    
    return count_th(word[s-1:])


# def count_th(word):
#     string = 'th'
        
#     def counter(word, string, occurrences=[]):
#         w = len(word)
#         s = len(string)
#         string = 'th'
#         if string not in word[0:s]:  # base case: if 'word' does not contain 'string' (which is equal to 'th'), return 0
#             return 0
#         elif string in word[0:s] > 0:  # recursive function: if 'string'('th') is in 'word', add to occurrences list
#             occurrences.append[word]
#         #     return counter(str1[n2-1:], str2 +1)
#         # return counter(str1[n2-1:], str2)
    
count_th('ninth')
count_th('seven')
count_th('thenth')
count_th('Thenth')
count_th('THthThtH')
count_th('htthth')

# def find_max_profit(prices):
#   current_min_price_so_far = prices[0] # price at zero index
#   max_profit_so_far = prices[1] - prices[0] # subtract price at zero index from price at first index

#   for i in range(1, len(prices)):
#     if prices[i] < current_min_price_so_far:  # if price we're looking at is less than the current min price: 
#       current_min_price_so_far = prices[i]  # the current min price will be the price we're looking at
#     elif prices[i] - current_min_price_so_far > max_profit_so_far:
#       max_profit_so_far = prices[i] - current_min_price_so_far
  
#   return max_profit_so_far

# def count_th(word):
#     string = 'th'
#     t = word[0]
#     h = word[1]
#     l = len(word) 
#     if     
    

