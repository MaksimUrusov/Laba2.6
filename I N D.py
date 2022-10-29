
import sys

if __name__ == '__main__':
    # Список .
    manslist = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Название магазина",
                    "Товар",
                    "Цена"
                )
            )
            print(line)

            # Вывести данные о человеке.
            for idx, man in enumerate(manslist, 1):
                pr = man.get('price', '')
                print(
                    '| {:>4} | {:<30} | {:<20} | {:<20}  |'.format(
                        idx,
                        man.get('name', ''),
                        man.get('product', ''),
                        round(man.get('price',0), 2),
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            sel = parts[1]

            count = 0
            for man in manslist:
                if man.get('name') == sel:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, man.get('name', ''))
                    )
                    print('Товар:', man.get('product', ''))
                    print('Цена:', round( man.get('price', 0), 2)),

            # Если счетчик равен 0, то человек не найден.
            if count == 0:
                print("Магазин не найден.\n Вызвана комманда add: ")
                name = input("Название:  ")
                product = input("Товар ")
                price = input("Цена: ")

                # Создать словарь.
                man = {
                    'name': name,
                    'product': product,
                    'price': price,
                }

                # Добавить словарь в список.
                manslist.append(man)
                # Отсортировать список.
                if len(manslist) > 1:
                    manslist.sort(key=lambda item: item.get('date', ''))

        elif command == 'add':
            # Запросить данные .
            name = input("Название магазина:  ")
            product = input("Товар ")
            price = float(input("Цена: "))


            # Создать словарь.
            man = {
                'name': name,
                'product': product,
                'price': price,
            }

            # Добавить словарь в список.
            manslist.append(man)
            # Отсортировать список.
            if len(manslist) > 1:
                manslist.sort(key=lambda item: item.get('name', ''))

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить магазин;")
            print("list - вывести список магазинов;")
            print("select <товар> - показать товары из заданного магазина;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)