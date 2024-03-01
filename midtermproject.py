import json
import os

def read_orders(file_path):
    # Read orders from a JSON file "example_order.json".
   
    with open(file_path, 'r') as orders_file:
        return json.load(orders_file)

def update_customers(orders):
    # Updates customer information based on orders.
    
    return {order['phone']: order['name'] for order in orders}

def update_items(orders):
    # Updates item information based on orders.
    
    items = {}
    for order in orders:
        for item in order['items']:
            item_name = item['name']
            price = item['price']
            items.setdefault(item_name, {'price': price, 'orders': 0})['orders'] += 1
    return items

def write_json(data, file_name):
    # Writes data to a JSON file.
    
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    orders_file_path = 'example_orders.json'

    if os.path.exists(orders_file_path):
        orders = read_orders(orders_file_path)

        customers = update_customers(orders)
        write_json(customers, 'customers.json')

        items = update_items(orders)
        write_json(items, 'items.json')
    else:
        print(f"Error: File '{orders_file_path}' not found.")

if __name__ == '__main__':
    main()
