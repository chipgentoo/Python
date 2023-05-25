file_path = "tel_sprav.csv"

def file_read(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        return file.read()

def showTel(file_path):
    print('===========================================')
    for record in file_read(file_path).split('\n'):
        print(record)
    print('===========================================')

def rec_add():
    family = input("Введите Фамилию: ")
    name = input("Введите Имя: ")
    parent = input("Введите Отчество: ")
    telephone = input("Введите телефон: ")
    return (family + ';' + name + ';' + parent + ';' + telephone + ';\n')

def rec_find():
    print('===========================================')
    element = input("Введите строку для поиска: " + "\n")
    for user in file_read(file_path).split(";"):
        for userDetail in user.split("\n"):
            if userDetail.lower() == element.lower():
                print("Найдено: " +  user)
    print('===========================================')

def rec_write():
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(rec_add())

def Main():
    showTel(file_path)
    print('add\t - Добавить')
    print('find\t - Поиск')
    print('end\t - Выход')
    in_str = input()
    if in_str == 'add':
        rec_write()
    elif in_str == 'find':
        rec_find()
    elif in_str == 'end':
        return 'end'

while True:
    if Main() == 'end':
        break
    else:
        Main()
