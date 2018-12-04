from tld import get_tld


class RemoveOneLetter:

    def __init__(self, url):
        self.url = url

    def remove_letters(self):
        '''
            :return:
        '''
        url = get_tld(self.url, as_object=True, fix_protocol=True)
        domain = url.domain

        new_urls_without_letter = []
        n = 0
        m = len(domain)
        while n < m:
            new_domain = domain[0:n] + domain[n+1:m]
            n = n + 1
            new_urls_without_letter.append(new_domain)
        new_urls_list = list(set(new_urls_without_letter))
        return new_urls_list







