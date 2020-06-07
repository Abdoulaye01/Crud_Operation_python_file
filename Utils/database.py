"""
Create a Crud Operation & saving it to a file
Using OOP with two classes continuation from the list project

"""
import os  # For mac

book_file = 'data.txt'
print("######################################".strip())
print(__doc__.strip())
print("######################################")


def add_book(name, author):
    with open(book_file, 'a') as file:
        file.write(f'{name}, {author}, 0 \n')


def check_if_file_exits():
    if not os.path.exists(book_file):
        print(" File does not exist >>> Create one !")
        exit()
    # with open(book_file, 'a') as file:
    #     print('File does not exit, Create one !')


def get_all_books():
    with open(book_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        return [
            {'name': line[0], 'author': line[1], 'read': line[2]} for line in lines]
    # else:
    #     print("File does not exist")


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
            print('Book marks as read! ')
            break
    else:
        print('Not found > TRY AGAIN')
    _save_back_the_file(books)


def _save_back_the_file(books):
    with open(book_file, 'w') as file:
        for book in books:
            file.write(f"{book['name'], book['author'], book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book[
        'name'] != name]  # Here we are saying if book name is not equal to the name we are looking for then return the list of books otherwise delete the book respectively
    _save_back_the_file(books)
