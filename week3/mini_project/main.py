from products import (
    add_product,
    view_products,
    search_product,
    update_product
)

from sales import record_sale, generate_receipt

from reports import view_reports


def main():
    products = {}
    sales = []

    while True:
        print("\n===== AKIBA BUSINESS TOOLKIT =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Record Sale")
        print("6. View Reports")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product(products)

        elif choice == "2":
            view_products(products)

        elif choice == "3":
            product_id = input("Enter product ID: ")

            product = search_product(products, product_id)

            if product is not None:
                print("Name:", product["name"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])
            else:
                print("Product not found.")

        elif choice == "4":
            update_product(products)

        elif choice == "5":
            sale = record_sale(products, sales)
            generate_receipt(sale)

        elif choice == "6":
            view_reports(products, sales)

        elif choice == "7":
            print("Thank you for using Akiba Business Toolkit!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()