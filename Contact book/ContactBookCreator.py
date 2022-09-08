from PickleThing import *


class Member:
    member_number = 1

    def __init__(self, name: str, phone: int, address: str = None, nik: str = None):
        self.name = name
        self.phone = phone
        self.address = address
        self.nik = nik
        self.member_number = Member.member_number
        Member.member_number += 1

    @staticmethod
    def initialization_new_member():
        try:
            name = str(input('Введите имя'))
            phone = int(input('Введите номер'))
            address = input('Введите адрес')
            nik = input('Введите ник')
            contact = Member(name, phone, address, nik)
            change_file[contact.name] = [contact.phone, contact.address, contact.nik]
        except ValueError:
            print('Неверный ввод')
