
#### The Function to reverse a string ####


def reverse_string():
	s = 'Hello World'
	# Reverse the string using slicing
	d = s[::-1]
	print ("The Reverse string is" , d)



# print words that satrts with s ###

def s_string():
	st = 'Sunset with sam'
	String = st.split()
	for item in String:
		if item[0].lower() == 's':
			print (item)


reverse_string()
s_string()


####   Write a program that prints the integers from 1 to 10. But for multiples of three print "Fizz" instead of the number, 
## and for the multiples of five print "Buzz".
### For numbers which are multiples of both three and five print "FizzBuzz".

def fizz_buzz():
	for letter in range(1,10):
		if letter%3 == 0 and letter % 5 != 0:
			print('FIZZ')
		elif letter%5 == 0 and letter % 3 != 0:
			print('BUZZ')
		elif letter%3 != 0 and letter % 5 != 0:
			print('FizzBuzz')
		else:
			print(letter)

 
reverse_string()
s_string()
fizz_buzz()