from time import sleep

from PickleThing import *


def show_contacts():
    print(change_file)


def del_contact():
    try:
        name = input('Введите имя для удаления: ')
        del change_file[name]
    except KeyError:
        print('Имя не существует или введено неверно')


def change_object():
    print('Что хотите изменить?\n\
          1-Имя\n\
          2-Телефон\n\
          3-Адрес\n\
          4-Ник')
    index = input('')
    if index in '1234':
        if index == '1':
            contact_name = input('Введите имя изменяемого контакта')
            new_value = input('Введите новое значение')
            change_file[new_value] = change_file[contact_name]
            del change_file[contact_name]
        else:
            contact_name = input('Введите имя изменяемого контакта')
            sleep(1)
            new_value = input('Введите новое значение')
            change_file[contact_name][int(index) - 2] = new_value
            print(change_file)
    else:
        print('Неверный ввод')
