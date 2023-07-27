class Dish:
    def __init__(self, name: str, description: str, price: float | int):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} x {self.price}'


class Category:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def __str__(self):
        return f'{self.name}\n' + '\n'.join(map(str, self.dishes))


class Menu:
    def __init__(self):
        self.categories = []

    def add_category(self, category: Category):
        self.categories.append(category)

    def __str__(self):
        return '\n'.join(map(str, self.categories))


# class Discount:
#     def __init__(self, value=0):
#         self.value = value
#
#     def discount(self):
#         raise NotImplementedError
#
#
# class RegularDiscount(Discount):
#     def __init__(self, value=5):
#         super().__init__(value)
#
#     def discount(self):
#         return 1 - self.value / 100
#
#
# class SilverDiscount(Discount):
#     def __init__(self, value=10):
#         super().__init__(value)
#
#     def discount(self):
#         return 1 - self.value / 100
#
#
# class GoldDiscount(Discount):
#     def __init__(self, value=20):
#         super().__init__(value)
#
#     def discount(self):
#         return 1 - self.value / 100

class Discount:
    def __init__(self, value=0):
        if not 0 <= value <= 100:
            raise InvalidDiscountError('Скидка должна быть в пределах 0-100%.')
        self.value = value

    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    def __init__(self, value=5):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100


class SilverDiscount(Discount):
    def __init__(self, value=10):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100


class GoldDiscount(Discount):
    def __init__(self, value=20):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100

class Order:
    def __init__(self):
        self.__dishes = []
        self.__quantities = []

    def add_dish(self, dish: Dish, quantity=1):
        if not isinstance(dish, Dish):
            raise TypeError('Error in Dish datatype')
        if not isinstance(quantity, int | float):
            raise TypeError('Error in quantity of dishes')
        if quantity <= 0:
            raise ValueError('Quantity must be > 0. But less or equal got')
        self.__dishes.append(dish)
        self.__quantities.append(quantity)

    def total(self, discount: Discount):
        summa = 0
        for item, quantity in zip(self.__dishes, self.__quantities):
            summa += item.price * quantity
        return summa * discount.discount()


class InvalidDiscountError(Exception):
    pass

if __name__ == "__main__":
    dish1 = Dish('Торт1', 'описание 1', 100)
    dish2 = Dish('Торт2', 'описание 2', 101)
    dish3 = Dish('Торт3', 'описание 3', 102)

    cat1 = Category('Категория 1')
    cat1.add_dish(dish1)
    cat1.add_dish(dish2)
    cat1.add_dish(dish3)

    menu = Menu()
    menu.add_category(cat1)

    print(menu)

    order = Order()

    try:
        order.add_dish(dish1, 2)
    except InvalidPriceError as e:
        print(f"Ошибка при добавлении блюда: {e}")
    else:
        try:
            discount = GoldDiscount(120)
        except InvalidDiscountError as e:
            print(f"Ошибка при установке скидки: {e}")
        else:
            print(order.total(discount))
