# -*- coding: utf-8 -*-
import argparse
import json
import urllib.parse
from modules.GoDaddyChecker import GoDaddy
from modules.Remover.RemoveOneLetter import RemoveOneLetter
from modules.Substitutions.HomoglyphAttack import HomoglyphAttack
from modules.Substitutions.Flipper import Flipper
from modules.Tldmodule.TldSelector import TldSelector
from modules.Urlchecker import checkvalidity


def main():
    print("""
 ___             __    _           ____
/ __> ___  _ _  /. | _| |_ ._ _ _ <__ /
\__ \/ . || | |/_  .| | |  | ' ' | <_ \\
<___/\_  |`___|  |_|  |_|  |_|_|_|<___/
       | |
\n""")

    parser = argparse.ArgumentParser(description='SquatMe v1.0 - Copyright @david3107')
    parser.add_argument('--url', dest='url', help='url to be squatted')
    parser.add_argument('--tld', dest='tld', type=bool, nargs='?',
                        const=True, default=True,
                        help='read the tld list form file db/top_domains and generate the domains. If not specified uses only .com')
    parser.add_argument('-A', dest='all', type=bool, nargs='?',
                        const=True, default=False, help='execute all the squatting attacks')
    parser.add_argument('-hg', dest='homoglyph', type=bool, nargs='?',
                        const=True, default=False, help='execute homoglyph attack ')
    parser.add_argument('-F', dest='flipper', type=bool, nargs='?',
                        const=True, default=False, help='execute flipping attack ')
    parser.add_argument('-R', dest='remove', type=bool, nargs='?',
                        const=True, default=False, help='remove one letter a time')
    #parser.add_argument('--output', dest='output', type=string, nargs='?',
    #                    const=True, default="stdout", choices=['stdout', 'file'], help='Output of the tool: stdout or file')
    #parser.add_argument('--output-format', dest='output_format', type=string, nargs='?',
    #                    const=True, default="text", choices=['text', 'json'], help='Format of the output of the tool')
    parser.add_argument('--available', dest='available', type=bool, nargs='?',
                        const=True, default=False,
                        help='lists only the available domains')

    args = parser.parse_args()
    url = args.url
    tld = args.tld
    available = args.available
    homoglyph = args.homoglyph
    flipper = args.flipper
    remove = args.remove
    #output = args.output
    #output_format = args.output_format
    all = args.all
    domains = []


    if url is None:
        print("--url field is mandatory")
        return

    if checkvalidity.check_valid_url(url):
        print("URL " + url + " is valid: let's squat\n")

        '''
        create the list of domains based on the attacks that were selected
        '''
        if remove or all:
            print("\n\x1b[6;30;42m" + "[*]Letter removal" + '\x1b[0m')
            step1 = RemoveOneLetter(url)
            domains = step1.remove_letters()

        if homoglyph or all:
            print("\x1b[6;30;42m[*] Homoglyph attack" + '\x1b[0m')
            step2 = HomoglyphAttack(url)
            step2.load_letters()
            domains = domains + step2.switch_letters()

        if flipper or all:
            print("\x1b[6;30;42m[*] Flipper attack" + '\x1b[0m')
            step3 = Flipper(url)
            domains = domains + step3.flip_letters()

        if len(domains) > 0:
            print("Exit: No domains have been generated!!")
            exit(1)

        if tld is False:
            tlds = ['com']
        else:
            tld_list = TldSelector(url)
            tlds = tld_list.generate_domains_from_top_tld

        godaddy = GoDaddy.GoDaddy()
        combined_domain_list = []

        for tld in tlds:
            try:
                for domain in domains:
                    complete_domain = domain + '.' + tld
                    response = godaddy.check_available_domain_get(complete_domain)
                    if len(response) > 0:
                        response = json.loads(response)
                        if available:
                            if response['ExactMatchDomain']['IsPurchasable']:
                                print('Domain ' + response['ExactMatchDomain']['Fqdn'] + ' is available: ' + str(
                                    response['ExactMatchDomain']['IsPurchasable']) + " - Price: " + str(response['Products'][0]['PriceInfo']['CurrentPrice']) + u"\xA3")

                        else:
                            print('Domain ' + response['ExactMatchDomain']['Fqdn'] + ' is available: ' + str(
                                response['ExactMatchDomain']['IsPurchasable']))

                    else:
                        print('Domain ' + urllib.parse.unquote(complete_domain) + ' : No info retrieved, try manually ')
                    combined_domain_list.append(complete_domain)
            except Exception as e:
                print(e)
                pass
    else:
        print("URL not valid. Exiting ...")
        return


if __name__ == "__main__":
    main()
