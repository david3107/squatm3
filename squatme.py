# -*- coding: utf-8 -*-
import argparse, json, signal, sys
import urllib.parse
from modules.GoDaddyChecker import GoDaddy
from modules.Remover.RemoveOneLetter import RemoveOneLetter
from modules.Remover.AddOneLetter import AddOneLetter
from modules.Substitutions.HomoglyphAttack2 import HomoglyphAttack2
from modules.Substitutions.HomoglyphAttack import HomoglyphAttack
from modules.Substitutions.Flipper import Flipper
from modules.Tldmodule.TldSelector import TldSelector
from modules.Urlchecker import checkvalidity
from modules.Output import outputer
from modules.Classes import Domain
import os


def banner():
    print("""
 ___             __    _           ____
/ __> ___  _ _  /. | _| |_ ._ _ _ <__ /
\__ \/ . || | |/_  .| | |  | ' ' | <_ \\
<___/\_  |`___|  |_|  |_|  |_|_|_|<___/
       | |
\n""")


def signal_handler(sig, frame):
    sys.exit(0)


def prepare_arguments():
    global args, url, tld, available, homoglyph_fast,homoglyph_complete,enable_godaddy, flipper, remove, add, all_args, output, output_format

    parser = argparse.ArgumentParser(description='SquatMe v1.1 -  @davide107')
    parser.add_argument('--url', dest='url', help='url to be squatted')
    parser.add_argument('--tld', dest='tld', type=bool, nargs='?',
                        const=True, default=True,
                        help='read the tld list form file db/top_domains and generate the domains. If not specified uses only .com')
    parser.add_argument('-A', dest='all', type=bool, nargs='?',
                        const=True, default=False, help='execute all the squatting attacks')
    parser.add_argument('-Hf', dest='homoglyph_fast', type=bool, nargs='?',
                        const=True, default=False, help='execute a fast homoglyph attack, mutating only one letter at the time ')
    parser.add_argument('-Hc', dest='homoglyph_complete', type=bool, nargs='?',
                        const=True, default=False,
                        help='execute a complete homoglyph attack,generating all the possible combinations (slow) ')
    parser.add_argument('-F', dest='flipper', type=bool, nargs='?',
                        const=True, default=False, help='execute flipping attack ')
    parser.add_argument('-R', dest='remove', type=bool, nargs='?',
                        const=True, default=False, help='remove one letter a time')
    parser.add_argument ('--add', dest='add', type=bool, nargs='?',
                         const=True, default=False, help='add one letter a time')
    parser.add_argument('--godaddy', dest='enable_godaddy', type=bool, nargs='?',
                        const=True, default=False, help='checks on godaddy if the domain is available for sale together with the price')
    parser.add_argument('--output', dest='output', type=str, nargs='?',
                        const=True, default="text", choices=['text', 'json'], 
                        help='Output of the tool: text or json')
    parser.add_argument('--only-available', dest='available', type=bool, nargs='?',
                        const=True, default=False,
                        help='lists only the available domains for purchase')
    args = parser.parse_args()
    url = args.url
    tld = args.tld
    available = args.available
    homoglyph_fast = args.homoglyph_fast
    homoglyph_complete = args.homoglyph_complete
    enable_godaddy = args.enable_godaddy
    flipper = args.flipper
    remove = args.remove
    add = args.add
    output = args.output
    all_args = args.all

def print_out(msg):
    global output, out_messages, out_domains
    color = '\x1b[6;30;42m'
    color_end = '\x1b[0m'
    if output == 'text':
        if isinstance(msg, Domain.Domain):
            if msg.no_info:
                outputer.print_text_to_console(msg.fqdn + " - No info retrieved, try manually")
            elif msg.price:
                outputer.print_text_to_console (
                    msg.fqdn + " is available - Price: " + msg.price)
            else:
                outputer.print_text_to_console(msg.fqdn + " is not available")
        elif isinstance(msg, list):
            for d in msg:
                outputer.print_text_to_console(d.fqdn + " - No info retrieved, try manually")   
        else:
            outputer.print_text_to_console(color + "[*]" +str(msg) + color_end)
            
    if output == 'json':
        if isinstance(msg, type(Domain.Domain)):
            out_domains.append(msg)
        elif isinstance(msg, list):
            out_domains=msg
        else:
            out_messages.append(msg)
            if msg == "Done!":
                outputer.print_json_to_console(out_messages, out_domains)




