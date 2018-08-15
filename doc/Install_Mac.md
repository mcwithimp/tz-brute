## Mac OS
###### Just run ```run-osx.sh``` or follow the steps below:

Firstly you'll need to install Python 3 if you don't have it already.  
pyenv is a great way to manage multiple python installations, if you want to use pyenv open up a Terminal and run:  
```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
pyenv install 3.6.5
pyenv global 3.6.5
```  
If you don't want to use pyenv you can download Python 3 here:  
https://www.python.org/downloads/  

Next step is installing pip:
```bash
sudo easy_install pip
```  

Now we have pip we need to download and unzip this file:  
https://github.com/NODESPLIT/tz-brute/archive/master.zip  
You can then type "cd " into terminal (without brackets and with the space at the end) then drag and drop the newly unzipped folder into the terminal window and run the resulting command.  

We now need to install dependencies:
```bash
pip install -r requirements.txt
```

From here we can run Tz-Brute like so:
```bash
python main.py
```
