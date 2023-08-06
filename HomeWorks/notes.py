import sys

file_path = 'notes.csv'
notes_list = []


def file_read(file_path):
    try:
        file = open(file_path)
    except FileNotFoundError as file_not_found:
        print('Файл не найден: ' + file_not_found.filename)
        try:  # создаём новый
            file = open(file_path, 'w', encoding='utf-8')
            file.close()
        except IOError as io_err:
            print('Ошибка создания файла:' + io_err)
            # TODO: Дописать обработку ошибки
    else:
        for line in file:
            notes_list.append(line.replace('\n', ''))


def notes_show():
    if len(notes_list) > 0:
        print('Кол-во заметок:' + str(len(notes_list)))
        print('==============================')
        for note in notes_list:
            print(note)
    else:
        print('==============================')
        print('Заметки отсутствуют')
    print('==============================')


def note_new_id():
    max_index = 0
    for note in notes_list:
       if int(note[0]) > max_index:
           max_index = int(note[0])
    return str(max_index + 1)


def note_add():
    note_id = note_new_id()
    note_title = input('Введите заголовок: ')
    note_body = input('Ведеите текст заметки: ')
    notes_list.append(note_id + ';' + note_title + ';' + note_body)


def note_remove(note_id):
    for note in notes_list:
        if int(note[0]) == int(note_id):
            notes_list.remove(note)


def notes_save():
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for note in notes_list:
                file.write(str(note) + '\n')
    except IOError as io_err:
        print(io_err)


def main():
    notes_show()
    print('add \t - Добавить')
    print('save\t - Сохранить')
    print('del \t - Удалить')
    print('exit\t - Выход')
    in_str = input(">>")
    if in_str == 'add':
        note_add()
    elif in_str == 'save':
        notes_save()
    elif in_str == 'del':
        note_remove(int(input('Введите индекс заметки: ')))
    elif in_str == 'exit':
        return 'exit'


file_read(file_path)
while True:
    if main() == 'exit':
        notes_save()
        sys.exit()
    else:
        main()
