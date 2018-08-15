from heuristic import claimTezos
from itertools import product

# Step 1. Put your information in pdf
publicAddress = "put your tezos address which starts with tz1 here"
mnemonic = "put your 15 mneonic words in pdf here"
email = "put your email address in pdf here"

# Step 2. Spilt your password into meaning units
# For example if cadidates for your passwords are
# john0513, john2kate, Kate23!@, john!@#03
# then your passwords consist of alphabet, number and special character
alphabet = [
	"john", "kate", "Kate"
]
number = [
	"0513", "2", "23", "03"
]

special = [
	"!@", "!@#"
]

# (optional) Step 3.
# When you only remember which special characters you used,
# but you don't know how they are sequenced
# and you know how long they will be
# for example you are sure that you use only "!", "#" and "$"
mySpecial = "!#$"
minimumLength = 0
maximumLength = 3
mySpecialList = []
for tail in range(minimumLength, maximumLength + 1):
	for suf in product(special, repeat=tail):
		mySpecialList.append(''.join(suf))

# Step 4. Set sequences of password with your password group
# in our example in Step 2
# john0513, john2kate, Kate23!@, john!@#03
# sequces are
# 	john0513: alphabet, number
# 	john2kate: alphabet, number, alphabet
# 	Kate23!@: alphabet, number, special
# 	john!@#03: alphabet, special, number
# so your cases are 4
cases = []
cases.append([alphabet, number])
cases.append([alphabet, number, alphabet])
cases.append([alphabet, number, special])
cases.append([alphabet, special, number])
# if you are in the case of Step 3, then replace special into mySpecialList
# cases.append([alphabet, number])
# cases.append([alphabet, number, alphabet])
# cases.append([alphabet, number, mySpecialList])
# cases.append([alphabet, mySpecialList, number])

# do not modify this
claimTezos(cases, publicAddress, mnemonic, email)
