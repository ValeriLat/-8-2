class QueueNode:
    """Узел для элемента очереди"""
    def __init__(self, value):
        self.value = value  # Значение элемента
        self.next = None  # Ссылка на следующий узел


class Queue:
    """Реализация очереди на основе связного списка без счетчика _size"""
    def __init__(self):
        self.head = None  # Указатель на начало очереди
        self.tail = None  # Указатель на конец очереди

    def push(self, n):
        """Добавление элемента в конец очереди"""
        new_node = QueueNode(n)  # Создаем новый узел
        if self.tail is None:  # Если очередь пуста
            self.head = self.tail = new_node  # Новый узел становится и головой, и хвостом
        else:
            self.tail.next = new_node  # Привязываем новый узел к концу очереди
            self.tail = new_node  # Обновляем хвост очереди
        return "ok"

    def pop(self):
        """Удаление и возврат элемента из начала очереди"""
        if self.head is None:  # Если очередь пуста
            return "error"
        value = self.head.value  # Сохраняем значение головного узла
        self.head = self.head.next  # Перемещаем указатель головы на следующий узел
        if self.head is None:  # Если очередь стала пустой
            self.tail = None  # Обнуляем указатель хвоста
        return value

    def front(self):
        """Получение первого элемента без удаления"""
        if self.head is None:  # Если очередь пуста
            return "error"
        return self.head.value  # Возвращаем значение головного узла

    def size(self):
        """Получение текущего размера очереди (вычисляется динамически)"""
        count = 0  # Инициализируем счетчик
        current = self.head  # Начинаем с головного узла
        while current:  # Пока есть узлы
            count += 1  # Увеличиваем счетчик
            current = current.next  # Переходим к следующему узлу
        return count  # Возвращаем количество узлов

    def clear(self):
        """Очистка всей очереди"""
        self.head = self.tail = None  # Обнуляем указатели головы и хвоста
        return "ok"

    def print_queue(self):
        """Вывод всех элементов очереди"""
        if self.head is None:  # Если очередь пуста
            print("Очередь пуста")
            return

        current = self.head  # Начинаем с головного узла
        print("Содержимое очереди:", end=" ")  # Выводим начало сообщения
        while current:  # Пока есть узлы
            print(current.value, end=" ")  # Выводим значение узла
            current = current.next  # Переходим к следующему узлу
        print()  # Переход на новую строку


def main():
    """Основная функция программы"""
    queue = Queue()  # Создаем экземпляр очереди
    print(
        "МЕНЮ ПРОГРАММЫ ОЧЕРЕДЬ\n"
        "Добро пожаловать в программу очередь! Доступные команды:\n"
        "1. push <число> - Добавить число в очередь\n"
        "2. pop          - Удалить первый элемент\n"
        "3. front        - Показать первый элемент\n"
        "4. size         - Показать размер очереди\n"
        "5. clear        - Очистить очередь\n"
        "6. exit         - Выйти из программы\n"
        "Введите команду полностью (например: 'push 3')!"
    )

    while True:
        try:
            user_input = input("\nВведите команду: ").strip()
            if not user_input:
                continue  # Пропускаем итерацию
            parts = user_input.split()  # Разбиваем ввод на части
            command = parts[0]  # Первая часть - команда
            if command == "exit":
                print("bye")
                break
            elif command == "push":
                if len(parts) < 2:  # Если нет числа для добавления
                    print("Ошибка: после 'push' укажите число")
                else:
                    try:
                        num = int(parts[1])  # Пробуем преобразовать в число
                        print(queue.push(num))  # Добавляем число в очередь
                    except ValueError:
                        print("Ошибка: необходимо ввести целое число")
            elif command == "pop":
                result = queue.pop()  # Удаляем элемент из очереди
                print(result)
                if result != "error":  # Если удаление прошло успешно
                    print("Элемент удален")
            elif command == "front":
                print(queue.front())  # Выводим первый элемент
            elif command == "size":
                print(queue.size())  # Выводим размер очереди
            elif command == "clear":
                print(queue.clear())  # Очищаем очередь
                print("Очередь очищена")
            else:
                print(f"Неизвестная команда: {command}")
            queue.print_queue()  # Выводим текущее состояние очереди
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            continue

if __name__ == "__main__":
    main()