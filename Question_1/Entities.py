import json
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "copies": self.copies
        }

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name
        }

class Transaction:
    def __init__(self, transaction_id, user_id, book_id, type):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.book_id = book_id
        self.type = type  # "borrow" or "return"

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "type": self.type
        }
