from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.name!r}, {self.price}, {self.quantity}, {self.__number_of_sim})'

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def number_of_sim(self) -> int:
        """
        Геттер приватного параметра number_of_sim
        :return:
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        """
        Сеттер приватного параметра который проверяет, что длина наименования товара не больше 10 символов
        """
        if not isinstance(number_of_sim, float) and number_of_sim >= 1:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
