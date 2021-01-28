# Các thư viện cần thiết
import save
import web_op
import time


def start():
    # Nhóm các biến toàn cục cung cấp thông số cho chương trình:
    history = url_set = set()

    save.creat_dir()  # Tạo thư mục lưu các file html
    domain = web_op.input_url()  # Nhập url xuất phát
    url_set.add(domain)
    max_page = web_op.input_max()  # Nhập số lượng trang web cần tải
    print('-'*50+'\nĐang tải...')
    check = time.time()
    while (len(url_set) > 0) and (len(history) < max_page):
        url = url_set.pop()
        history.add(url)
        page_content = web_op.parsing(url)
        wait = web_op.find_link(page_content, domain)
        url_set = url_set | (wait - history)
        history = history | url_set
    history = list(history)
    history = history[0:max_page]
    for (index, url) in enumerate(history, 1):
        content = web_op.save_content(url)
        print(f'{index} : {url}')
        name = web_op.file_name(domain, url, index)
        save.write_file(name, content)
        save.write_data(url)
    end = time.time()
    print('-'*50)
    print(f"Runtime of the program is {end - check}")


if __name__ == '__main__':
    start()
