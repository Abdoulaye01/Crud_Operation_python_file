"""
Create a Crud Operation using List & List comprehension
Using OOP with two classes

"""

books = []
print("######################################".strip())
print(__doc__.strip())
print("######################################")


def add_book(name, author):
    books.append({
        'name': name,
        'author': author,
        'read': False
    })


def get_all_books():
    return books


def mark_book_as_read(name):
    global books
    for book in books:
        if book['name'] == name:
            books['read'] = True
    else:
        print('Not found > TRY AGAIN')


def delete_book(name):
    global books
    books = [book for book in books if book[
        'name'] != name]  # Here we are saying if book name is not equal to the name we are looking for then return the list of books otherwise delete the book respectively
