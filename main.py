
import os


data = {}
search_history = []

folder_name = "user_files"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

with open('Data\DictData.txt', 'r', encoding="utf-16", buffering=1) as file:
    for line in file:
        line = line.strip()
        if line.startswith('@'):
            key = line[1:].strip()
            data[key] = []
        elif line.startswith('*'):
            data[key].append({'type': line[1:].strip(), 'meanings': []})
        elif line.startswith('-'):
            if len(data[key]) > 0:
                data[key][-1]['meanings'].append(line[1:].strip())
            else:
                # Nếu danh sách rỗng, tạo một từ mới
                data[key].append({'type': '', 'meanings': [line[1:].strip()]})
        elif line.startswith('='):
            data[key][-1]['example'] = line[1:].strip()
        elif line.startswith('!'):
            data[key][-1]['idioms'] = line[1:].strip()

# tìm kiếm theo từ khóa
def search_word(keyword, data):
    search_history.append(keyword)
    for key, values in data.items():
        if keyword in key or any(keyword in meaning for value in values for meaning in value['meanings']):
            print(f"Word : {key}")
            for value in values:
                print(f"Type: {value['type']}")
                print("Meanings:")
                for meaning in value['meanings']:
                    print(f"- {meaning}")
                if 'example' in value:
                    print(f"Example: {value['example']}")
                if 'idioms' in value:
                    print(f"Idioms: {value['idioms']}")
#Người dùng tạo file  và add nó vào folder user_file
def create_file():
    filename = input("Nhập tên file mới: ")
    filepath = os.path.join("user_files", f"{filename}.txt")
    with open(filepath, 'w',encoding='utf-8') as file:
        print("File mới đã được tạo thành công.")
#Thêm từ vào file
def add_word_file():
    filename = input("Nhập tên file bạn muốn thêm từ vào: ")
    filepath = os.path.join("user_files", f"{filename}.txt")
    with open(filepath, "a", encoding="utf-8") as file:
        word = input("Nhập từ bạn muốn thêm: ")
        meaning = input("Nhập nghĩa của từ: ")
        file.write(f"{word}: {meaning}\n")
        print(f"Từ {word} đã được thêm vào file {filename}.")

# Xóa từ trong file
def delete_word_file():
    filename = input("Nhập tên file bạn muốn xóa từ: ")
    filepath = os.path.join("user_files", f"{filename}.txt")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            folder_user = {}
            for line in file:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(":")
                    folder_user[parts[0]] = parts[1]
        word = input("Nhập từ bạn muốn xóa: ")
        if word in folder_user:
            del folder_user[word]
            with open(filepath, "w", encoding="utf-8") as file:
                for word, meaning in folder_user.items():
                    file.write(f"{word}: {meaning}\n")
            print(f"Từ đã được xóa khỏi file {filename}.")
        else:
            print(f"Từ {word} không tồn tại trong file {filename}.")
    else:
        print(f"File {filename} không tồn tại.")
# Xen hết các từ trong file
def view_allword_file():
    filename = input("Nhập tên file bạn muốn xem: ")
    filepath = os.path.join("user_files", f"{filename}.txt")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            folder_user = {}
            for line in file:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(":")
                    folder_user[parts[0]] = parts[1]
        if len(folder_user) > 0:
            for word, mean in folder_user.items():
                print(f"{word}: {mean}")
        else:
            print(f"File {filename} không có từ nào.")
    else:
        print(f"File {filename} không tồn tại.")
# Xem lại lịch sử tìm kiếm
def view_history():
    print("Lịch sử tìm kiếm:")
    if len(search_history) == 0:
        print("Không có từ nào trong lịch sử tìm kiếm.")
    else:
        for i, keyword in enumerate(search_history):
            print(f"{i + 1}. {keyword}")
while True:
    print("1. Tra cứu")
    print("2. Xem lại các từ đã tìm kiếm")
    print("3. Tạo tệp của riêng bạn")
    print("4. Thoát chương trình")
    choice = input("Mời bạn nhập lựa chọn(1-4): ")
    if choice=='4':
        break
    elif choice == '1':
        word = input("Nhập từ bạn muốn tra cứu: ")
        keyword=key.lower()
        search_word(keyword, data)
    elif choice == '2':
        view_history()
    elif choice=="3":
        create_file()
        while True:
            choicefile=input("Bạn muốn làm gì" +"\n"
                             "1. Thêm từ"+"\n"
                             "2. Xóa từ"+"\n"
                             "3. Xem tất cả"+"\n"
                             "4. Thoát file"+"\n"
                             "Mời bạn nhập lựa chọn (1-4): ")
            if choicefile == "4":
                break
            elif choicefile=="1":
                add_word_file()
            elif choicefile=="2":
                delete_word_file()
            elif choicefile == "3":
                view_allword_file()
    else:
        print("Dữ liệu sai.Mời bạn nhập lại.")