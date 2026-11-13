from products import search_product


def record_sale(products, sales):
    product_id = input("Enter product ID: ")

    product = search_product(products, product_id)

    if product is None:
        print("Product not found.")
        return None

    print("Product:", product["name"])
    print("Available quantity:", product["quantity"])

    quantity = int(input("Enter quantity to buy: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return None

    if quantity > product["quantity"]:
        print("Not enough stock.")
        return None

    total = quantity * product["price"]

    product["quantity"] = product["quantity"] - quantity

    sale = {
        "product_name": product["name"],
        "quantity": quantity,
        "price": product["price"],
        "total": total
    }

    sales.append(sale)

    print("Sale recorded successfully.")

    return sale


def generate_receipt(sale):
    if sale is None:
        return

    print("\n========== RECEIPT ==========")
    print("Product:", sale["product_name"])
    print("Quantity:", sale["quantity"])
    print("Unit Price:", sale["price"])
    print("Total:", sale["total"])
    print("=============================")