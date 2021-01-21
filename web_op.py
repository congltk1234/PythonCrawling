#Các thư viện cần thiết:
import requests
from bs4 import BeautifulSoup
import re

#Các hàm cần thiết:

#Hàm đọc nội dung trang web:
#Kết quả trả về là 1 văn bản dạng chuỗi .txt
def read_content(url):
    # Gửi yêu cầu truy cập url
    try:
        raw_page = requests.get(url)
        print('Đã nhận link.\n--------------------------')
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
    item = domain + item
    return item