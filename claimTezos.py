from heuristic import claimTezos
from itertools import product, permutations

# Step 1. Put your information in pdf
publicAddress = "tz1XuEaocsLyD7"
mnemonic = "flavoattoo near two hope"
email = "scom"

# Step 2. Spilt your password into meaning units
# For example if cadidates for your passwords are
# john0513, john2kate, Kate23!@, john!@#03
# then your passwords consist of alphabet, number and special character

alphabet = [
	"tkfka", "a", "cooking", "mnet", "qkqh", "qudtls", "patty", "addd"
]
alphabet = alphabet + test

number = [
	"1", "2", "1123", "147", "3874", "1527",
	# "62166216",
	"1004", "6216621", "6216"
]

special = [
	"!@", "!@#"
]

# (optional) Step 3.
# When you only remember which special characters you used,
# but you don't know how they are sequenced
# and you know how long they will be
# for example you are sure that you use only "!", "#" and "$"
mySpecial = "@#!"
minimumLength = 1
maximumLength = 2
duplicateSpecial = []
nonDuplicateSpecial = []
# duplicate
for lenNum in range(minimumLength, maximumLength + 1):
	for suf in product(mySpecial, repeat=lenNum):
		duplicateSpecial.append(''.join(suf))

# non duplicate
for lenNum in range(minimumLength, maximumLength + 1):
	for suf in permutations(mySpecial, lenNum):
		nonDuplicateSpecial.append(''.join(suf))

secondSpecial = list(set(duplicateSpecial) - set(nonDuplicateSpecial))


# word = ["tkfka", "slrzns", "skrzns", "skrskr", "kimsunlover", "sunlover",
# "skrtka", "slrtka", "skrtkaqnfrhrl", "qnfrhrl", "slrtkaqnfrhrl",
# "patskim", "patkim", "psumkim", "sumkim", "a", "qkqh", "sorsor", "skrdnscjswo", "cjswo",
# "gusskrdns", "nakun"]
# num = [
# 	"1", "2", "1123", "147", "3874", "1527", "6216621", "1004"
# ]

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
cases.append([alphabet, number, nonDuplicateSpecial, number, nonDuplicateSpecial])

cases.append([alphabet, nonDuplicateSpecial, number, nonDuplicateSpecial])
cases.append([alphabet, nonDuplicateSpecial, number, nonDuplicateSpecial, number])

# do not modify this
claimTezos(cases, publicAddress, mnemonic, email)
