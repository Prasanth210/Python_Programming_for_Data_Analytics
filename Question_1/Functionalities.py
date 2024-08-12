from Entities import Book,User,Transaction
from File_Handling import add_book,add_user,add_transaction,load_data,save_data

def list_books():
    books = load_data('books.txt')
    for book in books:
        print(f"ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")

def list_users():
    users = load_data('users.txt')
    for user in users:
        print(f"ID: {user['user_id']}, Name: {user['name']}")

def borrow_book(user_id, book_id):
    books = load_data('books.txt')
    for book in books:
        if book['book_id'] == book_id and book['copies'] > 0:
            book['copies'] -= 1
            save_data('books.txt', books)
            transaction = Transaction(len(load_data('transactions.txt')) + 1, user_id, book_id, "borrow")
            add_transaction(transaction)
            print(f"Book borrowed successfully by User ID: {user_id}")
            return
    print("Book is not available or doesn't exist.")

def return_book(user_id, book_id):
    books = load_data('books.txt')
    for book in books:
        if book['book_id'] == book_id:
            book['copies'] += 1
            save_data('books.txt', books)
            transaction = Transaction(len(load_data('transactions.txt')) + 1, user_id, book_id, "return")
            add_transaction(transaction)
            print(f"Book returned successfully by User ID: {user_id}")
            return
    print("Book ID not found.")

# Example usage:
book1 = Book(1, "Python Programming", "John Doe", 3)
user1 = User(1, "Prasanth")

add_book(book1)
add_user(user1)

list_books()
list_users()

borrow_book(1, 1)
list_books()

return_book(1, 1)
list_books()
