class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ₹{self.price}, Stock: {self.stock_quantity}"

class User:
    def __init__(self, username, password, user_type='customer'):
        self.username = username
        self.password = password
        self.user_type = user_type
        self.cart = Cart(self)

    def __str__(self):
        return f"User: {self.username}, Type: {self.user_type}"

class Cart:
    def __init__(self, user):
        self.user = user
        self.items = {}

    def add_to_cart(self, product, quantity):
        if quantity <= product.stock_quantity:
            if product.product_id in self.items:
                self.items[product.product_id]['quantity'] += quantity
            else:
                self.items[product.product_id] = {'product': product, 'quantity': quantity}
            product.stock_quantity -= quantity
            print(f"Added {quantity} {product.name}(s) to the cart.")
        else:
            print(f"Not enough stock for {product.name}. Only {product.stock_quantity} left.")

    def remove_from_cart(self, product, quantity):
        if product.product_id in self.items and self.items[product.product_id]['quantity'] >= quantity:
            self.items[product.product_id]['quantity'] -= quantity
            product.stock_quantity += quantity
            print(f"Removed {quantity} {product.name}(s) from the cart.")
        else:
            print(f"Not enough quantity of {product.name} to remove.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for item in self.items.values():
                product = item['product']
                print(f"{product.name} - ₹{product.price} x {item['quantity']}")

    def total_price(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def checkout(self):
        if self.items:
            total = self.total_price()
            print(f"Total: ₹{total}")
            confirm = input("Do you want to confirm your order? (y/n): ").lower()
            if confirm == 'y':
                self.items.clear()
                print("Order placed successfully!")
            else:
                print("Order cancelled.")
        else:
            print("Your cart is empty!")

class ECommerceSystem:
    def __init__(self):
        self.products = {}
        self.users = {}
        self.current_user = None

    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Product '{product.name}' added successfully.")

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products.values():
            print(product)

    def search_product(self, keyword):
        print(f"\nSearch Results for '{keyword}':")
        for product in self.products.values():
            if keyword.lower() in product.name.lower():
                print(product)

    def register_user(self, username, password, user_type='customer'):
        if username in self.users:
            print("User already exists!")
        else:
            new_user = User(username, password, user_type)
            self.users[username] = new_user
            print(f"User {username} registered successfully!")

    def login_user(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.current_user = self.users[username]
            print(f"Welcome, {self.current_user.username}!")
        else:
            print("Invalid username or password!")

    def logout_user(self):
        if self.current_user:
            print(f"Goodbye, {self.current_user.username}!")
            self.current_user = None
        else:
            print("No user logged in!")

def menu():
    print("\n1. Register User")
    print("2. Login User")
    print("3. Logout User")
    print("4. Add Product (Admin)")
    print("5. View Products")
    print("6. Search Product")
    print("7. Add to Cart")
    print("8. Remove from Cart")
    print("9. View Cart")
    print("10. Checkout")
    print("11. Exit")

def main():
    system = ECommerceSystem()

    # Adding some products for demonstration
    system.add_product(Product(1, "Laptop", "Electronics", 50000, 10))
    system.add_product(Product(2, "Smartphone", "Electronics", 20000, 15))
    system.add_product(Product(3, "Shirt", "Clothing", 1000, 30))

    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.register_user(username, password)
        
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.login_user(username, password)

        elif choice == 3:
            system.logout_user()

        elif choice == 4:
            if system.current_user and system.current_user.user_type == 'admin':
                name = input("Enter product name: ")
                category = input("Enter product category: ")
                price = float(input("Enter product price: ₹"))
                stock_quantity = int(input("Enter stock quantity: "))
                product_id = len(system.products) + 1
                product = Product(product_id, name, category, price, stock_quantity)
                system.add_product(product)
            else:
                print("Only admin can add products.")

        elif choice == 5:
            system.display_products()

        elif choice == 6:
            keyword = input("Enter product name to search: ")
            system.search_product(keyword)

        elif choice == 7:
            if system.current_user:
                system.display_products()
                product_id = int(input("Enter product ID to add to cart: "))
                quantity = int(input("Enter quantity: "))
                if product_id in system.products:
                    system.current_user.cart.add_to_cart(system.products[product_id], quantity)
                else:
                    print("Product not found.")
            else:
                print("Please login first.")

        elif choice == 8:
            if system.current_user:
                system.current_user.cart.view_cart()
                product_id = int(input("Enter product ID to remove from cart: "))
                quantity = int(input("Enter quantity to remove: "))
                if product_id in system.products:
                    system.current_user.cart.remove_from_cart(system.products[product_id], quantity)
                else:
                    print("Product not found.")
            else:
                print("Please login first.")

        elif choice == 9:
            if system.current_user:
                system.current_user.cart.view_cart()
            else:
                print("Please login first.")

        elif choice == 10:
            if system.current_user:
                system.current_user.cart.checkout()
            else:
                print("Please login first.")

        elif choice == 11:
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
