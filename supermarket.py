from datetime import datetime

name = input("Enter your name: ")

items = {
    "rice": 420.0,
    "wheat flour": 250.0,
    "sugar": 50.0,
    "salt": 20.0,
    "cooking oil": 160.0,
    "tea powder": 180.0,
    "coffee powder": 130.0,
    "milk": 60.0,
    "bread": 45.0,
    "eggs": 90.0,
    "butter": 250.0,
    "cheese": 180.0,
    "apple": 120.0,
    "banana": 40.0,
    "orange": 100.0,
    "onion": 35.0,
    "tomato": 30.0,
    "potato": 25.0,
    "green peas": 60.0,
    "detergent": 150.0,
    "dishwash liquid": 90.0,
    "toothpaste": 80.0,
    "shampoo": 120.0,
    "soap": 140.0,
    "chips": 30.0,
    "biscuits": 25.0,
    "cold drink": 70.0,
    "water bottle": 20.0,
    "noodles": 45.0,
    "spices": 100.0
}

print("\nAvailable Items:")
for item, price in items.items():
    print(f"{item.title()} : ₹{price}")

cart = []
total = 0

while True:
    item = input("\nEnter item name (or type 'exit'): ").lower()

    if item == "exit":
        break

    if item not in items:
        print("❌ Item not available")
        continue

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("❌ Quantity must be a number")
        continue

    cost = qty * items[item]
    total += cost
    cart.append((item.title(), qty, cost))

    print(f"✅ {item.title()} added — ₹{cost}")

    more = input("Add more items? (yes/no): ").lower()
    if more != "yes":
        break

gst = total * 0.05
final = total + gst

print("\n" + "="*25, "BILL", "="*25)
print("Customer:", name)
print("Date:", datetime.now())
print("-"*60)
print("Item\t\tQty\tPrice")

for item, qty, price in cart:
    print(f"{item}\t{qty}\t₹{price}")

print("-"*60)
print("Total:\t\t₹", total)
print("GST (5%):\t₹", gst)
print("Final Amount:\t₹", final)
print("="*60)
print("Thank you. Visit Again!")
