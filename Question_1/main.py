from Entities import Book,User
from File_Handling import add_book,add_user
from Functionalities import list_books,list_users,borrow_book,return_book

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Register User")
        print("3. List Books")
        print("4. List Users")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            copies = int(input("Enter Number of Copies: "))
            add_book(Book(book_id, title, author, copies))
        elif choice == '2':
            user_id = int(input("Enter User ID: "))
            name = input("Enter User Name: ")
            add_user(User(user_id, name))
        elif choice == '3':
            list_books()
        elif choice == '4':
            list_users()
        elif choice == '5':
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))
            borrow_book(user_id, book_id)
        elif choice == '6':
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))
            return_book(user_id, book_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
