#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = {'quantity': 0, 'price': 0} 

    def add_item(self, title, price, quantity=1):
        """Adds an item to the cash register with optional quantity"""
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = {'quantity': quantity, 'price': price}

    def apply_discount(self):
        """Applies discount if available, returns discounted total"""
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            self.total = round(self.total, 2)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """Removes the last transaction from the total and items list"""
        if not self.items:
            self.total = 0.0
            return
        
        amount_to_void = self.last_transaction['price'] * self.last_transaction['quantity']
        self.total -= amount_to_void
        
        for _ in range(self.last_transaction['quantity']):
            if self.items: 
                self.items.pop()
        
        if self.total < 0:
            self.total = 0.0
        

