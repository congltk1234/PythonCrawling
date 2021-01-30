# Các thư viện cần thiết:
import requests
from bs4 import BeautifulSoup
import re
from requests import HTTPError


# Các hàm cần thiết:
# Nhập số lượng trang web cần tải về:
def input_max():
    while True:
        try:
            num = int(input('Số lượng trang web cần tải về:'))  # Nhập vào số tự nhiên
        except ValueError:
            print('Không phải là số tự nhiên, vui lòng nhập lại!\n' + '-' * 5)
            continue
        else:
            if num > 0:  # Nếu sô vừa nhập là số tự nhiên > 0 thì trả kết quả là số vừa nhập
                return num
            else:
                print('Hãy nhập lại số tự nhiên lớn hơn 0.')


# Nhập url:
def input_url():
    pattern = '[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    domain = input('Nhập url xuất phát:')
    # Vòng lặp yêu cầu người dung nhập đúng định dạng url
    while re.match(pattern, domain) is not None:
        domain = input('Url không hợp lệ, vui lòng nhập lại:')
        print('-' * 5)
    if 'https://' not in domain:
        domain = 'https://' + domain
    if domain[-1] == '/':
        domain = domain[0: -1]
        return domain
    else:
        return domain


# Kết quả trả về là 1 văn bản dạng chuỗi .txt
def parsing(url):
    # Gửi yêu cầu truy cập url
    try:
        raw_page = requests.get(url)
    except HTTPError:
        print("The server returned an HTTP error:")
    else:
        # Lấy code html của trang web được trả về theo url
        result = BeautifulSoup(raw_page.text, "html.parser")
        return result


# Lấy các đường link web trong nội dung đọc về:
# Kết quả trả về là 1 list chứa các link
def find_link(page_content, domain):
    """
    Lấy các đường link từ nội dung trang web
    :param page_content:nội dung của trang
    :param domain:url ban đầu
    :return: Set (chứa các link)
    """
    a_tags = page_content.find_all("a")
    result = set()
    for item in a_tags:
        link = item.get("href")
        if checkHTTP(link, domain):
            result.add(link)
        elif check_link(link):
            result.add(domain + link)
    return result


# Hàm kiểm tra link có chưa https/http hay không:
# Kết quả trả về:True nếu hợp lệ/False nếu không hợp lệ
def checkHTTP(item, domain):
    link = str(item)
    domain = str(domain)
    regex = re.compile(f'^({domain}).*')
    result = re.match(regex, link) is not None
    return result


# Hàm kiểm tra link có hợp lệ hay không:
# Kết quả trả về True/False
def check_link(item):
    link = str(item)
    #regex = '^/.*(html|htm|chn|api|[/])$'
    regex = '^/.*'
    result = re.match(regex, link) is not None
    return result
