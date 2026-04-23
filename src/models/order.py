class Order():
    def __init__(self, order_id, total, user):
        self.total = total
        self.user = user

        if order_id is None:
            raise KeyError("Товар не найден")
        self.order_id = order_id

    def __str__(self):
        return f"Заказ #{self.order_id} на сумму {self.total} руб (Пользователь: {self.user})"

