import json
import os

def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return []

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def add_book(book):
    books = load_data('books.txt')
    books.append(book.to_dict())
    save_data('books.txt', books)

def add_user(user):
    users = load_data('users.txt')
    users.append(user.to_dict())
    save_data('users.txt', users)

def add_transaction(transaction):
    transactions = load_data('transactions.txt')
    transactions.append(transaction.to_dict())
    save_data('transactions.txt', transactions)
