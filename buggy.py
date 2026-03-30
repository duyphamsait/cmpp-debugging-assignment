# order_management.py

class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items  

    def calculate_total(self):
        total = 0
        for item in self.items:
            # FIX (Bug 7): Use multiplication (quantity * price) instead of addition
            total += item[1] * item[2]  
        if total == 0:  
            # FIX (Bug 4): Return 0 instead of "Empty Order" for consistent numeric type
            return 0              

        return total

    def add_item(self, item_name, quantity, price):
        self.items.append((item_name, quantity, price))  

    def remove_item(self, item_name):
        if len(self.items) == 0:
            print("List is empty, no items to remove")
            # FIX (Bug 2): Stop execution if the list is empty
            return            

        # Step 1: Make empty shopping cart
        new_items = []
        # Step 2: Walk through old cart
        for item in self.items:
            # Step 3: Check "Is this the one to throw?"
            if item[0] != item_name:
                # Step 4: Keep it in new cart
                new_items.append(item)
        # Step 5: Replace old cart with clean one
        self.items = new_items

    def print_summary(self):
        print("Order Summary for", self.customer_name)
        for item in self.items: 
            print(f"{item[1]} x {item[0]} @ ${item[2]:.2f}")
        print("Total: $", self.calculate_total())

    def apply_discount(self, code):
        if code == "SAVE10":
            return 0.1
        elif code == "SAVE20":
            return 0.2
        else:
            # FIX (Bug 3): Add default return 0 at the end
            return 0  

def main():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.add_item("Notebook", 3, 5.00)
    order.remove_item("Pen")
    order.print_summary()
    discount = order.apply_discount("SAVE30")
    print("Discount rate:", discount)

main()