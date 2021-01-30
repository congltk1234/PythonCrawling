def input_url():
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    domain = input('Nhập url xuất phát:')
    while re.match(pattern, domain) is None:
        domain = input('Url không hợp lệ, vui lòng nhập lại:')
        print('-' * 5)
    if domain[-1] == '/':
        domain = domain[0: -1]
        return domain
    else:
        return domain