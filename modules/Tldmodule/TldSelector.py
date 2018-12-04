# -*- coding: latin-1 -*-
from tld import get_tld
from configuration import config
import codecs


class TldSelector:
    def __init__(self, url):
        self.url = url
        self.db_path = config.DB['top_domains']

    @property
    def generate_domains_from_top_tld(self):
        top_domains = []
        with codecs.open(self.db_path, 'rU') as f:
            for line in f:
                top_domains.append(line.split('\n')[0])

        return top_domains
