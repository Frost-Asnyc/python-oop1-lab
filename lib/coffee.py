class Coffee:
    """Represents a coffee sold by the bookstore's cafe counter."""

    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        # size must be one of Small, Medium, or Large
        if size in self.VALID_SIZES:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Tipping the barista increases the price by 1
        print("This coffee is great, here’s a tip!")
        self.price += 1
