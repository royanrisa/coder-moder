# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: GardenMarket
import unittest


class TestGardenMarket(unittest.TestCase):
    def test_product_creation(self):
        from gardenmarket import Product
        product = Product("Зеле", 100, "Банка")
        self.assertEqual(product.name, "Зеле")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.unit, "Банка")

    def test_order_creation(self):
        from gardenmarket import Order
        order = Order("Иван", 500.0, "Прочие")
        self.assertEqual(order.customer_name, "Иван")
        self.assertEqual(order.amount_due, 500.0)
        self.assertEqual(order.payment_method, "Прочие")

    def test_customer_creation(self):
        from gardenmarket import Customer
        customer = Customer("Мария", "+79001234567", "Адрес улицы 1")
        self.assertEqual(customer.name, "Мария")
        self.assertEqual(customer.phone, "+79001234567")

    def test_stock_creation(self):
        from gardenmarket import Stock
        stock = Stock("Помидоры", 5.0, "кг", 15)
        self.assertEqual(stock.product_name, "Помидоры")
        self.assertEqual(stock.quantity, 5.0)

    def test_data_entry_creation(self):
        from gardenmarket import DataEntry
        entry = DataEntry("2023-10-01", "10", "100.00")
        self.assertEqual(entry.date, "2023-10-01")

    def test_order_status(self):
        from gardenmarket import OrderStatus
        status = OrderStatus("Ожидает оплаты")
        self.assertEqual(status.status_text, "Ожидает оплаты")


if __name__ == "__main__":
    unittest.main()
