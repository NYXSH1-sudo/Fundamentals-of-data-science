"""
Q8: library_system.py - OOP Library Management: borrow/return/search books.
Uses files, exception handling, encapsulation.
Author: Seshank Kumar Sharma,SEC-B.
Date: 2026-04-17
"""
import csv
import os

FILENAME   = "library.csv"
FIELDNAMES = ["book_id", "title", "author", "genre", "available"]


# ─── Book Class ──────

class Book:
    '''Represents a book in the library.'''

    def __init__(self, book_id, title, author, genre, available=True):
        self.__book_id   = book_id
        self.__title     = title
        self.__author    = author
        self.__genre     = genre
        self.__available = available if isinstance(available, bool) else (available == "True")

    # ── Getters (encapsulation) ──
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        self.__available = value

    def to_dict(self):
        return {
            "book_id":   self.__book_id,
            "title":     self.__title,
            "author":    self.__author,
            "genre":     self.__genre,
            "available": str(self.__available),
        }

    def display(self, show_status=True):
        status = "Available" if self.__available else "Borrowed"
        line = (f"  [{self.__book_id}] '{self.__title}' by {self.__author}"
                f"  |  Genre: {self.__genre}")
        if show_status:
            line += f"  |  Status: {status}"
        print(line)


# ─── Library Class ────────

class Library:
    '''Manages the collection of books, with file-backed persistence.'''

    def __init__(self):
        self.__books = {}   # dict: book_id -> Book
        self.__load_books()

    # ── Private: file helpers ──

    def __ensure_file(self):
        if not os.path.exists(FILENAME):
            try:
                with open(FILENAME, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                    writer.writeheader()
                # Seed with sample books
                samples = [
                    Book("B001", "Pocket Psychiatry",      "Kamaldeep Bhui",  "Psychology"),
                    Book("B002", "Clean Code",         "Robert Martin", "Technology"),
                    Book("B003", "Atomic Habits",      "James Clear",   "Self-Help"),
                    Book("B004", "A Wrinkle In Time",            "Madeleine L'Engle",  "Fiction"),
                    Book("B005", "Python Crash Course","Eric Matthes",  "Technology"),
                ]
                for book in samples:
                    self.__books[book.book_id] = book
                self.__save_all()
                print(f"  '{FILENAME}' created and seeded with {len(samples)} sample books.\n")
            except IOError as e:
                print(f"  Error creating file: {e}")

    def __load_books(self):
        '''Load all books from CSV into memory.'''
        self.__ensure_file()
        try:
            with open(FILENAME, "r", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    book = Book(row["book_id"], row["title"], row["author"],
                                row["genre"], row["available"])
                    self.__books[book.book_id] = book
        except FileNotFoundError:
            print(f"  '{FILENAME}' not found. Starting fresh.")
        except KeyError as e:
            print(f"  CSV format error – missing column: {e}")
        except IOError as e:
            print(f"  Error loading books: {e}")

    def __save_all(self):
        '''Write the full in-memory book dict back to CSV.'''
        try:
            with open(FILENAME, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writeheader()
                for book in self.__books.values():
                    writer.writerow(book.to_dict())
        except IOError as e:
            print(f"  Error saving data: {e}")

    # ── Public methods ──

    def add_book(self, book):
        '''Add a new book to the library.'''
        if book.book_id in self.__books:
            print(f"  ✘ Book ID '{book.book_id}' already exists.")
            return
        self.__books[book.book_id] = book
        self.__save_all()
        print(f"  ✔ '{book.title}' added to the library.")

    def search_book(self, keyword):
        '''Search by book_id, title, or author (case-insensitive).'''
        kw = keyword.lower()
        results = [b for b in self.__books.values()
                   if kw in b.book_id.lower()
                   or kw in b.title.lower()
                   or kw in b.author.lower()]
        if results:
            print(f"\n  Found {len(results)} result(s) for '{keyword}':")
            for book in results:
                book.display()
        else:
            print(f"\n  No book found matching '{keyword}'.")

    def borrow_book(self, book_id):
        '''Mark a book as borrowed.'''
        try:
            book = self.__books[book_id]
            if book.available:
                book.available = False
                self.__save_all()
                print(f"\n  ✔ You have borrowed '{book.title}'. Please return it on time!")
            else:
                print(f"\n  ✘ '{book.title}' is currently not available (already borrowed).")
        except KeyError:
            print(f"\n  ✘ No book found with ID '{book_id}'.")

    def return_book(self, book_id):
        '''Mark a book as returned/available.'''
        try:
            book = self.__books[book_id]
            if not book.available:
                book.available = True
                self.__save_all()
                print(f"\n  ✔ '{book.title}' returned successfully. Thank you!")
            else:
                print(f"\n  ✘ '{book.title}' was not marked as borrowed.")
        except KeyError:
            print(f"\n  ✘ No book found with ID '{book_id}'.")

    def view_all(self):
        '''Display all books.'''
        if not self.__books:
            print("\n  The library has no books.")
            return
        print(f"\n  === Library Catalogue ({len(self.__books)} book(s)) ===")
        for book in self.__books.values():
            book.display()

    def view_available(self):
        '''Display only available books.'''
        avail = [b for b in self.__books.values() if b.available]
        if not avail:
            print("\n  No books are currently available.")
        else:
            print(f"\n  === Available Books ({len(avail)}) ===")
            for book in avail:
                book.display(show_status=False)


# ─── Input Helper ───────

def get_input(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("  Input cannot be empty.")


# ─── Main ────────

def main():
    library = Library()

    while True:
        print("\n" + "=" * 50)
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)
        print("  1. View all books")
        print("  2. View available books")
        print("  3. Search for a book")
        print("  4. Borrow a book")
        print("  5. Return a book")
        print("  6. Add a new book")
        print("  7. Exit")
        print("=" * 50)

        choice = input("  Enter choice (1-7): ").strip()

        if choice == "1":
            library.view_all()

        elif choice == "2":
            library.view_available()

        elif choice == "3":
            keyword = get_input("  Enter title, author, or book ID: ")
            library.search_book(keyword)

        elif choice == "4":
            book_id = get_input("  Enter Book ID to borrow: ").upper()
            library.borrow_book(book_id)

        elif choice == "5":
            book_id = get_input("  Enter Book ID to return: ").upper()
            library.return_book(book_id)

        elif choice == "6":
            print("\n  --- Add New Book ---")
            book_id = get_input("  Book ID : ").upper()
            title   = get_input("  Title   : ")
            author  = get_input("  Author  : ")
            genre   = get_input("  Genre   : ")
            library.add_book(Book(book_id, title, author, genre))

        elif choice == "7":
            print("\n  Exiting Library System. Goodbye!")
            break

        else:
            print("  Invalid choice. Enter a number from 1 to 7.")


# Main
main()