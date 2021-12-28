class Human:
    # static fields
    default_name = 'Default'
    default_age: int = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 100
        self.__house = 'Big'

    @property
    def money(self):
        return self.__money

    @property
    def house(self):
        return self.__house

    def info(self):
        print(self.name, self.age, self.money, self.house)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)


Human.default_info()


