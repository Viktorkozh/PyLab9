#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date


if __name__ == '__main__':
    # Список людей со строками для демонстрации.
    people = [
        {'name': 'Иван', 'surname': 'Иванов', 'date_of_birth': [
            1, 2, 1990], 'zodiac_sign': 'Овен'},
        {'name': 'Мария', 'surname': 'Петрова', 'date_of_birth': [
            15, 7, 1985], 'zodiac_sign': 'Рак'},
        {'name': 'Алексей', 'surname': 'Сидоров', 'date_of_birth': [
            10, 11, 2000], 'zodiac_sign': 'Скорпион'},
        {'name': 'Елена', 'surname': 'Козлова', 'date_of_birth': [
            3, 4, 1995], 'zodiac_sign': 'Овен'},
        {'name': 'Сергей', 'surname': 'Игнатов', 'date_of_birth': [
            22, 9, 1982], 'zodiac_sign': 'Дева'},
        {'name': 'Анна', 'surname': 'Кузнецова', 'date_of_birth': [
            5, 12, 1988], 'zodiac_sign': 'Стрелец'}
    ]

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            name = input("Фамилия: ")
            surname = input("Имя: ")
            date_of_birth = list(map(int, input(
                "Введите дату рождения (в формате ДД.ММ.ГГГГ через точку): ").split('.')))
            zodiac_sign = input("Знак зодиака: ")

            # Создать словарь.
            person = {
                'name': name,
                'surname': surname,
                'date_of_birth': date_of_birth,
                'zodiac_sign': zodiac_sign
            }

            # Добавить словарь в список.
            people.append(person)
            # Отсортировать список по знакам Зодиака.
            people.sort(key=lambda item: item.get('zodiac_sign', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 20,
                '-' * 20,
                '-' * 15,
                '-' * 13 
            )
            print(line)
            print(
                '| {:^4} | {:^20} | {:^20} | {:^15} | {:^12} |'.format(
                    "№",
                    "Имя",
                    "Фамилия",
                    "Знак Зодиака",
                    "Дата рождения"
                )
            )
            print(line)

            # Вывести данные о всех людях.
            for idx, person in enumerate(people, 1):
                # Преобразование даты рождения в строку для вывода
                birth_date_str = '.'.join(
                    map(str, person.get('date_of_birth', '')))
                print(
                    '| {:^4} | {:<20} | {:<20} | {:<15} | {:<13} |'.format(
                        idx,
                        person.get('name', ''),
                        person.get('surname', ''),
                        person.get('zodiac_sign', ''),
                        birth_date_str
                    )
                )

            print(line)

        elif command.startswith('select '):
            # Разбить команду на части для выделения номера месяца.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый месяц.
            month = int(parts[1])

            # Инициализировать счетчик.
            count = 0
            # Проверить данные о людях из списка.
            for person in people:
                if person.get('date_of_birth', [])[1] == month:
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(count, person.get(
                            'name', ''), person.get('surname', ''))
                    )

            # Если счетчик равен 0, то люди не найдены.
            if count == 0:
                print("Люди, родившиеся в указанном месяце, не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print(
                "select <месяц> - вывод на экран информации о людях, родившихся в указанный месяц (цифра)")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
