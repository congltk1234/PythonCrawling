# Các thư viện cần thiết
import tek
import web_op
import time
import os


def start():
    # Nhóm các biến toàn cục cung cấp thông số cho chương trình:
    download_set = url_set = set()   # Tạo tập hợp rỗng
    folder = tek.creat_dir()  # Tạo thư mục lưu các file html
    domain = web_op.input_url()  # Nhập url xuất phát
    url_set.add(domain) # Thêm url xuất phát vào url_set
    max_page = web_op.input_max()  # Nhập số lượng trang web cần tải
    print('-'*50+'\nĐang tải...')
    check = time.time()  # Đặt mốc thời gian

    # Kịch bản tải các trang web:   BeautifulSoup crawling script:
    # Lặp thêm các url vào trong url_set
    # cho đến khi len(url_set) > = max page.
    while (len(url_set) > 0) and (len(download_set) < max_page):
        url = url_set.pop()  # Lấy ngẫu nhiên 1 url ra khỏi url_set
        download_set.add(url)   # Thêm url đó vào tập hợp các link chờ tải vể
        page_content = web_op.parsing(url)  # Phân tích source code của url vừa lấy ra
        found_links = web_op.find_link(page_content, domain)   # Tìm thêm url từ source code rồi gom thành 1 tập hợp
        found_links = found_links - download_set  # Trả về tập hợp đã loại đi những phần tử đã có trong download_set
        url_set = url_set | found_links  # Hợp tập hợp những url vừa tìm được vào tập hợp url_set
        download_set = download_set | url_set  # Hợp tập hợp url_set vào tập hợp download_set
    download_set = list(download_set)   # Chuyển set thành list
    download_list = download_set[0:max_page]  # Để giới hạn lại tùy theo số lượng trang cần tải về
    # Lặp tải các trang web về thư mục chỉ định
    for (index, url) in enumerate(download_list, 1):
        print(f'{index} : {url}')  # Hiển thị số thứ tự và link đang tải
        data = web_op.parsing(url)  # Phân tích source code của url
        tek.saveHTML(domain, url, index, data, folder)  # Tải source code về rồi lưu thành file .html
    end = time.time()  # Đánh dấu mốc thời gian kết thúc chương trình
    print('-'*50)
    print(f"Runtime of the program is {end - check}")  # Hiển thị thời gian chạy chương trình
    # Lưu những đường link đã tìm được vào file .txt
    os.chdir(folder)
    for (index, url) in enumerate(download_set, 1):
        tek.write_txt(index,url)
if __name__ == '__main__':
    start()
