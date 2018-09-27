# -*- coding: latin-1 -*-
from tld import get_tld
import codecs
import urllib.parse
import itertools



class HomoglyphAttack:
    def __init__(self, url):
        self.url = url
        self.list_of_chars = []
        self.dictionary = {}

    def load_letters(self):
        '''
            :return:
        '''
        with codecs.open('db/homoglyph', 'rU', encoding='utf8') as f:
            for line in f:
                key_value = line.split('\n')[0].split(',')
                self.dictionary[key_value[0]] = key_value[1].split(' ')

    
    def switch_letters(self):
        
        '''
        The following function switches every single letter with a homoglyph

        '''

        url = get_tld(self.url, as_object=True, fix_protocol=True)
        domain = url.domain
        n = 0
        m = len(domain)

        domains = []
        try:
            while n < m:
                if n == 0:
                    j = 0
                    while j < len(self.dictionary[domain[n]]):
                        try:

                            letter = self.dictionary[domain[n]][j]

                            new_domain = letter + domain[n + 1:m]

                            domains.append(urllib.parse.quote(new_domain.encode('utf-8')))
                            j = j + 1
                        except Exception as e:
                            print(e)
                            j = j + 1
                            pass
                elif n == len(domain) - 1:
                    j = 0
                    while j < len(self.dictionary[domain[n]]):
                        try:
                            letter = self.dictionary[domain[n]][j]

                            new_domain = domain[0:n] + letter

                            domains.append(urllib.parse.quote(new_domain.encode('utf-8')))

                            j = j + 1
                        except Exception as e:
                            print(e)
                            j = j + 1
                            pass
                else:
                    j = 0
                    while j < len(self.dictionary[domain[n]]):
                        try:
                            letter = self.dictionary[domain[n]][j]
                            # encode utf-8 hex for Godaddy

                            new_domain = domain[0:n] + letter + domain[n + 1:m]
                            domains.append(urllib.parse.quote(new_domain.encode('utf-8')))

                            j = j + 1
                        except Exception as e:
                            print(e)
                            j = j + 1
                            pass

                n = n + 1
        except Exception as e:

            pass

        return domains

    def switch_all_letters(self):
        """
        The following function generates all the possible combinations using homoglyphs

        """
        domains = []
        url = get_tld(self.url, as_object=True, fix_protocol=True)
        domain = url.domain
        a = []
        for letter in domain:
            self.dictionary[letter].extend(letter)
            a.append(self.dictionary[letter])

        b = itertools.product(*a)

        for i in b:
            domains.append(urllib.parse.quote(''.join(i).encode('utf-8')))

        return domains










