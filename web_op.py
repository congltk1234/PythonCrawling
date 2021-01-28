# Các thư viện cần thiết:
import requests
from bs4 import BeautifulSoup
import re, csv
import urllib.request, urllib.error, urllib.parse
from requests import HTTPError
#from urllib import request


# Các hàm cần thiết:
# Nhập số lượng trang web cần tải về:
def input_max():
    while True:
        try:
            num = int(input('Số lượng trang web cần tải về:'))
        except ValueError:
            print('Không phải là số tự nhiên, vui lòng nhập lại!\n' + '-' * 5)
            continue
        else:
            if num > 0:
                return num
            else:
                print('Hãy nhập lại số tự nhiên lớn hơn 0.')


# Nhập url:
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


# Hàm đọc nội dung trang web:
def save_content(url):
    response = urllib.request.urlopen(url)
    result = response.read()
    return result


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
    :return: List (chứa các link)
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
    # regex = re.compile(r'^/.*(html|epi)$?')
    regex = '^/.*(html|api|[/])$'
    result = re.match(regex, link) is not None
    return result


# Hàm tạo tên file html tự động (vd:"filename_index.html")
# Hàm tạo tên file tự động
def file_name(domain, url, index):
    a = len(domain) + 1
    if '.html' in url:
        name = getTitle(url)
    else:
        if url == domain:
            name = 'TRANG CHỦ'
        else:
            #name = url[a:]
            name = re.sub(domain,'MỤC',url)
    name = re.sub('\W','_',name)
    name = str(index) + '_' + name
    return name


# Hàm lấy tiêu đề bài viết
def getTitle(url):
    html = urllib.request.urlopen(url).read().decode('utf8')
    html[:60]
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title')
    return str(title.string)
