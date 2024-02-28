import json
import os

def read_orders(file_path):
    # Reads orders from example_orders.json file and returns List of orders.
    with open(file_path, 'r') as orders_file:
        return json.load(orders_file)


def main():
    orders_file_path = 'example_orders.json'

    if os.path.exists(orders_file_path):
        orders = read_orders(orders_file_path)

    else:
        print(f"Error: File '{orders_file_path}' not found.")
