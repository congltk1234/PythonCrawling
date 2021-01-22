#Các thư viện cần thiết:
import requests
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error, urllib.parse

#Các hàm cần thiết:
#Hàm đọc nội dung trang web:
def save_content(url):
    response = urllib.request.urlopen(url)
    result = response.read()
    return result


#Kết quả trả về là 1 văn bản dạng chuỗi .txt
def parsing(url):
    # Gửi yêu cầu truy cập url
    try:
        raw_page = requests.get(url)
    except HTTPError as e:
        print("The server returned an HTTP error")
    except URLError as e:
        print("The server could not be found!")
    else:
        raw_page = requests.get(url)
    # Lấy code html của trang web được trả về theo url
        result = BeautifulSoup(raw_page.text, "html.parser")
        return result


#Lấy các đường link web trong nội dung đọc về:
#Kết quả trả về là 1 list chứa các link
def catchlink(page_content):
    """
    Lấy các đường link từ nội dung trang web
    :param page_content:
    :return: List (chứa các link)
    """
    a_tags = page_content.find_all("a")
    result = []
    for item in a_tags:
        link = item.get("href")
        result.append(link)
    return result


# Hàm kiểm tra link có chưa https/http hay không:
# Kết quả trả về:True nếu hợp lệ/False nếu không hợp lệ
def checkHTTP(item):
    link = str(item)
    regex = re.compile(r'^(http://|https://)')
    result = re.match(regex, link) is not None
    return result


# Hàm kiểm tra link có hợp lệ hay không:
# Kết quả trả về True/False
def check_link(item):
    link = str(item)
    regex = re.compile(r'^/\w/')
    result = re.match(regex, link) is not None
    return result


#Hàm chỉnh sửa đường link nếu đường link không đầy đủ:
#Kết quả trả về là 1 đường link đầy đủ.
def editlink(domain,item):
    """
    Hàm chỉnh sửa đường link bị thiếu tên miền
    :param domain: Tên miền
    :param item: Đường link bị thiếu
    :return:
    """
    item = domain + item
    return str(item)