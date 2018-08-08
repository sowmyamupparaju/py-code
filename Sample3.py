## function to return if both numbers are even, returns  lower 
##  one or both numbers are odd return greater
 # lesser_of_two_evens(6,4) --> 4
 # lesser_of_two_evens(2,5) --> 5

def two_num(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
		
#  function takes a two-word string , returns True if both words start with same letter
		
def two_word(text):
    x = text.split()
    if x[1][0]  == x[0][0]:
        return True
    else:
        return False

		# Second way
def two_word1(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


## for integer, return True if it is within 10 of either 100 or 200	
	
def closest(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))