# -*- coding: latin-1 -*-
from tld import get_tld
import codecs


class TldSelector:
    def __init__(self, url):
        self.url = url

    @property
    def generate_domains_from_top_tld(self):
        top_domains = []
        with codecs.open('db/top_domains', 'rU') as f:
            for line in f:
                top_domains.append(line.split('\n')[0])

        return top_domains
