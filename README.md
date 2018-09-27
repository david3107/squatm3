## About Squatm3 


<img src="http://pixelartmaker.com/art/7d89078b16bb7d7.png" width="300"/> <br>
Squatm3 is a python tool designed to enumerate available domains generated modifying the original domain name through different techniques:

-	Substitution attacks
-	Flipping attack
- 	Homoglyph attack fast (execute a fast homoglyph attack, mutating only one letter at the time )
-   Homoglyph attack complete (generates all the possible combinations)

Squatm3 will help penetration testers to identify domains to be used in phishing attack simulations and security analysts to prevent effective phishing attacks



## Installation

```
git clone https://github.com/david3107/squatm3.git
```

## Recommended Python Version:

Squatm3 currently supports only **Python 3** 


## Dependencies:

Squatm3 depends on the `tld` , `validators` and the `decorator>=4.1.2` python modules.

These dependencies can be installed using the requirements file:

- Installation on Windows:
```
c:\python33\python.exe -m pip install -r requirements.txt
```
- Installation on Linux
```
pip install -r requirements.txt
```

## Usage
```

 ___             __    _           ____
/ __> ___  _ _  /. | _| |_ ._ _ _ <__ /
\__ \/ . || | |/_  .| | |  | ' ' | <_ \
<___/\_  |`___|  |_|  |_|  |_|_|_|<___/
       | |


usage: squatme.py [-h] [--url URL] [--tld [TLD]] [-A [ALL]]
                  [-Hf [HOMOGLYPH_FAST]] [-Hc [HOMOGLYPH_COMPLETE]]
                  [-F [FLIPPER]] [-R [REMOVE]] [--godaddy [ENABLE_GODADDY]]
                  [--only-available [AVAILABLE]]

SquatMe v1.1 - @davide107

optional arguments:
  -h, --help            show this help message and exit
  --url URL             url to be squatted
  --tld [TLD]           read the tld list form file db/top_domains and
                        generate the domains. If not specified uses only .com
  -A [ALL]              execute all the squatting attacks
  -Hf [HOMOGLYPH_FAST]  execute a fast homoglyph attack, mutating only one
                        letter at the time
  -Hc [HOMOGLYPH_COMPLETE]
                        execute a complete homoglyph attack,generating all the
                        possible combinations (slow)
  -F [FLIPPER]          execute flipping attack
  -R [REMOVE]           remove one letter a time
  --godaddy [ENABLE_GODADDY]
                        checks on godaddy if the domain is available for sale
                        together with the price
  --only-available [AVAILABLE]
                        lists only the available domains for purchase
```

## License

Squatm3 is licensed under the GNU GPL license.

## Troubleshooting

If after the usage of the tool you do not get any results, it is possible that GoDaddy limited your IP. Workaround:

-	use VPN
- wait till your IP is allowed again

## Version
** Current version is 1.1 **
