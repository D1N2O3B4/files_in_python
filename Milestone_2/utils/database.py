books = []

def add_book(title,author):
    books.append({"title":title,"author":author,"read":False})

def read_book(title):
    for i in books:
        if i["title"] == title:
            i["read"] = True
    return None

def remove_book(title):
    for i in books:
        if i["title"] == title:
            books.remove(i)
            return title,"removed succesfully"
    return None

def list_all():
    for i in books:
        return("Book title is",i["title"],"written by",i["author"],". User read book ?:",i["read"])
    return None
# def find_book(title):
#     for i in range(len(books)):
#         name = books[i]["title"]
#         return title,"found at index",i
#     return None

class NoneError(NameError):
    pass


