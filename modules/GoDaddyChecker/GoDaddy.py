from tld import get_tld
from configuration import config
import simplejson, requests
import urllib


class GoDaddy:
    def __init__(self):
        self.key = config.GODADDY['key']
        self.secret = config.GODADDY['secret']
        self.api_endpoints = config.GODADDY['api_endpoints']
        self.api_url = config.GODADDY['api_url']
        self.url = config.GODADDY['url']

    def get_available_tlds(self):
        tlds_available_path = self.api_endpoints[0]
        headers = {'Authorization': 'sso-key ' + self.key + ':' + self.secret}
        url = 'https://api.godaddy.com/' + tlds_available_path
        return requests.get(url, headers=headers)

    def check_available_domain_one(self, domain):
        available_domain = self.api_endpoints[1]
        headers = {'Authorization': 'sso-key ' + self.key + ':' + self.secret}
        url = self.api_url + available_domain + '?domain=' + domain
        response = requests.get(url, headers=headers)
        return response.content

    def check_available_domains(self, domains):
        available_domain = self.api_endpoints[1]
        headers = {'Authorization': 'sso-key ' + self.key + ':' + self.secret}
        url = self.api_url + available_domain

        payload = domains

        response = requests.post(url, headers=headers, json=payload)
        print(response.content)
        results = simplejson.loads(response.content.decode('utf-8'))

        return results

    def check_available_domain_get(self, domain):

        url = self.url + domain


        headers = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text / html, application / xhtml + xml, application / xml;',
            'Accept-Encoding': 'gzip, deflate'
        }
        cookie = {'currency': 'EUR'}

        response = requests.get(url,headers=headers, cookies=cookie)
        return response.content

