# Matthew Landale
# Lab 8
# 15 November 2019

# JA: Always remember to add comments to your code

class Product(object):
    def __init__(self, product, quantity, price):
        """Represents the item"""
        self.myProduct = product
        self.myQuantity = quantity
        self.myPrice = price


    def __str__(self):
        ans = "Product: " + self.myProduct + "\n"
        ans += "Quantity: " + str(self.myQuantity) + "\n"
        ans += "Price: ${0:0.2f}".format(self.myPrice)
        return ans


    def getProduct(self):
        """gets the name of the product"""
        ans = self.myProduct
        return ans


    def getQuantity(self):
        """gets the quantity of the product"""
        ans = self.myQuantity
        return ans


    def getPrice(self):
        """gets the price of the product"""
        ans = self.myPrice
        return ans


    def setPrice(self, newPrice):
        """sets the price of the product"""
        self.myPrice = newPrice


    def setQuantity(self, newQuantity):
        """sets the quantity of the product"""
        self.myQuantity = newQuantity


    def setProduct(self, newProduct):
        """sets the name of the product"""
        self.myProduct = newProduct


    def inStock(self, product, quantity):
        """checks if an amount of products are in stock"""

ultrasonicRangeFinder = Product("Ultrasonic range finder", 4, 2.50)
servoMotor = Product("Servo motor", 10, 14.99)
servoController = Product("Servo controller", 5, 44.95)
microcontrollerBoard = Product("Microcontroller board", 7, 34.95)
laserRangeFinder = Product("Laser range finder", 2, 149.99)
lithiumPolymerBattery = Product("Lithium polymer", 8, 8.99)

productList = [ultrasonicRangeFinder, servoMotor, servoController, microcontrollerBoard, laserRangeFinder, lithiumPolymerBattery]


def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0, len(productList)):
        print(str(i)+")", productList[i])
    print()


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and the quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodId = int(vals[0])
        count = int(vals[1])

        if productList[prodId].getQuantity() >= count:
            if cash >= productList[prodId].getPrice():
                productList[prodId].setQuantity(productList[prodId].getQuantity()-count)
                cash -= productList[prodId].getPrice() * count
                print("You purchased", count, productList[prodId].getProduct()+".")
                print("You have ${0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", productList[prodId].getProduct())


main()
