import json

file = open("files_in_python/Milestone_2_Datatxt/utils/data.txt","r")
file_content = json.load(file)
file.close()


def add_book(title,author):
    with open("data.txt","a") as file:
        file.write(f"Book Title:{title},Author{author},Read{0}")

def read_book(title):
    pass

def remove_book(title):
    pass

def list_all():
    with open("data.txt","r") as file:
        all_books = [line.strip for line in file.readlines()]
        return all_books

def json_func():
    pass