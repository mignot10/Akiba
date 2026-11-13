def add_product(products):
    product_id = input("Enter product ID: ")

    if product_id in products:
        print("Product already exists.")
        return

    name = input("Enter product name: ")

    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return

    products[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    print("Product added successfully.")


def view_products(products):
    if len(products) == 0:
        print("No products available.")
        return

    for product_id in products:
        print("\nProduct ID:", product_id)
        print("Name:", products[product_id]["name"])
        print("Price:", products[product_id]["price"])
        print("Quantity:", products[product_id]["quantity"])


def search_product(products, product_id):
    if product_id in products:
        return products[product_id]
    else:
        return None


def update_product(products):
    product_id = input("Enter product ID: ")

    if product_id not in products:
        print("Product not found.")
        return

    print("1. Update Name")
    print("2. Update Price")
    print("3. Update Quantity")

    choice = input("Choose an option: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        products[product_id]["name"] = new_name

    elif choice == "2":
        new_price = float(input("Enter new price: "))

        if new_price < 0:
            print("Price cannot be negative.")
            return

        products[product_id]["price"] = new_price

    elif choice == "3":
        new_quantity = int(input("Enter new quantity: "))

        if new_quantity < 0:
            print("Quantity cannot be negative.")
            return

        products[product_id]["quantity"] = new_quantity

    else:
        print("Invalid choice.")
        return

    print("Product updated successfully.")