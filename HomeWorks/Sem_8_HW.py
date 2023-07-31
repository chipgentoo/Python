file_path = "tel_sprav.csv"


def file_read(filepath):
    with open(filepath, 'r+', encoding='utf-8') as file:
        return file.read()


def showtel(filepath):
    print('===========================================')
    for record in file_read(filepath).split('\n'):
        print(record)
    print('===========================================')


def rec_add():
    family = input("Введите Фамилию: ")
    name = input("Введите Имя: ")
    parent = input("Введите Отчество: ")
    telephone = input("Введите телефон: ")
    return family + ';' + name + ';' + parent + ';' + telephone + ';\n'


def rec_find():
    print('===========================================')
    element = input("Введите строку для поиска: " + "\n")
    for user in file_read(file_path).split(";"):
        for userDetail in user.split("\n"):
            if userDetail.lower() == element.lower():
                print("Найдено: " + user)
    print('===========================================')


def rec_write():
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(rec_add())


def main():
    showtel(file_path)
    print('add \t - Добавить')
    print('find\t - Поиск')
    print('end \t - Выход')
    in_str = input(">>")
    if in_str == 'add':
        rec_write()
    elif in_str == 'find':
        rec_find()
    elif in_str == 'end':
        return 'end'


while True:
    if main() == 'end':
        break
    else:
        main()
