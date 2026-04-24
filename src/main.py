from src.models.order import Order
from src.models.product import Product

goods = [
    Product("Мышь", 1500, 20),
    Product("Клавиатура", 3000, 15),
    Product("Ноутбук", 50000, 10)
]
goods.sort()
for product in goods:
    print(product)   
goods = Order(1, 50000, "Иван")
print(goods)

def check_stock(self):
    pass

def update_stock(self):
    pass


# ! коммент для коммита
#! второй коммент для коммита


# ! коммент для коммита на главной ветке