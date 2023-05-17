from src.items import Item

if __name__ == '__main__':
    # Файл item.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items_err.csv удалена последняя колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл items_err.csv поврежден.
