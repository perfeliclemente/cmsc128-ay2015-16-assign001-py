def numToWords(user_input):															# Function that converts numbers to words
	ones = {0: '', 	1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'} # This is the dictionary for referencing elements (eys and values).
	tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
	teen = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen	'}

	user_input = str(user_input)
	n = len(user_input)
	i = 0

	answer = []
	if int(user_input) == 1000000:													# If user input is equal to 1000000 (max).
		print('one million') 

	if int(user_input) > 1000000: print('Input exceeds')							# If user input is greater than 1000000 (max).
	else:
		while i < n:																# This loop contains the whole process of conversion.
			if (((n-i) == 5) | ((n-i) == 2)) & (int(user_input[i]) == 1):			# If there is a special case of having 10 - 19 values in input in positions specified.
				answer.append(teen[int(user_input[i+1])])
				i = i + 1
			elif ((n-i) == 5) | ((n-i) == 2):										# If the current number is just in the in tens place without aggregates e.g. 10, 20, 30 etc.
				answer.append(tens[int(user_input[i])])
			else: # all else fail													# If the current num is just in the ones place.	
				answer.append(ones[int(user_input[i])])								
			if ((n-i) % 3 == 0) & ((int(user_input[i])) > 0):						# If the current number is in a hundred place.
				answer.append('hundred')
			if ((n-i) == 4):														# If the current number is in the thousand place.
				answer.append('thousand')
			i = i + 1

		print('Converted to Words:')
		for a in answer:															# Printing appended values in the answer list.
			print(a, end=' ')
		print('')



def wordsToNum(user_input):															# Function that converts words to numbers.
	
	numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, # This is the dictionary for referencing elements (eys and values).
			'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
			'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'hundred': 100, 'thousand': 1000, 'million': 1000000}

	user_input = user_input.split(' ')
	total, to_be_added, i  = 0, 0, 0

	while i < len(user_input):														# This loop contains the whole process of conversion.
		if (user_input[i] == 'million') | (user_input[i] == 'thousand'):			# If the current word is million or thousand (Indicates that 
			to_be_added = to_be_added * numbers[user_input[i]]						# it needs to be multiplied by million/thousand) and adds the
			total = to_be_added + total												# number to be added to the total.
			to_be_added = 0
		elif (user_input[i] == 'hundred'):											# If the current word needs to be multiplied by a hundred.
			to_be_added = to_be_added * numbers[user_input[i]]
			if i == (len(user_input)-1):											# This checks if the number multiplied with a hundred needs to be 
				total = to_be_added + total											# added to the total given that there is no million/thousand present.
				to_be_added = 0
		else:																		# Adds number in (to_be_added) before adding to the accumulator. 
			to_be_added = to_be_added + numbers[user_input[i]]	
			if i == (len(user_input)-1):											# This checks if the number multiplied with a hundred needs to be
				total = to_be_added + total											# added to the total given that there is no million/thousand present.
				to_be_added = 0
		i = i + 1

	print(total)

def wordsToCurrency(user_input, user_input_curr):									# Function that converts words to specified currency.
	if ((user_input_curr == 'PHP') | (user_input_curr == 'JPY') | (user_input_curr == 'USD')):
		print(user_input_curr, end='')												# Checks if the input for currency is valid. Prints the currency.
		wordsToNum(user_input)														# Calls the function/method wordsToNum for emphasis on modularity.
	else: print('Invalid Currency.')												# Invalid currency input.

		
def numberDelimited(user_input_num, user_input_char, user_input_jumps):				# Function that asks for character and number of jumps where the former will be added.
	input_len = len(user_input_num)
	input_jumps = int(user_input_jumps)
	n = 0

	if (input_jumps < input_len):													# This checks if the desired number of jumps is justified within
		user_input_list = []															# the bounds of the input number.

		while n < input_len:															# This loop is mainly used to put the values (per index) of string in a list
			user_input_list.append(user_input_num[n])									# for easier manipulation.
			n = n + 1

		user_input_list.insert(input_len-input_jumps, user_input_char)					# This line uses list method in python to insert a character in a specified place.
																						# This considers a simple formula (for proper placement) of length of input - number of desired jumps
		for element in user_input_list:
			print(element, end='')
	else: print('Invalid number of jumps (Out of bounds - string contains less elements than the desired number of jumps)')

	