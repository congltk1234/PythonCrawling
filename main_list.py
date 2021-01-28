# Các thư viện cần thiết
import save
import web_op
import time


def start():
    # Nhóm các biến toàn cục cung cấp thông số cho chương trình:
    url_list = []  # Chứa các đường link sẽ được duyệt
    history = []  # Chứa các đường link đã duyệt
    count = 0  # Đếm số lượng trang web đã tải về

    save.creat_dir()
    # Kịch bản tải các trang web:  BeautifulSoup crawling script:
    domain = web_op.input_url()
    url_list.append(domain)
    max_page = int(input('Số lượng trang web cần tải:'))  # Quy định số lượng trang web được tải về
    while (count < max_page) and (len(url_list) > 0):
        url = url_list.pop(0)
        history.append(url)
        content = web_op.save_content(url)
        count += 1
        print(f'{count} : {url}')
        name = save.file_name(domain, url, count)
        save.write_file(name, content)
        page_content = web_op.parsing(url)
        # print(page_content)
        links = web_op.find_link(page_content, domain)  # links là 1 set chứa các link
        links = list(links)
        for item in links:  # Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            # Nếu đường link chưa hề được duyệt và chưa có trong hàng đợi:
            if item not in url_list and item not in history:
                url_list.append(item)  # Thêm đường link mới vào danh sách chờ duyệt.


if __name__ == '__main__':
    check = time.time()
    start()
    end = time.time()
    print(f"Runtime of the program is {end - check}")
