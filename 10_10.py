class Furniture():
    maker = "Ikea"
    is_sold = False

    def __init__(self, price):
        self.price = price

f = Furniture()
print(f.maker)