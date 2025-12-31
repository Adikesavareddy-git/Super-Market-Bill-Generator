Supermarket Billing Generator

A console-based supermarket billing generator developed using Python.
This application simulates a basic retail checkout process by allowing users to select grocery items, enter quantities, calculate totals, apply GST, and generate a formatted billing receipt.
The project is intentionally focused on clean control flow, input validation, and core Python programming concepts, rather than graphical interfaces.

 Features
🔹 Predefined Inventory
Includes 30 grocery items with fixed prices
Prices stored in a dictionary for fast and reliable lookup
🔹 Dynamic Item Entry
Users can add multiple items in a single billing session
Full control over when the billing process ends
🔹 Quantity-Based Pricing
Automatically calculates item cost based on entered quantity
🔹 GST Calculation
Applies a flat 5% GST on the subtotal
🔹 Formatted Console Receipt
Displays:
Customer name
Date and time
Itemized bill
GST amount
Final payable amount
🔹 Input Validation
Handles:
Invalid item names
Non-numeric quantity inputs
Controlled exit from the shopping loop
🛠️ Technical Details
Language: Python 3.x
Core Concepts Used:
Dictionaries for constant-time price lookup
Lists of tuples for cart storage
while loops for session control
try-except blocks for runtime input validation
Standard Library:
datetime for bill timestamping
Execution Environment:
Terminal / Command Line
No external libraries. No unnecessary dependencies.

How to Run
Clone the repository
git clone https://github.com/Adikesavareddy-git/grocery-billing-system.git

Navigate to the project directory
cd grocery-billing-system

Run the program
python grocery_billing.py
Application Flow
Enter customer name
View available grocery items
Add item → enter quantity
Choose whether to add more items
Generate final bill with GST
Straightforward and predictable — exactly how a billing system should work.

 Limitations (Honest)
Console-based only (no GUI or web interface)
Fixed pricing (no inventory updates)
Single GST rate
No data persistence (bill is not saved to a file)
These are design choices, not implementation errors.
 
 Possible Enhancements

Menu-driven item selection (numeric input)
Save receipts as text or PDF files
Inventory stock management
Item-wise tax configuration
GUI or web-based interface
Add these only to improve learning, not to artificially inflate the project.

 Author
Adikesavareddy Katterapalli
GitHub: https://github.com/Adikesavareddy-git
LinkedIn: https://www.linkedin.com/in/adikesavareddy-katterapalli
