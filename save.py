# Các thư viện cần thiết:
import os
import re


# Các hàm:
# Hàm tạo thư mục:
def creat_dir():
    """
    Tạo và chuyển vị trí lưu đến thư mục vừa tạo
    : directory:
    """
    while True:
        folder = input('Nhập tên thư mục bạn muốn tạo:')
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Folder '{}' đã được tạo.".format(folder))
            os.chdir(folder)
            print('-' * 50)
            break
        else:
            check = input("Folder '{}' tồn tại. Bạn có muốn lưu tại Folder này không? (y/n) ".format(folder))
            if check == 'y' or check == 'Y':
                print("Đã chuyển vị trí lưu đến thư mục '{}'.".format(folder))
                os.chdir(folder)
                print('-' * 50)
                break

# Creat a new file
def write_file(name, data):
    if not os.path.isfile(name + '.html'):
        f = open(name + '.html', 'wb')
        f.write(data)
        f.close()


def write_data(url):
    f = open('0_DownloadedLink.txt', 'a+')
    f.write(url+'\n')
    f.close()