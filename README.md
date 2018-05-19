## About Squatm3 

Squatm3 is a python tool designed to enumerate available domains generated modifying the original domain name through different techniques:

-	Substitution attacks
-	Flipping attack
- 	Homoglyph attack

Squatm3 will help penetration testers to identify domains to be used in phishing attack simulations and security analysts to prevent effective phishing attacks



## Installation

```
git clone https://github.com/david3107/squatm3.git
```

## Recommended Python Version:

Sublist3r currently supports only **Python 3** 


## Dependencies:

Squatm3 depends on the `tld` , `validators` and the `decorator-4.1.2` python modules.

These dependencies can be installed using the requirements file:

- Installation on Windows:
```
c:\python33\python.exe -m pip install -r requirements.txt
```
- Installation on Linux
```
sudo pip install -r requirements.txt
```

##Usage
```
usage: squatme.py [-h] [--url URL] [--tld [TLD]] [-A [ALL]] [-hg [HOMOGLYPH]]
                  [-F [FLIPPER]] [-R [REMOVE]] [--available [AVAILABLE]]

SquatMe v1.0 - Copyright @wh1teInk

optional arguments:
  -h, --help            show this help message and exit
  --url URL             url to be squatted
  --tld [TLD]           read the tld list form file db/top_domains and
                        generate the domains. If not specified uses only .com
  -A [ALL]              execute all the squatting attacks
  -hg [HOMOGLYPH]       execute homoglyph attack
  -F [FLIPPER]          execute flipping attack
  -R [REMOVE]           remove one letter a time
  --available [AVAILABLE]
                        lists only the available domains
```

## License

Squatm3 is licensed under the GNU GPL license.


## Version
**Current version is 1.0**