from random import choice


class Hang:
    def __init__(self):
        with open('C:\\Users\\dsyzranov\\PycharmProjects\\pythonProject1\\src\\06WordsStockRus.txt', 'r',
                  encoding='utf-8') as file:
            self.hidden_word = choice(file.readlines()).strip('\n')  # автоматическая генерация слова из словаря
        self.number_of_mistakes = 8
        self.game_field = self.hidden_word.replace(self.hidden_word, '_' * (len(self.hidden_word)))

    def mistakes(self, number_of_mistakes=int(input('Добро пожаловать в игру!\nВведите количество попыток: '))):
        self.number_of_mistakes = number_of_mistakes

    def set_letter(self, letter):  # подставляет литерал если он в поле
        # print(self.hidden_word)
        if letter not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' or letter not in self.hidden_word:
            self.number_of_mistakes -= 1
            self.check_win()
            return print(f'Такой буквы нет, осталось {self.number_of_mistakes} попыток\n{self.game_field}')

        for n, v in enumerate(self.hidden_word):
            if v == letter:
                tmp = list(self.game_field)
                tmp[n] = letter
                self.game_field = ''.join(tmp)
                self.number_of_mistakes -= 1
                print(f'Верно!\n{self.game_field}\nОсталось {self.number_of_mistakes} попыток')
        return self.check_win()

    def check_win(self):
        if self.hidden_word == self.game_field:
            self.number_of_mistakes = 0
            return print(f"Поздравляем это действительно {self.hidden_word}!")
        elif self.number_of_mistakes == 0:
            return print(f'Игра окончена вы проиграли\n{self.game_field}\nВерное слово "{self.hidden_word}"')
        else:
            return a


p1 = Hang()
p1.mistakes()
while p1.number_of_mistakes != 0:
    a = input('Введите букву ').lower()
    p1.set_letter(a)
