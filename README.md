# Tz-Brute
Tezos password bruteforcer built on top of Arthur Breitman's fundraiser tools for validation.  

## Update:
##### 1) Installation on Linux
##### 2) Simple heuristic

## How to use:  
#### 1. Install the tool
#### 2. Run the tool
##### 1) When you don't remember your password at all.
##### Mac OS
     python main.py
##### Linux
     python3 main.py

##### 2) When you remember the candidates for your passwords
Modify and run claimTezos.py
##### Mac OS
     python claimTezos.py
##### Linux
     python3 claimTezos.py

## Install Guide:
#### Mac OS
[Installation on Mac Os](doc/Install_Mac.md)  

#### Linux
[Installation on Linux](doc/Install_Linux.md)  

#### Windows
###### coming soon
###
###
## Parameters:
##### Charset (1 - 6):
This is basically the characters that could be in your password, the lower the number and the less in the charset the better as it'll mean less permutations to test.
```
1| "0123456789"
2| "0123456789abcdefghijklmnopqrstuvwxyz"
3| "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
4| "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
5| "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
6| "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
```
##### Minimum (1 - ?):
This is the password length that the bruteforcer will start at, this can really help cut down on crack time by skipping the multitudes of permutations possible in lengths that you don't think your password would be.

##### Public key (e.g. tz1ABCDeF...):
This is the address you were given as your Tezos address upon contribution.

##### Email address:
This is the email address you used when you contributed. This is CASE SENSITIVE.

##### Mnemonic (e.g. apples cat radio...):
This is the mnemonic you received upon contribution, it will be within the PDF you downloaded. It's a long string of words all in lowercase separated by spaces.

## Reset:
Without resetting the script will start from where it last left off.  
You can reset your anchor.json by running:
```bash
python main.py reset
```
This will backup your anchor.json with a timestamp, remember to delete these when you're done as they will have your contribution details in them.

###
###
###
###
___
###
###
###

built by Jon - admin of the [unofficial Tezos Telegram](https://t.me/tezosplatform)  

web: [e.rroneo.us](http://e.rroneo.us/)  
email: [jon@e.rroneo.us](mailto:jon@e.rroneo.us)  
telegram: [@erroneous](https://t.me/erroneous)  

feel free to contact me with any questions!  


feeling generous?  

tez: tz1MDNRzDjHEXrMM17MeajYBBJwGVWBrgWhb  
eth: 0xbebb3c979daa3fbe89af4fb624c454ab842b18b3  
btc: 3NSczAYLbyhKpKACW2epwgxUZVfthbUHzR  
ltc: MDt9foDqjRhuCrWQhucYdJgCjXgASdShw9  
