#Các thư viện cần thiết:
import os, re

#Các hàm:


# Hàm tạo thư mục:
def creat_dir(folder):
    """
    Tạo và chuyển vị trí lưu đến thư mục vừa tạo (Thuộc ổ đĩa C)
    : directory:
    """
    while True:
        if not os.path.exists('C:\\'+folder):
            os.mkdir('C:\\'+folder)
            print("Folder '{}' đã được tạo.".format(folder))
            os.chdir('C:\\' + folder)
            print('-' * 50)
            break
        else:
            check = input("Folder '{}' tồn tại. Bạn có muốn lưu tại Folder này không? (y/n) ".format(folder))
            if check == 'y' or check == 'Y':
                print("Đã chuyển vị trí lưu đến thư mục '{}'.".format(folder))
                os.chdir('C:\\' + folder)
                print('-' * 50)
                break
            else:
                print('Vui lòng nhập tên thư mục:')


#Hàm tạo tên file html tự động (vd:"filename_index.html")
# Hàm tạo tên file tự động
def file_name(url,index):
    url = re.sub("^(https://www.|http://www.|https://|http://)", "", url)
    url = re.sub('\W', "", url)
    url = re.sub('(com)?',"",url)
    name = url + '_' + str(index)
    return name

# Creat a new file
def write_file(path, data):
    if not os.path.isfile(path+'.html'):
        f = open(path +'.html', 'wb')
        f.write(data)
        f.close()