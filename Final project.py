import os
import time
import random

books = {
    "Harry Potter and the Philosopher's Stone": {
        "price": 10,
        "author": "J.K. Rowling"
    },
    "The Hobbit": {
        "price": 8,
        "author": "J.R.R. Tolkien"
    },
    "The Catcher in the Rye": {
        "price": 6,
        "author": "J.D. Salinger"
    },
    "To Kill a Mockingbird": {
        "price": 7,
        "author": "Harper Lee"
    }
}

cart = []


## Functions

def print_store():
    print("Welcome to the store! Here are our items:")
    for book in books:
        print(f"{book}: ${books[book]['price']}")

def add_to_cart(item):
    cart.append({
        "item": item,
        "price": books[item]["price"]
    })
    print(f"{item} has been added to your cart!")

def view_cart():
    if len(cart) == 0:
        print("Your cart is empty!")
    else:
        total = 0
        print("Your cart contains:")
        for item in cart:
            print(f"{item['item']}: ${item['price']}")
            total += item['price']
        print(f"Total: ${total}")

def purchase():
    if len(cart) == 0:
        print("Your cart is empty!")
    else:
        total = 0
        print("Thank you for your purchase!")
        print("You bought:")
        for item in cart:
            print(f"{item['item']}: ${item['price']}")
            total += item['price']
        print(f"Total: ${total}")
        cart.clear()
        print("Your cart is now empty now.")

## Main Program

def main():
    print_store()

    while True:
        choice = input("What would you like to do? (Add/View/Purchase/Quit): ")
        if choice.lower() == "add":
            item = input("Please enter the name of the item you would like to add: ")
            if item in books:
                add_to_cart(item)
            else:
                print("That item is not in the store!")
        elif choice.lower() == "view":
            view_cart()
        elif choice.lower() == "purchase":
            purchase()
            break
        elif choice.lower() == "quit":
            print("Thank you for visiting the store!")
            break
        else:
            print("That is not a valid option!")

if __name__ == "__main__":
 main()

