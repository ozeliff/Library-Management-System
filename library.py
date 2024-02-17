class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()
    
    def list_books(self):
        try:
            with open("books.txt", "r") as file:
                books = file.readlines()
                for book in books:
                    book_info = book.split(',')
                    print(f"Book Name: {book_info[0]} - Author: {book_info[1]}")  
        except FileNotFoundError:
            print("books.txt not found!")


    def add_book(self):
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            year = input("Enter First Release Year: ")
            page_count = input("Enter Number of Pages: ")
            
            book_info = f"{title}, {author}, {year}, {page_count}\n"
            with open('books.txt', 'a+') as file:
                file.write(book_info)
            
            print("Book was added successfully.\n")
        

    def remove_book(self):
        title = input("Enter Book Title: ")
        try:
            with open("books.txt", "r") as file:
                books = file.readlines()

                for index, book in enumerate(books):
                    book_info = book.split(',')
                    if title == book_info[0]:
                        books.pop(index)
                        print("Book was deleted successfully.\n")

            with open("books.txt", "w") as file:
                file.writelines(books)

        except FileNotFoundError:
            print("books.txt not found!")


lib = Library()


while(True):
    print("*** MENU***\n1-List Book\n2-Add Book\n3-Remove Book\n4-Quit")
    selection = input("Enter Number: ")
    try:  
        selection = int(selection)
        if selection == 1:
            lib.list_books()
        elif selection == 2:
            lib.add_book()
        elif selection == 3:
            lib.remove_book()
        elif selection == 4:
            break
        else:
            print("Please enter a valid number\n")
    except ValueError:
        print("Please enter a valid number\n")
