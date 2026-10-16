
# ==========================================
# Task 6: Interactive Inventory Stock Controller
# ==========================================

def add_product(inventory, name, price, stock):
    """Add a new product to the inventory."""
    if not name or not name.strip():
        print("Product name cannot be empty.")
        return False

    name = name.strip()

    if name in inventory:
        print(f"Product '{name}' already exists in the inventory.")
        return False

    if price < 0:
        print("Price cannot be negative.")
        return False

    if stock < 0:
        print("Stock cannot be negative.")
        return False

    inventory[name] = {
        'price': float(price),
        'stock': int(stock)
    }

    print(f"Product '{name}' added successfully.")
    return True


def search_product(inventory, name):
    """Search for a product and return its details."""
    if not name or not name.strip():
        print("Search query cannot be empty.")
        return None

    name = name.strip()

    if name in inventory:
        return {'name': name, **inventory[name]}

    print(f"Product '{name}' not found.")
    return None


def update_price(inventory, name, new_price):
    """Update the price of an existing product."""
    name = name.strip() if name else ""

    if name not in inventory:
        print(f"Product '{name}' not found.")
        return False

    if new_price < 0:
        print("Price cannot be negative.")
        return False

    inventory[name]['price'] = float(new_price)

    print(f"Price for '{name}' updated to ${new_price:.2f}.")
    return True


def increase_stock(inventory, name, quantity):
    """Increase the stock of an existing product."""
    name = name.strip() if name else ""

    if name not in inventory:
        print(f"Product '{name}' not found.")
        return False

    if quantity < 0:
        print("Stock increase quantity cannot be negative.")
        return False

    inventory[name]['stock'] += int(quantity)

    print(
        f"Added {quantity} units to '{name}'. "
        f"New stock: {inventory[name]['stock']}."
    )
    return True


def sell_product(inventory, name, quantity):
    """Sell a product if enough stock is available."""
    name = name.strip() if name else ""

    if name not in inventory:
        print(f"Product '{name}' not found.")
        return False

    if quantity < 0:
        print("Sale quantity cannot be negative.")
        return False

    if quantity > inventory[name]['stock']:
        print(
            f"Sale exceeds available stock for '{name}'. "
            f"Available: {inventory[name]['stock']}."
        )
        return False

    inventory[name]['stock'] -= int(quantity)

    print(
        f"Sold {quantity} units of '{name}'. "
        f"Remaining stock: {inventory[name]['stock']}."
    )
    return True


def calculate_total_inventory_value(inventory):
    """Calculate the total value of all items in stock."""
    return sum(
        item['price'] * item['stock']
        for item in inventory.values()
    )


def generate_low_stock_report(inventory, threshold=5):
    """Return products whose stock is below the threshold."""
    return {
        name: details
        for name, details in inventory.items()
        if details['stock'] < threshold
    }


# ==========================================
# Interactive Console Menu
# ==========================================

def run_inventory_system():
    inventory = {}

    while True:
        print("\n" + "=" * 40)
        print("      INVENTORY STOCK CONTROLLER")
        print("=" * 40)
        print("1. Add a new product")
        print("2. Search for a product")
        print("3. Update product price")
        print("4. Increase stock")
        print("5. Sell a product")
        print("6. Calculate total inventory value")
        print("7. Generate low-stock report")
        print("8. View all inventory")
        print("9. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter price ($): "))
            stock = int(input("Enter initial stock quantity: "))
            add_product(inventory, name, price, stock)

        elif choice == '2':
            name = input("Enter product name to search: ")
            result = search_product(inventory, name)

            if result:
                print("\nProduct Details:")
                print(f"   Name  : {result['name']}")
                print(f"   Price : ${result['price']:.2f}")
                print(f"   Stock : {result['stock']} units")

        elif choice == '3':
            name = input("Enter product name to update price: ")
            new_price = float(input("Enter new price ($): "))
            update_price(inventory, name, new_price)

        elif choice == '4':
            name = input("Enter product name to restock: ")
            quantity = int(input("Enter quantity to add: "))
            increase_stock(inventory, name, quantity)

        elif choice == '5':
            name = input("Enter product name to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            sell_product(inventory, name, quantity)

        elif choice == '6':
            total = calculate_total_inventory_value(inventory)
            print(f"\nTotal Inventory Value: ${total:.2f}")

        elif choice == '7':
            threshold_input = input(
                "Enter low-stock threshold (press Enter for default 5): "
            ).strip()

            if threshold_input == "":
                threshold = 5
            else:
                threshold = int(threshold_input)

            report = generate_low_stock_report(inventory, threshold)

            print(f"\nLow-Stock Report (Threshold: < {threshold}):")

            if not report:
                print("All stock levels are healthy.")
            else:
                for name, details in report.items():
                    print(
                        f"   {name}: Price = ${details['price']:.2f}, "
                        f"Stock = {details['stock']} units"
                    )

        elif choice == '8':
            if not inventory:
                print("\nInventory is currently empty.")
            else:
                print("\nCurrent Inventory List:")

                for name, details in inventory.items():
                    print(
                        f"   {name} — Price: ${details['price']:.2f} "
                        f"| Stock: {details['stock']} units"
                    )

        elif choice == '9':
            print("\nExiting Inventory System. Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    run_inventory_system()
