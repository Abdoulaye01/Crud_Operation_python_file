from Utils import database


USER_INPUT = """
Please input letter a - b - c - d and q to quit 
    a - add book to the list
    b - view all books
    c - mark book as read
    d - delete book
    q - quit application """

user_input = input(USER_INPUT)


def prompt_add_book():
    how_many = int(input('how many books are you entering to: '))
    for i in range(0, how_many):
        name = input('Enter book name: ')
        author = input('Enter author name: ')
        database.add_book(name, author)


def prompt_get_all_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book[
                            'read'] == '1' else 'NO'  # This is saying if book read is true then read == YES else read == False
        print(f"{book['name'].title()} by {book['author'].title()}, read: {read.capitalize()}")


def prompt_mark_book_as_read():
    name = input('what book have you read, enter name: ')
    books = database.mark_book_as_read(name)
    return books


def prompt_delete_book():
    name = input('what book have you read, enter name: ')
    books = database.delete_book(name)
    return books


while user_input != 'q':
    database.check_if_file_exits()

    if user_input == 'a':
        prompt_add_book()
    elif user_input == 'b':
        prompt_get_all_books()
    elif user_input == 'c':
        prompt_mark_book_as_read()
    elif user_input == 'd':
        prompt_delete_book()
    else:
        print('wrong input TRY AGAIN ! ')
        user_input = input(USER_INPUT)

    user_input = input(USER_INPUT)
