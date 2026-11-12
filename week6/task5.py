class Product:
    # Class attribute
    store_name = "Tech Store"

    def __init__(self, name, price):
        # Instance attributes
        self.name = name
        self.price = price

    # Instance method
    def display_product(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Store: {self.store_name}")

    # Class method
    @classmethod
    def change_store_name(cls, new_name):
        cls.store_name = new_name

    # Static method
    @staticmethod
    def is_valid_price(price):
        return price > 0


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            if Product.is_valid_price(product.price):
                self.products.append(product)
            else:
                print("Invalid product price!")
        else:
            print("Only Product objects can be added.")

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.price

        return total

    def display_cart(self):
        print("\n===== Shopping Cart =====")

        for product in self.products:
            product.display_product()
            print("----------------")

        print(f"Total: ${self.calculate_total()}")


# Create products
product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 25)
product3 = Product("Keyboard", 50)

# Change the store name
Product.change_store_name("Mignot's Store")

# Create shopping cart
cart = ShoppingCart()

# Add products
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

# Display cart
cart.display_cart()
