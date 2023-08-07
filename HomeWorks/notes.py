import sys
from datetime import datetime
from typing import Final

file_path = 'notes.csv'
notes_list = []

NOTE_ID: Final = 0
NOTE_TITLE: Final = 1
NOTE_TEXT: Final = 2
NOTE_DATE: Final = 3


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
            notes_list.append(line.replace('\n', '').split(';'))


def notes_show():
    if len(notes_list) > 0:
        print('Кол-во заметок:' + str(len(notes_list)))
        print('==============================')
        for note in notes_list:
            print(str(
                int(note[NOTE_ID])) + ', ' +
                str(note[NOTE_TITLE]) + ', ' +
                str(note[NOTE_TEXT]) + ', ' +
                str(note[NOTE_DATE]))
    else:
        print('==============================')
        print('Заметки отсутствуют')
    print('==============================')


def note_new_id():
    max_id = 0
    for note in notes_list:
        if int(note[NOTE_ID]) > max_id:
            max_id = int(note[NOTE_ID])
    return max_id + 1


def note_add():
    note_list = []
    note_id = note_new_id()
    note_title = input('Введите заголовок: ')
    note_text = input('Введите заметку: ')
    note_date = datetime.now().__format__('%d.%m.%Y')
    note_list.append(note_id)
    note_list.append(note_title)
    note_list.append(note_text)
    note_list.append(note_date)
    notes_list.append(note_list)


def note_del(note_id):
    if note_id.isnumeric():
        for note in notes_list:
            if int(note[NOTE_ID]) == int(note_id):
                notes_list.remove(note)
    else:
        print('Не числовое значение')


def note_edit(note_id):
    for note in notes_list:
        if int(note[NOTE_ID]) == int(note_id):
            print('Заголовок: ' + note[NOTE_TITLE])
            print('Текст заметки: ' + note[NOTE_TEXT])
            note[NOTE_TEXT] = input('Введите новый текст заметки')
            note[NOTE_DATE] = datetime.now().__format__('%d.%m.%Y')
            notes_save()


def notes_save():
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for note in notes_list:
                note_str = str(note[NOTE_ID]) + ';' + note[NOTE_TITLE] + ';' + note[NOTE_TEXT] + ';' + note[NOTE_DATE]
                file.write(str(note_str) + '\n')
        print('Файл с заметками сохранен.')
    except IOError as io_err:
        print(io_err)


def main():
    print('==================================================================================')
    print('[add]-Добавить | [del]-Удалить | [edit]-Изменить | [save]-Сохранить | [exit]-Выход')
    print('==================================================================================')
    notes_show()
    in_str = input(">>")
    if in_str == 'add':
        note_add()
    elif in_str == 'del':
        note_del(input('Введите индекс заметки: '))
    elif in_str == 'edit':
        note_edit(input('Введите индекс заметки: '))
    elif in_str == 'save':
        notes_save()
    elif in_str == 'exit':
        return 'exit'


file_read(file_path)
while True:
    if main() == 'exit':
        notes_save()
        sys.exit()
    else:
        main()