def prepare_list_domains_based_on_input():
    '''
    create the list of domains based on the attacks that were selected
    '''
    domains = []
    if remove or all_args:
        print_out("Letter removal")
        step1 = RemoveOneLetter(url)
        domains = step1.remove_letters()

    if homoglyph_fast or all_args:
        print_out("Fast Homoglyph attack")
        step2 = HomoglyphAttack(url)
        step2.load_letters()
        domains = domains + step2.switch_letters()
        #step2.switch_letters()
        #step2.switch_all_letters()

    if homoglyph_complete or all_args:
        print_out("Complete Homoglyph attack (slow)")
        step2 = HomoglyphAttack(url)

        #step2 = HomoglyphAttack2(url)

        step2.load_letters()
        domains = domains + step2.switch_all_letters()


    if flipper or all_args:
        print_out("Flipper attack")
        step3 = Flipper(url)
        domains = domains + step3.flip_letters()

    if add or all_args:
        print_out("Duplicate attack")
        step4 =  AddOneLetter(url)
        domains = domains + step4.add_one_letter()

    # Moved from modules, not sure if needed here
    #if len(domain) < 4: 
    #        print_out("With domains with less than 4 letters, this check is not accurate\n")

    if len(domains) == 0:
        print_out("Exit: No domains have been generated!! Did you specify the attack(s)?")
        exit(1)
        
    return domains


def check_required_params():
    global url
    if url is None:
        print_out("--url field is mandatory")
        exit(0)

    if not checkvalidity.check_valid_url(url):
        print_out("URL not valid. Exiting ...")
        exit(0)


def check_domain_availability(domains):
    global tld, url
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
                result_domain = Domain.Domain()
                if enable_godaddy == True:
                    response = godaddy.check_available_domain_get(complete_domain)
                    os.system('sleep 0.9')
                    if len(response) > 0:
                        response = json.loads(response)
                        if available:
                            if response['ExactMatchDomain']['IsPurchasable']:
                                result_domain.fqdn = str(response['ExactMatchDomain']['Fqdn'])
                                result_domain.purchasable = str(response['ExactMatchDomain']['IsPurchasable'])
                                result_domain.price = str(response['Products'][0]['PriceInfo']['CurrentPrice'])
                                result_domain.no_info = False
                                print_out(result_domain)

                        else:
                            result_domain.fqdn = str(response['ExactMatchDomain']['Fqdn'])
                            result_domain.purchasable = str(response['ExactMatchDomain']['IsPurchasable'])
                            result_domain.price = str (response['Products'][0]['PriceInfo']['CurrentPrice'])
                            print_out(result_domain)

                    else:
                        result_domain.fqdn = urllib.parse.unquote(complete_domain);
                        result_domain.no_info = True
                result_domain.fqdn = urllib.parse.unquote(complete_domain);
                combined_domain_list.append(result_domain)
        except Exception as e:
            print_out(str(e))
            pass

    if enable_godaddy == False and len(combined_domain_list) > 0:
        try:
            print_out(list(set(combined_domain_list)))
        except Exception as e:
            print(str(e))
            pass
    print_out("Total: " + str(len(list(set(combined_domain_list)))))
    print_out("Done!")

def main():
    banner()
    prepare_arguments()
    check_required_params()
    domains = prepare_list_domains_based_on_input()
    check_domain_availability(domains)


if __name__ == "__main__":
    args = url = tld = available = homoglyph_fast = enable_godaddy = flipper = remove = add = all_args = output = None
    out_messages = out_domains = []
    signal.signal(signal.SIGINT, signal_handler)
    main()
