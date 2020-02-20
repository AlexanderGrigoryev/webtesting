#
#  базовые классы для реализации паттернов
#


class Helper:
    """
    Помощник. Используется только для обозначения реализации паттерна.


    Пример использования:

    class ConcreteHelper(Helper):
        pass

    """
    pass


class Prototype:
    """
    Прототип. Используется только для обозначения реализации паттерна.


    Пример использования:

    class ConcretePro(Helper):
        pass

    """
    pass


class Product:
    """
    Продукт для реализации паттернов, конструирующих продукт.
    Используется только для обозначения


    Пример использования:

    class ConcreteProduct(Product):
        pass

    """
    pass


class Builder:
    """
    Строитель для реализации паттерна Строитель.

    def build_part_a(self):
        self.product = self.product + 'part_a'

    def build_part_b(self):
        self.product = self.product + 'part_b'

    def build_part_c(self):
        self.product = self.product + 'part_c'

    """

    def __init__(self, product=None):
        self.product = product


class BuilderDirector:
    """
    Директор для реализации паттерна Строитель.

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()

    """

    def __init__(self, builder):
        self.builder = builder


class Facade:
    """
    Фасад. Используется только для обозначения реализации паттерна.


    Пример использования:

    class ConcreteFacade(Facade):
        pass

    """
    pass


def singleton(cls):
    """
    Декоратор класса, который должен иметь только один экземпляр на сессию
    :param cls: оборачиваемый декоратором класс
    :return: единственный экземпляр класса


    Пример использования:

    @singleton
    class ConcreteSingleton:
        pass

    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
