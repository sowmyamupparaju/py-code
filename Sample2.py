
#### The Function check if string is palindrome ####


def palindrome():
	s = 'Hello H'
    s = s.replace(' ','')
    return s == s[::-1]  


 ### check the number of upper ann lower case letters in a string


def up_low():
	s = 'Google World'
    d = {"upp":0, "low":0}
    for c in s:
        if c.isupper():
            d["upp"]+=1
        elif c.islower():
            d["low"]+=1
        else:
            pass
    print("String given  : ", s)
    print("Upper case characters : ", d["upper"])
    print("Lower case Characters : ", d["lower"])

	 ### count primes ###
def count_p(num):
    p = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in p:  # use the p list!
            if x%y == 0:
                x += 2
                break
        else:
            p.append(x)
            x += 2
    print(p)
