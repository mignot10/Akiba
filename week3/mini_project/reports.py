def calculate_revenue(sales):
    total = 0

    for sale in sales:
        total = total + sale["total"]

    return total


def calculate_inventory_value(products):
    total = 0

    for product_id in products:
        price = products[product_id]["price"]
        quantity = products[product_id]["quantity"]

        total = total + (price * quantity)

    return total


def display_low_stock(products):
    found = False

    print("\n========== LOW STOCK PRODUCTS ==========")

    for product_id in products:
        if products[product_id]["quantity"] <= 5:
            print("Product:", products[product_id]["name"])
            print("Quantity:", products[product_id]["quantity"])
            found = True

    if found == False:
        print("No low-stock products.")


def display_sales(sales):
    if len(sales) == 0:
        print("No sales recorded.")
        return

    print("\n========== SALES HISTORY ==========")

    for sale in sales:
        print("Product:", sale["product_name"])
        print("Quantity:", sale["quantity"])
        print("Total:", sale["total"])
        print("------------------------")


def view_reports(products, sales):
    print("\n========== BUSINESS REPORT ==========")

    revenue = calculate_revenue(sales)
    inventory = calculate_inventory_value(products)

    print("Total Revenue:", revenue)
    print("Inventory Value:", inventory)
    print("Total Products:", len(products))
    print("Total Sales:", len(sales))

    display_low_stock(products)
    display_sales(sales)