def calculate_subtotal(items):
    if not items:
        return 0
    for item in items:
        if 'price' not in item or 'quantity' not in item or item['price'] < 0 or item['quantity'] < 0:
            print("Each item must have a non-negative 'price' and 'quantity'.")
            return 0
        
    return sum(item['price'] * item['quantity'] for item in items)

def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.1
    elif 1000 <= subtotal < 3000:
        return subtotal * 0.05
    return 0

def calculate_tax(amount, tax_rate):
    if tax_rate < 0:
        print("Tax rate cannot be negative.")
        return 0
    return amount * tax_rate


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    discounted_total = subtotal - discount
    tax = calculate_tax(discounted_total, tax_rate)
    total = discounted_total + tax
    return {
        "subtotal": subtotal,
        "discount": discount,
        "discounted_total": discounted_total,
        "tax": tax,
        "total": total
    }

def run_shopping_cart():
    items=[{"price": 100, "quantity": 2}, {"price": 50, "quantity": 5}]
    tax_rate = float(input("Enter tax rate (as a decimal, e.g., 0.07 for 7%): "))
    receipt = generate_receipt(items, tax_rate)
    for key, value in receipt.items():
        print(f"{key.capitalize()}: ${value:.2f} Birr")


if __name__ == "__main__":
    run_shopping_cart()