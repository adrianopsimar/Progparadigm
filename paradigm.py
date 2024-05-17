def vending_machine():
    # Define products and their prices
    products = {
        "1": {"name": "Chips", "price": 1.50},
        "2": {"name": "Soda", "price": 1.00},
        "3": {"name": "Candy", "price": 0.75},
        "4": {"name": "Chocolate", "price": 1.25},
        "5": {"name": "Juice", "price": 1.75}
    }
    
    # Function to display products
    def display_products():
        print("\nAvailable products:")
        for key, product in products.items():
            print(f"{key}. {product['name']} - ${product['price']:.2f}")

    # User enters money
    try:
        money = float(input("Enter the amount of money you have: $"))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    while True:
        display_products()
        
        # User selects a product
        choice = input("\nEnter the number of the product you want to buy (or 'q' to quit): ").strip()
        
        if choice.lower() == 'q':
            print("Transaction cancelled. Returning your money: ${:.2f}".format(money))
            break
        
        if choice not in products:
            print("Invalid selection. Please try again.")
            continue
        
        selected_product = products[choice]
        
        if money >= selected_product["price"]:
            money -= selected_product["price"]
            print(f"Dispensing {selected_product['name']}. Enjoy!")
            if money > 0:
                print(f"Your remaining balance is: ${money:.2f}")
            else:
                print("You have no remaining balance.")
        else:
            print(f"Insufficient funds for {selected_product['name']}. You need ${selected_product['price'] - money:.2f} more.")
        
        if input("\nDo you want to buy another product? (yes/no): ").strip().lower() != 'yes':
            print("Thank you for using the vending machine.")
            if money > 0:
                print(f"Returning your remaining money: ${money:.2f}")
            break

if __name__ == "__main__":
    vending_machine()
