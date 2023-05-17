import os  # Подключение модуля OS - адаптация пути к файлам в ОС.
import csv  # Подключение модуля CSV

BASE_PATH = os.path.abspath("src")  # Применение абсолютного пути.

FILE_CSV = "items.csv"        # нормальный файл
# FILE_CSV = "item.csv"  # несуществующий файл
# FILE_CSV = "items_err.csv"  # повреждённый файл

FILE_ITEMS = os.path.join(BASE_PATH, FILE_CSV)  # Полноценный путь к файлу


class InstantiateCSVError(Exception):
    """
    Общий класс исключения.
    """

    def __str__(self):
        print(f'InstantiateCSVError: ПОВРЕЖДЁН файл "{FILE_CSV}" \nПо адресу *{FILE_ITEMS}*.')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0  # Скидка
    all = []  # Список всего в ячейке памяти
    all_name = []  # Список всего наименованиями

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

        Item.all.append(self)
        Item.all_name.append(name)

    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.__name!r}, {self.price}, {self.quantity})'

    def __str__(self) -> str:
        return str(self.name)

    @property
    def name(self) -> str:
        """
        Геттер приватного параметра name
        :return:
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Сеттер приватного параметра который проверяет,
        что длина наименования товара не больше 10 символов
        """
        if len(name) <= 10:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __add__(self, other: int) -> int:
        """
        Складывать можно только объекты Item и дочерние от них.
        :param other:
        :return: int
        """
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @staticmethod
    def string_to_number(number: float) -> int:
        """
        Возвращает целое число ели будет десятичное
        :param number:
        :return: int
        """
        return int(float(number))

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Класс-метод, инициализирующий экземпляры класса Item данными
        из файла src/****.csv
        Проверяет на наличие файла и ошибки.
        :return: None
        """
        try:
            with open(FILE_ITEMS, "r", encoding='windows-1251') as csv_file:
                reader = csv.DictReader(csv_file)
                if 'name' not in reader.fieldnames or \
                        'price' not in reader.fieldnames or \
                        'quantity' not in reader.fieldnames:
                    raise InstantiateCSVError
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])

        except FileNotFoundError:
            print(f'FileNotFoundError: ОТСУТСТВУЕТ файл "{FILE_CSV}" \nПо адресу *{FILE_ITEMS}*.')
