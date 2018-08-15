from collections import OrderedDict

def reverseLowerUpper(list):
	additional = []
	for li in list:
		tmp = li.swapcase()
		if tmp not in list:
			additional.append(tmp)
	return list + additional

def lowerUpper(ch):
	result = []
	return result + [ch.lower(), ch.upper()]

def makeLoUp(str):
	if len(str) == 0:
		return [str]
	head = lowerUpper(str[0])
	remain = str[1:]
	if not remain:
	    return head
	permutations = makeLoUp(remain)
	new_permutations = []
	for perm in permutations:
	    for h in head:
	        new_permutations.append(h + perm)
	return new_permutations

def makeMulitLoUp(list):
	result = []
	for li in list:
		result += makeLoUp(li)
	return list(OrderedDict.fromkeys(result))

def isContainsUpper(alpha):
	return any(x.isupper() for x in alpha)


def heuristicLoUp(sequence):
	result = []
	for seq in sequence:
		if len(seq) == 0:
			result.append(seq)
			continue

		if(isContainsUpper(seq)):
			result.append(seq.swapcase())

		result.append(seq.lower())
		result.append(seq.upper())

		if len(seq) > 1:
			result.append(seq[0].upper() + seq[1:])
			result.append(seq[0] + seq[1:].upper())
	return list(OrderedDict.fromkeys(result))

def makeCombs(listLeft, listRight):
	result = []
	for le in listLeft:
		for ri in listRight:
			if le == "" or ri == "":
				result.append(le + ri)
				continue
			if le.lower() == ri.lower():
				continue
			if (le.lower()).find(ri.lower()) != -1 or (ri.lower()).find(le.lower()) != -1:
				continue
			result.append(le + ri)
	return result

def reduce(sequence, iter, initVal = False):
	if(initVal == False):
		initVal = sequence[0]
		sequence = sequence[1:]
	for seq in sequence:
		if(seq[0].isalpha()):
			# seq = makeMuseqtLoUp(seq)
			seq = heuristicLoUp(seq)
		initVal = iter(initVal, seq)
	return initVal

import tezos
def check(publicAddress, mnemonic, email, guess):
	return tezos.check(publicAddress, mnemonic, email, guess)

def force(check, perms, publicAddress, mnemonic, email):
	attempts = 0
	for guess in perms:
		attempts += 1
		guess = ''.join(guess)
		if check(publicAddress, mnemonic, email, guess) == 1:
			return (guess, attempts)

		print("- {:>20} - permutations: {:>8}".format(guess, attempts), end="\r")
	return False

def claimTezos(cases, publicAddress, mnemonic, email):
    for c in cases:
    	permutations = reduce(c, makeCombs, [""])
    	print("all possibles: ", len(permutations))
    	passwd = force(check, permutations, publicAddress, mnemonic, email)
    	if passwd:
    		print('Congrats! Your password is')
    		print(passwd[0])
    	else:
    		print()
    		print("Nope.. Modify candidates and try again..")
