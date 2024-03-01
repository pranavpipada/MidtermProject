# MidtermProject

This is a Python script designed to read and process orders from a JSON file "example_orders.json", updating customer and item information, and then saving the results in separate JSON files "customers.json" and "items.json". This simple system is useful for businesses or individuals managing orders and wanting to maintain a record of customer details and popular items.


## Features

1. Read Orders: The system reads order information from a JSON file, allowing flexibility in handling different datasets.

2. Update Customers: It extracts customer details from the orders and creates a dictionary mapping phone numbers to customer names.

3. Update Items: The script processes each order to update item information, including the item name, price, and the number of times the item has been ordered.

4. Write to JSON: The system writes the updated customer and item information to separate JSON files, providing easily accessible records.


## How to Use

1. Prepare Orders File: Create a JSON file "example_orders.json" containing the order information. Ensure that the structure follows the expected format, including customer details, items, and prices.

2. Run the Script: Execute the script in a Python environment, providing the path to the orders file as a command-line argument. For example:
    python order_management.py example_orders.json

3. Review Output: Check the generated `customers.json` and `items.json` files for updated customer and item information.

4. Error Handling: If the specified orders file is not found, an error message will be displayed.

5. Customization: You can modify the script to suit specific needs, such as changing the output file names or extending the functionality based on business requirements.


## Use

When an input file `example_orders.json` with orders. Running the script with this file will generate `customers.json` and `items.json` files, providing valuable insights into customer data and popular items.
