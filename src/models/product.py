class Product():
    def __init__(self, name, price, quantity):      
        self.name = name
        self.quantity = quantity

        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = price
            

    def __str__(self):
        return f"Товар {self.name}, Цена: {self.price}, Количество: {self.quantity}"

    def __lt__(self, other):
        if not isinstance(other, Product):
            return False
        return self.price < other.price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price


# ! добавил коментарий для конфликта