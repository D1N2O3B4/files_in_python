import json
file = open("read_write_files/json_data.txt","r")
file_content = json.load(file)
file.close()
print(file_content["friends"][1])

"""Write in json using dump"""

books = [
    {"title":"Rich Dad","author":"Robert Kiyosaki"},
    {"title":"Adventures of Mubalak","author":"Soro Jung"}
]

create_file = open("read_write_files/json_books.txt","r+")
json.dump(books,create_file)
create_file.close()

stray = '[{"name":"Sammy","father":"Devine"}]'
shot = json.loads(stray)
print(shot[0]["father"])