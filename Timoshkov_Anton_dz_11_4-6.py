class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:

    def __init__(self):
        # создаем словарь с товарами
        self.dict_product = {
            'Printer': 0,
            'Scanner': 0,
            'Copier': 0
        }

    @staticmethod
    def chek_valid(param_1: str):
        if param_1.isdigit():
            param_1 = int(param_1)
            return param_1
        else:
            raise OwnError('Нужно ввести число!')

    # метод приема товара на склад
    def acceptance(self, name, amt):
        self.dict_product[name] = self.dict_product.get(name) + Store.chek_valid(amt)

    # метод передачи товара со склада
    def transfer(self, name, amt):
        self.dict_product[name] = self.dict_product.get(name) - Store.chek_valid(amt)
        if self.dict_product.get(name) < 0:
            print(f"Не хватает {abs(self.dict_product.get(name))} товаров")


# Если я правильно понял, то классы ниже нужны только для просмотра информации о продукте
class Equipment:
    def __init__(self):
        self.manufacturer = '༼ つ ◕_◕ ༽つ'


class Printer(Equipment):
    def __init__(self):
        super().__init__()
        self.brand = 'Принтер'


class Scanner(Equipment):
    def __init__(self):
        super().__init__()
        self.brand = 'Сканер'


class Copier(Equipment):
    def __init__(self):
        super().__init__()
        self.brand = 'Ксерокс'


a = Store()

# Что бы улучшить код, можно в цикле while запрашивать данные у пользователя и если он ввел не число, ловить raise
# и просить ввести число

print(Printer().manufacturer, Printer().brand)

a.acceptance('Printer', '2')
print(a.dict_product)
a.transfer('Printer', 'g')
print(a.dict_product)

