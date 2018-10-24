from tld import get_tld


class AddOneLetter:

    def __init__(self, url):
        self.url = url

    def add_one_letter(self):
        '''
            This function adds the same letter after the correct one
            tesla.com - ttesla.com - teesla.com - tessla.com - teslla.com - teslaa.com
        '''
        url = get_tld(self.url, as_object=True, fix_protocol=True)
        domain = url.domain

        new_urls_with_double_letter = []
        n = 0
        m = len(domain)
        while n < m:
            new_domain = domain[0:n] + domain[n] + domain[n] + domain[n+1:m]
            n = n + 1
            new_urls_with_double_letter.append(new_domain)

        return new_urls_with_double_letter







