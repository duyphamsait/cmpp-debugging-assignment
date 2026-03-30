import unittest
from buggy import Order


class TestOrder(unittest.TestCase):

    # Total should use quantity * price

    def test_total_uses_multiplication(self):
        # Arrange: create order with 2 iPhones, each $1000
        order = Order("Destiny Cooper", [("iPhone", 2, 1000.00)])

        # Act: calculate total
        total = order.calculate_total()

        # Assert: expected total = 2 * 1000 = 2000
        self.assertEqual(total, 2000.00)

    def test_total_multiple_items(self):
        # Arrange: 2 iPhones ($1000 each) and 3 iPads ($500 each)
        order = Order("Mahdi ElDani", [("iPhone", 2, 1000.00), ("iPad", 3, 500.00)])

        # Act
        total = order.calculate_total()

        # Assert: expected total = (2*1000) + (3*500) = 3500
        self.assertEqual(total, 3500.00)

    # Bug 4: empty order should return 0

    def test_total_empty_returns_zero(self):
        # Arrange: empty order
        order = Order("Ezequiel Montero", [])

        # Act
        total = order.calculate_total()

        # Assert: expected total = 0, not "Empty Order"
        self.assertEqual(total, 0)

    def test_total_empty_type_is_numeric(self):
        # Arrange
        order = Order("Duy Pham", [])

        # Act
        total = order.calculate_total()

        # Assert: expected type is numeric
        self.assertIsInstance(total, (int, float))

    # remove_item should remove all matches safely

    def test_remove_item_empty_list(self):
        # Arrange: empty list
        order = Order("Aariyana Sayani", [])

        # Act
        order.remove_item("iPhone")

        # Assert: expected list remains empty
        self.assertEqual(order.items, [])

    def test_remove_item_removes_all_matches(self):
        # Arrange: list contains duplicate "iPhone"
        order = Order("Destiny Cooper", [
            ("iPhone", 1, 1000.0),
            ("iPad", 1, 500.0),
            ("iPhone", 1, 1000.0)
        ])

        # Act
        order.remove_item("iPhone")

        # Assert: expected only "iPad" remains
        self.assertEqual(order.items, [("iPad", 1, 500.0)])

    def test_remove_item_no_match(self):
        # Arrange: no item named "MacBook"
        order = Order("Mahdi ElDani", [("iPhone", 1, 1000.0), ("iPad", 2, 500.0)])

        # Act
        order.remove_item("MacBook")

        # Assert: expected list unchanged
        self.assertEqual(order.items, [("iPhone", 1, 1000.0), ("iPad", 2, 500.0)])

    # Invalid discount code should return 0

    def test_discount_invalid_returns_zero(self):
        # Arrange
        order = Order("Ezequiel Montero", [("iPhone", 1, 1000.0)])

        # Act
        discount = order.apply_discount("SAVE30")

        # Assert: expected discount = 0 for invalid code
        self.assertEqual(discount, 0)

    def test_discount_empty_code_returns_zero(self):
        # Arrange
        order = Order("Duy Pham", [("iPhone", 1, 1000.0)])

        # Act
        discount = order.apply_discount("")

        # Assert: expected discount = 0
        self.assertEqual(discount, 0)

    def test_discount_save10(self):
        # Arrange
        order = Order("Aariyana Sayani", [("iPhone", 1, 1000.0)])

        # Act
        discount = order.apply_discount("SAVE10")

        # Assert: expected discount = 0.1 (10%)
        self.assertEqual(discount, 0.1)

    def test_discount_save20(self):
        # Arrange
        order = Order("Cooper, Destiny", [("iPhone", 1, 1000.0)])

        # Act
        discount = order.apply_discount("SAVE20")

        # Assert: expected discount = 0.2 (20%)
        self.assertEqual(discount, 0.2)


if __name__ == "__main__":
    unittest.main()