#!/usr/bin/env python3

class Coffee:
     def __init__(self, size, price):
        # Initialize coffee with size and price
        self.size = size
        self.price = price

    # Property getter for size
     @property
     def size(self):
        return self._size

    # Property setter for size
     @size.setter
     def size(self, value):
        # Ensure size is valid
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Method to tip for coffee
     def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1