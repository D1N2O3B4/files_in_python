from utils.database import add_book,remove_book,read_book,list_all

USER_CHOICE = """Enter:
-a to add books to the database
-d to remove books from the database
-r to mark book as read
-l to list all books in the database
-f in repairs
-q to quit app
"""
# operations = {"a":add_book,
#               "d":remove_book,
#               "r":read_book,
#               "l":list_all}

def choice():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            title = input("Input book title: ")
            author = input("Input book author: ")
            add_book(title,author)
        
        elif user_input == "d":
            title = input("Input book title: ")
            remove_book(title)
            
        elif user_input == "r":
            title = input("Input book title: ")
            read_book(title)
           
        elif user_input == "l":
            list_all()
        user_input = input(USER_CHOICE)  
        
choice()