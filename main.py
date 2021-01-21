#Các thư viện cần thiết
import save , web_op


def start():
    #Nhóm các biến toàn cục cung cấp thông số cho chương trình:
    url_list = []    #Chứa các đường link sẽ được duyệt
    history = []    #Chứa các đường link đã duyệt
    max_page = 10 #Quy định số lượng trang web được tải về
    count = 0   #Đếm số lượng trang web đã tải về

    folder = input('Nhập tên thư mục bạn muốn tạo:')
    save.creat_dir(folder)
    #Kịch bản tải các trang web:  BeautifulSoup crawling script:
    url = input('Nhập url xuất phát:')
    url_list.append(url)
    while (count < max_page) and (len(url_list)>0):
        url = str(url_list.pop(0))
        page_content = web_op.read_content(url)
        links = web_op.catchlink(page_content)  #links là 1 list chứa các link
        for item in links:  #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if web_op.checkHTTP(item):  #Nếu đường link là hợp lệ thì tiếp tục thực hiện bên dưới:
                if (item not in url_list) and (item not in history):    #Nếu đường link chưa hề được duyệt và chưa có trong hàng đợi:
                    url_list.append(item)   #Thêm đường link mới vào danh sách chờ duyệt.
            elif web_op.check_link(item):
                item = web_op.editlink(url, item)
                if (item not in url_list) and (item not in history):
                    url_list.append(item)
            history.append(item)

        count += 1

'''
        save.save_content(page,data_folder)
        history.append(url)
        count +=1
'''


if __name__ == '__main__':
    start()
