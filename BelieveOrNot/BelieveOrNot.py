import csv


class GameBelieve:
    def __init__(self, pass_to_file: str):
        self.pass_to_file = pass_to_file
        self.mistake_count = 3
        self.winner_score = 3
        self.game_list = []
        with open(f'{self.pass_to_file}\\08Questions.csv', newline='') as file:
            game_file = csv.reader(file, delimiter=';')
            for row in game_file:
                row = row[0].split(';')
                self.game_list.append(row)

    def question(self):
        for i in self.game_list:
            return print(i[0])

    def answer_check(self, answer: str):
        if answer.lower() in 'yn':
            if answer == 'y':
                return self.game_process('Yes')
            else:
                return self.game_process('No')
        else:
            print('Неверный ввод. Введите y или n.')

    def game_process(self, answer):
        if answer == str(self.game_list[0][1]):
            comment = [self.game_list[0][2]]
            print(f'Верно! {comment}')
            self.winner_score -= 1
            self.game_list.pop(0)
        else:
            comment = [self.game_list[0][2]]
            print(f'Неправильно. {comment}')
            self.mistake_count -= 1
            self.game_list.pop(0)


game = GameBelieve(input('Укажите путь к файлу:'))


def initialization():
    try:
        if game.mistake_count:
            game.mistake_count = int(input('Введите количество допустимых ошибок: '))
        if game.winner_score:
            game.winner_score = int(input('Введите количество очков до победы: '))
    except ValueError:
        print('Неверный ввод, введите число')
        initialization()


initialization()

while game.mistake_count != 0:
    game.question()
    game.answer_check(input('y или n?'))
    if game.winner_score == 0:
        print('Поздравляю вы выиграли')
        break
    if game.mistake_count == 0:
        print('Игра окончена вы проиграли')
        break
