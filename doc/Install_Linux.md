## Linux
#####  

Firstly you'll need to install python3-dev, git if you don't have it already.  
Open up a Terminal and run:  
```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y git
sudo apt-get install python3-dev
```  
If you encounter this message when 'sudo apt-get update':
######  
```could not get lock /var/lib/apt/lists/lock - …```
```bash
sudo rm /var/lib/apt/lists/lock
sudo apt-get update
```

If you encounter this message when 'sudo apt-get install -y git':
######  
```could not get lock /var/lib/dpkg/lock - …```
```bash
sudo rm /var/lib/apt/lists/lock
sudo dpkg --configure -a
sudo apt-get install -y git
```

Next step is installing pip:
```bash
sudo apt-get install python3-pip
```  

Now we have pip we need to download and unzip this file:  
https://github.com/mcwithimp/tz-brute/archive/master.zip  
You can then type "cd " into terminal (without brackets and with the space at the end) then drag and drop the newly unzipped folder into the terminal window and run the resulting command.  
Or
```bash
git clone git@github.com:mcwithimp/tz-brute.git
cd tz-brute
```

We now need to install dependencies:
```bash
pip3 install --upgrade setuptools --user
pip3 install pysodium --user
pip3 install -r requirements.txt --user
```

From here we can run Tz-Brute like so:
```bash
python3 main.py
```
If you have a trouble, this may be because you already have installed python3 before:
```bash
python3.5 main.py
```
