import validators


def check_valid_url(url):

    """

    :type url: string

    """
    return validators.domain(url)


