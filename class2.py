class Computer:
    def __init__(self, num1, num2):
        self.__first_number = num1
        self.__secoend_number = num2

    def sum(self):
        return self.__first_number + self.__secoend_number

    def get_first_number(self):
        return self.__first_number

    def set_first_number(self, number):
        self.__first_number = number
        return self.get_first_number()


class Laptop(Computer):
    def __init__(self, name, num1, num2):
        self.name = name
        Computer.__init__(self, num1, num2)

    def get_first_super_number(self):
        return super().get_first_number()

    # def set_first_super_number(self, value):
    #     super().set_first_number(value)
    #     return self._Computer__first_name


computer1 = Computer(4, 5)
laptop = Laptop("HP", 4, 5)
print(laptop.get_first_super_number())
print(laptop.set_first_super_number(56))
# print(laptop.get_first_super_number())
# print(laptop.set_first_super_number(10))
# first_number = computer1.get_first_number()
# print(first_number)
# first_number = computer1.set_first_number(6)
# print(first_number)
