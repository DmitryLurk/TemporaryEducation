from ContactBookCreator import *
from PickleThing import *
from ChangeContact import *


def action_choice():
    while True:
        choice_list = {'1': 'Member.initialization_new_member()',
                       '2': 'change_object()',
                       '3': 'del_contact()',
                       '4': 'show_contacts()',
                       '5': 'Работа завершена'}
        print('Выберите действие:\n\
            1 - Добавить контакт\n\
            2 - Изменить контакт\n\
            3 - Удалить контакт\n\
            4 - Показать контакты\n\
            5 - Закончить работу'
              )
        a = input('Выберите действие:   ')
        if a not in '12345':
            print('неверный ввод')
            continue
        elif a == '5':
            pickling(change_file)
            print(choice_list[a])
            break
        else:
            eval(choice_list[a])


action_choice()
