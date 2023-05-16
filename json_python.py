import json
file = open("files_in_python/json_data.txt","r")
file_content = json.load(file)
file.close()
print(file_content["friends"][1])

"""Write in json using dump"""

books = [
    {"title":"Rich Dad","author":"Robert Kiyosaki"},
    {"title":"Adventures of Mubalak","author":"Soro Jung"}
]

create_file = open("files_in_python/json_books.txt","w")
json.dump(books,create_file)
create_file.close()

stray = '[{"name":"Sammy","father":"Devine"}]'
shot = json.loads(stray)
print(shot[0]["father"])