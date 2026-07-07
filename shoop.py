class Customer:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.cart = None     

    def __str__(self):
        return f"your balance is : {self.balance}"

    def buy(self, products, cart):
        total = cart.total_fee(products)

        if total > self.balance:
            print("not enough money!")
            return

        for name, count in cart.cart:
            products[name].count -= count

        self.balance -= total
        cart.cart.clear()
        


class Cart:
    def __init__(self):
        self.cart = []

    def __str__(self):
        return f"your list is : {self.cart}"

    def total_fee(self, products):
        total = 0
        for name, count in self.cart:
            total += products[name].fee * count
        print(f"total fee is : {total}")
        return total

    def add(self, products):
        name = input("enter name of product :")
        if name not in products:
            print("invalid product...")
            return

        count = int(input("how many ?"))
        if count > products[name].count:
            print("not enough product")
            return

        self.cart.append((name,count))
        print("product added !")


class Product:
    def __init__(self,name,fee,count):
        self.name = name
        self.fee = fee
        self.count = count

    def __str__(self):
        return f"{self.name} , fee: {self.fee} , count: {self.count}"


if __name__=='__main__':
    products = {
        "chips": Product("chips",30000,10),
        "icecream": Product("icecream",25000,30),
        "coffee": Product("coffee",35000,40)
    }

    customer = Customer("mohammad",2000000)
    cart = Cart()

    while True:
        print("1) buy\n2) add to cart\n3) show total fee\n4) show products\n5) exit")
        order = int(input("enter your option : "))

        if order == 1:
            customer.buy(products, cart)

        elif order == 2:
            cart.add(products)

        elif order == 3:
            cart.total_fee(products)

        elif order == 4:
            for p in products.values():
                print(p)

        elif order == 5:
            break

        else:
            print("invalid option")

    

    
    
    
    
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def manage_store(self):
        pass
class Customer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.cart = []

    def buy(self, product):
        self.cart.append(product)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class OnlineStore:
    def __init__(self):
        self.products = []
        self.employees = []
    def add_product(self, product):
        self.products.append(product)
    def add_employee(self, employee):
        self.employees.append(employee)
